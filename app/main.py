from fastapi import FastAPI
from pydantic import BaseModel
from app.database import carrega_jogos, adiciona_jogo, remove_jogo

app = FastAPI(title="Biblioteca de Jogos")

class Jogo(BaseModel):
    nome: str
    genero: str
    ano: int

@app.get("/")
def home():
    return {"status": "API rodando"}

@app.get("/jogos")
def listar_jogos():
    return carrega_jogos()

@app.post("/jogos")
def criar_jogo(jogo: Jogo):
    adiciona_jogo(jogo.dict())
    return {"msg": "Jogo adicionado"}

@app.delete("/jogos/{nome}")
def deletar_jogo(nome: str):
    remove_jogo(nome)
    return {"msg": "Jogo removido"}
