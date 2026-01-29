#  Biblioteca de Jogos – Backend + Cliente C#

Projeto de estudo que implementa uma **API REST em Python (FastAPI)** para gerenciar uma biblioteca de jogos, com um **cliente em C#** que consome essa API via HTTP.

O objetivo é praticar conceitos reais de backend, integração entre linguagens e arquitetura de software.

---

## Tecnologias Utilizadas

### Backend
- Python 3
- FastAPI
- Uvicorn
- JSON (como banco de dados inicial)

### Cliente
- C#
- .NET Console Application
- HttpClient
- System.Text.Json

---

## Estrutura do Projeto

biblioteca-jogos-backend/
│
├── app/
│ ├── main.py # Rotas da API
│ ├── database.py # Acesso e manipulação dos dados
│ └── init.py
│
├── BibliotecaJogosClient/
│ ├── Program.cs # Cliente C#
│ ├── Jogo.cs # Modelo de dados
│ └── *.csproj
│
├── database.json # Banco de dados (ignorado no Git)
└── README.md


---

##  Funcionalidades Atuais

### Backend (FastAPI)
-  Listar jogos (`GET /jogos`)
-  Adicionar jogo (`POST /jogos`)
-  Remover jogo (`DELETE /jogos/{nome}`)
-  Persistência em arquivo JSON

### Cliente C#
-  Enviar jogo para o backend via HTTP POST
-  Serialização de objetos para JSON
-  Comunicação direta com API REST

---

## Como Rodar o Projeto

###  Backend (Python)

```bash
cd biblioteca-jogos-backend
.venv\Scripts\activate
uvicorn app.main:app --reload

Acesse:
- API: http://127.0.0.1:8000/jogos
- DOCS: http://127.0.0.1:8000/docs

Cliente C# (.NET)

Em outro terminal:

cd BibliotecaJogosClient
dotnet run

Conceitos Trabalhados

API REST

Separação de responsabilidades

Comunicação via HTTP

Integração entre Python e C#

Serialização / Desserialização JSON

Arquitetura backend básica

Debug de erros reais

 Autor

Projeto desenvolvido para estudo e prática de backend e integração entre linguagens.


