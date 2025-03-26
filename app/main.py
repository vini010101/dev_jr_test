from fastapi import FastAPI, Depends, Query, HTTPException, Body
from sqlalchemy.orm import Session
from . import crud, models, schemas, services
from .database import SessionLocal, engine
from .scheduler import send_city_to_webhook  # Função do webhook


# Criação das tabelas no banco (se não existirem)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/previsao/", response_model=schemas.Previsao)
async def buscar_previsao(cidade: str = Body(..., embed=True), db: Session = Depends(get_db)):
    """
    Busca a previsão do tempo para a cidade na API externa
    e salva no banco de dados.
    """
    # Busca a previsão da API externa
    previsao = services.buscar_previsao_api(cidade)

    # Salva a previsão no banco de dados
    previsao_salva = crud.salvar_previsao(db=db, previsao=previsao)

    # Gerar os dados a serem enviados para o Webhook a partir dos dados salvos
    previsao_data = {
        "id": previsao_salva.id,
        "cidade": previsao_salva.cidade,
        "temperatura": previsao_salva.temperatura,
        "data": previsao_salva.data.isoformat(),  # Formato ISO 8601
    }

    # Enviar os dados para o webhook
    send_city_to_webhook(previsao_data)

    return previsao_salva



# Rota da API para listar uma ou as cidades Que estão salvas no banco de dados
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



# Função para excluir a previsão de uma cidade
@app.delete("/previsao/{cidade}", response_model=schemas.Previsao)
async def excluir_previsao(cidade: str, db: Session = Depends(get_db)):
    """
    Exclui a previsão de uma cidade específica no banco de dados.
    """
    previsao = crud.excluir_previsao_por_cidade(db, cidade)
    
    if previsao:
        return previsao
    else:
        raise HTTPException(status_code=404, detail=f"Cidade '{cidade}' não encontrada.")