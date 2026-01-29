from pydantic import BaseModel

class Jogo(BaseModel):
    nome: str
    genero: str
    ano: int
    plataforma: str