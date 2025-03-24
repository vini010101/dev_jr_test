# app/service.py

from sqlalchemy.orm import Session
import requests
from datetime import datetime
from app.models import Weather
from app.schemas import WeatherCreate
import os

# Variáveis de ambiente para a API
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obter_previsao(cidade: str, db: Session) -> Weather:
    """
    Função que obtém a previsão do tempo da OpenWeatherMap e salva no banco de dados.
    """
    params = {"q": cidade, "appid": API_KEY, "units": "metric", "lang": "pt"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        raise Exception("Erro ao buscar previsão do tempo")

    dados = response.json()
    
    # Criação de um novo registro de previsão no banco de dados
    previsao = Weather(
        cidade=cidade,
        temperatura=str(dados["main"]["temp"]),
        descricao=dados["weather"][0]["description"],
        data_consulta=datetime.utcnow()  # Usando UTC para padronizar a data
    )

    db.add(previsao)
    db.commit()
    db.refresh(previsao)
    
    return previsao

def listar_previsoes(db: Session) -> list[Weather]:
    """
    Função que lista todas as previsões de tempo armazenadas no banco de dados.
    """
    return db.query(Weather).all()

def buscar_previsao(cidade: str, data: str, db: Session) -> list[Weather]:
    """
    Função para buscar previsões filtrando por cidade e data.
    """
    query = db.query(Weather).filter(Weather.cidade == cidade)
    
    if data:
        data_formatada = datetime.strptime(data, "%Y-%m-%d")
        query = query.filter(Weather.data_consulta >= data_formatada)
    
    return query.all()

def deletar_previsao(id: int, db: Session) -> bool:
    """
    Função que deleta um registro de previsão com base no ID fornecido.
    """
    previsao = db.query(Weather).filter(Weather.id == id).first()
    
    if not previsao:
        return False
    
    db.delete(previsao)
    db.commit()
    
    return True
