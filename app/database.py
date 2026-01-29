import json

Arquivo = "app/database.json"

def carrega_jogos():
    with open(Arquivo, "r", encoding="utf-8") as f:
        return json.load(f)
    

def salva_jogos(jogos):
    with open(Arquivo, "w", encoding="utf-8") as f:
        json.dump(jogos, f, ensure_ascii=False, indent=4)


def adiciona_jogo(jogo):
    jogos = carrega_jogos()
    jogos.append(jogo)
    salva_jogos(jogos)

def remove_jogo(nome):
    jogos = carrega_jogos()
    jogos = [jogo for jogo in jogos if jogo["nome"] != nome]
    salva_jogos(jogos)

