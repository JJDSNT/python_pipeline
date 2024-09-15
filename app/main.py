from fastapi import FastAPI, Depends, UploadFile, File, BackgroundTasks
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, schemas, utils

app = FastAPI()

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)


# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Pipeline de Dados"}

# Outros endpoints como upload_csv, process_data, etc., serão adicionados aqui
