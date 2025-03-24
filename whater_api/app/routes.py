from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, service, database
import datetime

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/previsao/")
def obter_previsao(cidade: str, db: Session = Depends(get_db)):
    """
    Endpoint para obter a previsão do tempo para uma cidade e armazenar no banco de dados.
    """
  
    previsao = service.obter_previsao_do_tempo(cidade)
    if previsao:
    
        previsao_db = models.Weather(
            cidade=cidade,
            temperatura=previsao["temperatura"],
            descricao=previsao["descricao"],
            data_consulta=datetime.datetime.now(datetime.timezone.utc)
        )
        db.add(previsao_db)
        db.commit()
        db.refresh(previsao_db)
        return previsao_db
    else:
        raise HTTPException(status_code=400, detail="Erro ao obter dados da previsão")

@router.get("/previsao/")
def listar_previsoes(db: Session = Depends(get_db)):
    """
    Endpoint para listar todas as previsões armazenadas no banco de dados.
    """
    previsoes = db.query(models.Weather).all()
    return previsoes

@router.get("/previsao/{id}")
def buscar_previsao_por_id(id: int, db: Session = Depends(get_db)):
    """
    Endpoint para buscar uma previsão específica pelo ID.
    """
    previsao = db.query(models.Weather).filter(models.Weather.id == id).first()
    if not previsao:
        raise HTTPException(status_code=404, detail="Previsão não encontrada")
    return previsao

@router.get("/previsao/cidade")
def buscar_previsao_por_cidade(cidade: str, data: str = None, db: Session = Depends(get_db)):
    """
    Endpoint para buscar previsões por cidade e, opcionalmente, por data.
    """
    query = db.query(models.Weather).filter(models.Weather.cidade == cidade)
    
    if data:
        data_formatada = datetime.datetime.strptime(data, "%Y-%m-%d")
        query = query.filter(models.Weather.data_consulta >= data_formatada)
    
    previsoes = query.all()
    return previsoes

@router.delete("/previsao/{id}")
def deletar_previsao(id: int, db: Session = Depends(get_db)):
    """
    Endpoint para excluir uma previsão específica pelo ID.
    """
    previsao = db.query(models.Weather).filter(models.Weather.id == id).first()
    if not previsao:
        raise HTTPException(status_code=404, detail="Previsão não encontrada")
    
    db.delete(previsao)
    db.commit()
    return {"message": "Registro deletado com sucesso"}
