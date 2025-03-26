from fastapi import FastAPI, Depends, Query, HTTPException, Body
from sqlalchemy.orm import Session
from apscheduler.schedulers.background import BackgroundScheduler
from . import crud, models, schemas, services
from .database import SessionLocal, engine
from .scheduler import verificar_e_enviar_para_webhook

# Criação das tabelas no banco (se não existirem)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Função que será chamada pelo agendador para verificar novos dados e enviar ao webhook
def job():
    # Obtenha a sessão do banco de dados diretamente aqui
    db = SessionLocal()
    print("Verificando novos dados e enviando para o webhook...")
    verificar_e_enviar_para_webhook(db)
    db.close()  # Fechar a sessão após a execução

# Inicialize o agendador
scheduler = BackgroundScheduler()

@app.on_event("startup")
async def start_scheduler():
    print("Iniciando agendador...")
    # Agendar a execução do job a cada 1 minuto
    scheduler.add_job(job, 'interval', minutes=1)
    scheduler.start()

@app.on_event("shutdown")
async def shutdown_scheduler():
    print("Parando agendador...")
    scheduler.shutdown()

# Endpoint para buscar previsões e salvar no banco de dados
@app.post("/previsao/", response_model=schemas.Previsao)
async def buscar_previsao(cidade: str = Body(..., embed=True), db: Session = Depends(get_db)):
    previsao = services.buscar_previsao_api(cidade)
    if not previsao:
        raise HTTPException(status_code=404, detail="Previsão não encontrada.")
    previsao_salva = crud.salvar_previsao(db=db, previsao=previsao)
    return previsao_salva


@app.get("/previsao/", response_model=list[schemas.Previsao])
async def listar_previsoes(
    cidade: str = Query(None, description="Nome da cidade para previsão", example="São Paulo"),
    data: str = Query(None, description="Data da previsão (YYYY-MM-DD)", example="2025-03-25"),
    db: Session = Depends(get_db)
):
    """
    Lista previsões filtrando por cidade e data (opcionais).
    Se a cidade não estiver no banco, consulta na API externa e salva.
    """
    # Tenta buscar previsões no banco de dados
    previsoes = crud.listar_previsoes(db=db, cidade=cidade, data=data)
    
    if not previsoes:
        # Se a cidade não existir no banco, faz a requisição para a API externa
        previsao = services.buscar_previsao_api(cidade)
        
        if previsao:
            # Salva a previsão no banco de dados
            previsao_salva = crud.salvar_previsao(db=db, previsao=previsao)
            return [previsao_salva]  # Retorna a previsão recém-salva
        else:
            raise HTTPException(status_code=404, detail="Previsão não encontrada para a cidade.")
    
    return previsoes

# Função para excluir previsão de cidade
@app.delete("/previsao/{cidade}", response_model=schemas.Previsao)
async def excluir_previsao(cidade: str, db: Session = Depends(get_db)):
    previsao = crud.excluir_previsao_por_cidade(db, cidade)
    if previsao:
        return previsao
    else:
        raise HTTPException(status_code=404, detail="Cidade não encontrada.")
