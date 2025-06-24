### Regras da aplicação

[X] - Deve ser possível registrar uma refeição feita, com as seguintes informações:
    [X] - Nome
    [X] - Descrição
    [X] - Data e Hora
    [X] - Está dentro ou não da dieta
[X] - Deve ser possível editar uma refeição, podendo alterar todos os dados acima
[X] - Deve ser possível apagar uma refeição
[X] - Deve ser possível listar todas as refeições de um usuário
[X] - Deve ser possível visualizar uma única refeição
[X] - As informações devem ser salvas em um banco de dados

## Começando

**Clone o projeto e acesse a pasta**

```bash
$ git clone https://github.com/thoomassf/daily-diet-api.git && cd daily-diet-api
$ gh repo clone thoomassf/daily-diet-api && cd daily-diet-api
```

**Siga os passos abaixo**
```bash
# Instalar as dependências
pip install -q requirements.txt

# Crie o arquivo .env com base no .env.example

# Iniciar banco dados no docker (MySQL)
docker compose up -d

# Iniciar banco de dados local (SQLite)
flask shell
db.create_all()
db.session.commit()
exit()

# Iniciar o servidor
flask run --reload
```