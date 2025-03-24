from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
import datetime

class Weather(Base):
    __tablename__ = "weather"
    
    id = Column(Integer, primary_key=True, index=True)
    cidade = Column(String, index=True)
    temperatura = Column(String)
    descricao = Column(String)
    data_consulta = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
