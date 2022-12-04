from fastapi import FastAPI
from pydantic import BaseModel
import bd

app = FastAPI()


@app.get("/alunos")
async def root():
    return {"message": "Hello World"}


@app.get("/grupos/{cpf}")
async def retorna_horarios(cpf):
    return bd.buscar_alunos_no_bd(cpf) 


