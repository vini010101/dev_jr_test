from sqlalchemy.orm import Session
from . import models, schemas

def salvar_previsao(db: Session, previsao: schemas.PrevisaoCreate):
    db_previsao = models.Previsao(cidade=previsao.cidade, temperatura=previsao.temperatura)
    db.add(db_previsao)
    db.commit()
    db.refresh(db_previsao)
    return db_previsao

def listar_previsoes(db: Session, cidade: str = None, data: str = None):
    query = db.query(models.Previsao)
    if cidade:
        query = query.filter(models.Previsao.cidade == cidade)
    if data:
        query = query.filter(models.Previsao.data == data)
    return query.all()



def excluir_previsao_por_cidade(db: Session, cidade: str):
    """
    Exclui a previsão de uma cidade específica no banco de dados.
    """
    previsao = db.query(models.Previsao).filter(models.Previsao.cidade == cidade).first()
    
    if previsao:
        db.delete(previsao)
        db.commit()
        return previsao
    return None