# Importa classes e funções do FastAPI
from fastapi import APIRouter, Depends, HTTPException
# Importa a classe List do módulo typing para definir listas tipadas
from typing import List
# Importa a sessão de conexão ao banco de dados do SQLAlchemy
from sqlalchemy.orm import Session
# Importa a função get_db para obter a conexão com o banco de dados
from ..database import get_db
# Importa o modelo de dados Book do módulo models
from ..models.book import Book
# Importa serviços do módulo book_service para realizar operações no banco de dados
from ..services.book_service import get_all_books, get_book_by_id, create_book, update_book, delete_book

# Cria uma instância de roteador para gerenciar endpoints relacionados a livros
router = APIRouter(
    # Define o prefixo para as rotas de livros
    prefix="/books",
    # Define a tag "books" para facilitar a documentação da API
    tags=["books"],
    # Define uma resposta padrão para o erro 404 (Não encontrado)
    responses={404: {"description": "Not found"}}, )


# Define o endpoint GET para obter todos os livros
@router.get("/", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    # Chama a função get_all_books para retornar a lista de livros
    return get_all_books(db)


# Define o endpoint GET para obter um livro específico pelo seu ID
@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    # Tenta buscar o livro pelo ID
    try:
        return get_book_by_id(db, book_id)
    # Se ocorrer um erro (ex: livro não encontrado), lança uma exceção HTTP com o código 500
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define o endpoint POST para criar um novo livro
@router.post("/create", response_model=Book)
def create_new_book(book: Book, db: Session = Depends(get_db)):
    # Tenta criar um novo livro
    try:
        return create_book(db, book)
    # Se ocorrer um erro, lança uma exceção HTTP com o código 500
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define o endpoint PUT para atualizar um livro existente
@router.put("/update/{book_id}", response_model=Book)
def update_existing_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    # Tenta atualizar o livro pelo ID
    try:
        return update_book(db, book_id, book)
    # Se ocorrer um erro, lança uma exceção HTTP com o código 500
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define o endpoint DELETE para remover um livro existente
@router.delete("/remove/{book_id}", response_model=Book)
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    # Tenta deletar o livro pelo ID
    try:
        return delete_book(db, book_id)
    # Se ocorrer um erro, lança uma exceção HTTP com o código 500
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
