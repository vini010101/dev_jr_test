from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Caminho do banco de dados

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # Importante para o SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
