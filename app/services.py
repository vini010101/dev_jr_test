import requests
from .schemas import PrevisaoCreate
from sqlalchemy.orm import Session
from . import models, schemas


OPENWEATHERMAP_API_KEY = "b3cc4c01de119283f79908e4cc21646f"




def salvar_previsao(db: Session, previsao: schemas.PrevisaoCreate):
    db_previsao = models.Previsao(
        cidade=previsao.cidade,
        temperatura=float(previsao.temperatura)  # Convertendo para número
    )
    db.add(db_previsao)
    db.commit()
    db.refresh(db_previsao)
    return db_previsao


def buscar_previsao_api(cidade: str) -> PrevisaoCreate:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        raise Exception(f"Erro ao obter dados para a cidade: {cidade}")
    
    temperatura = data["main"]["temp"]
    return PrevisaoCreate(cidade=cidade, temperatura=str(temperatura))