# Importa a classe FastAPI do módulo fastapi para criar a aplicação.
from fastapi import FastAPI
# Importa os módulos de API para livros, estudantes e empréstimos.
from app.api import books, students, borrows
# Importa a função para configurar o banco de dados.
from app.database import setup_database

# Chama a função para configurar o banco de dados (criação de tabelas).
setup_database()

# Cria uma instância da aplicação FastAPI.
app = FastAPI()

# Inclui o roteador de livros na aplicação.
app.include_router(books.router)
# Inclui o roteador de estudantes na aplicação.
app.include_router(students.router)
# Inclui o roteador de empréstimos na aplicação.
app.include_router(borrows.router)

# Verifica se o script está sendo executado diretamente.
if __name__ == "__main__":
    # Importa o módulo uvicorn para executar o servidor ASGI.
    import uvicorn
    # Inicia o servidor Uvicorn com o aplicativo FastAPI, escutando em todas as interfaces na porta 8000.
    uvicorn.run(app, host="0.0.0.0", port=8000)
