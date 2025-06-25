# Daily Diet API 🥗

API para gerenciamento de refeições e controle de dieta.

Este projeto permite que um usuário registre, edite, visualize e apague refeições, com informações sobre se está ou não dentro da dieta.  
As informações são armazenadas em banco de dados.

---

## ✨ Funcionalidades

- ✅ Registrar uma refeição:
  - Nome
  - Descrição
  - Data e Hora
  - Indicação se está ou não dentro da dieta
- ✅ Editar uma refeição
- ✅ Apagar uma refeição
- ✅ Listar todas as refeições de um usuário
- ✅ Visualizar uma única refeição
- ✅ Persistência em banco de dados (SQLite ou MySQL)
- ✅ Proteção com autenticação via login

---

## 🚀 Tecnologias

- Python 3.13+
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite ou MySQL (via Docker)

---

## 🛠️ Regras da aplicação

- [x] Deve ser possível registrar uma refeição feita
- [x] Deve ser possível editar uma refeição
- [x] Deve ser possível apagar uma refeição
- [x] Deve ser possível listar todas as refeições de um usuário
- [x] Deve ser possível visualizar uma única refeição
- [x] As informações devem ser salvas em um banco de dados

---

## 🏁 Começando

### 📥 Clone o projeto

```bash
git clone https://github.com/thoomassf/daily-diet-api.git && cd daily-diet-api
# ou
gh repo clone thoomassf/daily-diet-api && cd daily-diet-api
```

### ⚙️ Instalação das dependências
```bash
pip install -r requirements.txt
```

### 🔐 Configuração do ambiente
Crie o arquivo .env com base no .env.example:
```bash
cp .env.example .env
```
Edite suas variáveis de ambiente conforme necessário.

### 📈 Inicializar banco de dados
Opção 1: Banco de dados no Docker (MySQL)
```bash
docker-compose up -d
```
Opção 2: Banco de dados local (SQLite)
```bash
flask shell
>>> from database import db
>>> db.create_all()
>>> db.session.commit()
>>> exit()
```

### 🚀 Rodar o servidor
```bash
flask run --reload
```
A aplicação estará disponível em: http://localhost:5000