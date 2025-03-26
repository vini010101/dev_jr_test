from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base
from datetime import datetime, timezone

class Previsao(Base):
    __tablename__ = "previsoes"

    id = Column(Integer, primary_key=True, index=True)
    cidade = Column(String, index=True)
    temperatura = Column(String)
    data = Column(DateTime, default=datetime.now(timezone.utc))
    enviado = Column(Boolean, default=False)