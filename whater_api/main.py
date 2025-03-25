from fastapi import FastAPI, HTTPException, Depends, APIRouter
from .models import Weather
from .routes import router  # Importando as rotas do arquivo routes.py
import sys
import os

from sqlalchemy.orm import Session
from . import models, service  # Certifique-se de que o módulo service e modelos estão importados corretamente
from .database import get_db  # Se você tiver um arquivo database.py com a função get_db
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


app = FastAPI()




# Incluindo o roteador das previsões
app.include_router(router)  # Incluindo as rotas definidas em routes.py


# Criando o router para agrupar as rotas
router = APIRouter()

# Rota POST para adicionar uma previsão
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

# Rota GET para listar todas as previsões
@router.get("/previsao/")
def listar_previsoes(db: Session = Depends(get_db)):
    """
    Endpoint para listar todas as previsões armazenadas no banco de dados.
    """
    previsoes = db.query(models.Weather).all()
    return previsoes

# Rota GET para buscar previsão por ID
@router.get("/previsao/{id}")
def buscar_previsao_por_id(id: int, db: Session = Depends(get_db)):
    """
    Endpoint para buscar uma previsão específica pelo ID.
    """
    previsao = db.query(models.Weather).filter(models.Weather.id == id).first()
    if not previsao:
        raise HTTPException(status_code=404, detail="Previsão não encontrada")
    return previsao

# Rota GET para buscar previsões por cidade
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

# Rota DELETE para excluir previsão por ID
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

# Incluindo o router no FastAPI
app.include_router(router)