from pydantic import BaseModel
from datetime import datetime

class WeatherBase(BaseModel):
    cidade: str
    temperatura: str
    descricao: str

    class Config:
        orm_mode = True

class WeatherCreate(WeatherBase):
    pass

class Weather(WeatherBase):
    id: int
    data_consulta: datetime

    class Config:
        orm_mode = True
