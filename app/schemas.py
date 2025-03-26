from pydantic import BaseModel
from datetime import datetime

class PrevisaoBase(BaseModel):
    cidade: str
    temperatura: float
    data: datetime

class PrevisaoCreate(PrevisaoBase):
    pass

class Previsao(PrevisaoBase):
    id: int

    class Config:
        orm_mode = True
