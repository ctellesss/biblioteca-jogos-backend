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

## 🔌 Funcionalidades Atuais

### Backend (FastAPI)
- ✅ Listar jogos (`GET /jogos`)
- ✅ Adicionar jogo (`POST /jogos`)
- ✅ Remover jogo (`DELETE /jogos/{nome}`)
- ✅ Persistência em arquivo JSON

### Cliente C#
- ✅ Enviar jogo para o backend via HTTP POST
- ✅ Serialização de objetos para JSON
- ✅ Comunicação direta com API REST

---

## ▶️ Como Rodar o Projeto

### 1️⃣ Backend (Python)

```bash
cd biblioteca-jogos-backend
.venv\Scripts\activate
uvicorn app.main:app --reload

Acesse:
- API: http://127.0.0.1:8000/jogos
- DOCS: http://127.0.0.1:8000/docs

2️⃣ Cliente C# (.NET)

Em outro terminal:

cd BibliotecaJogosClient
dotnet run

🧠 Conceitos Trabalhados

API REST

Separação de responsabilidades

Comunicação via HTTP

Integração entre Python e C#

Serialização / Desserialização JSON

Arquitetura backend básica

Debug de erros reais

🔮 Próximos Passos (Ideias para Evolução)

🔹 Criar menu interativo no cliente C#

🔹 Listar jogos via GET no C#

🔹 Remover jogos via DELETE no C#

🔹 Substituir JSON por SQLite ou PostgreSQL

🔹 Criar validação com Pydantic

🔹 Criar testes automatizados

🔹 Adicionar autenticação simples

🔹 Criar frontend (React / Blazor)

👨‍💻 Autor

Projeto desenvolvido para estudo e prática de backend e integração entre linguagens.

---

# 🏁 O QUE VOCÊ TEM AGORA

✔️ Projeto versionado  
✔️ README profissional  
✔️ Arquitetura clara  
✔️ Histórico de aprendizado real  
✔️ Algo **mostrável em entrevista / portfólio**

Se você quiser, no próximo passo eu posso:
- 🔹 te ajudar a **finalizar o projeto “versão 1.0”**
- 🔹 adaptar esse projeto para **LinkedIn / portfólio**
- 🔹 ou evoluir ele para nível **júnior backend**

É só dizer 🚀
::contentReference[oaicite:0]{index=0}
