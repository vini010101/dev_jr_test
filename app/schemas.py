from pydantic import BaseModel
from datetime import datetime

class PrevisaoBase(BaseModel):
    cidade: str
    temperatura: str

class PrevisaoCreate(PrevisaoBase):
    pass

class Previsao(PrevisaoBase):
    id: int
    data: datetime

    class Config:
        orm_mode = True
