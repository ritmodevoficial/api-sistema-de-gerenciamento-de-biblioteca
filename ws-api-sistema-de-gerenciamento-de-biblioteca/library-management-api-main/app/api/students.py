# Importa classes e funções do FastAPI
from fastapi import APIRouter, Depends, HTTPException
# Importa a sessão de conexão ao banco de dados do SQLAlchemy
from sqlalchemy.orm import Session
# Importa a função get_db para obter a conexão com o banco de dados
from ..database import get_db
# Importa os modelos Student e StudentCreate para representar dados de alunos
from ..models.student import Student, StudentCreate
# Importa o modelo Book para representar os livros
from ..models.book import Book
# Importa o serviço relacionado aos alunos
from ..services import student_service

# Cria uma instância de roteador para gerenciar endpoints relacionados a alunos
router = APIRouter(
    # Define o prefixo para as rotas relacionadas a alunos
    prefix="/students",
    # Define a tag "students" para a documentação da API
    tags=["students"],
    # Define uma resposta padrão para o erro 404 (Não encontrado)
    responses={404: {"description": "Not found"}},
)


# Define o endpoint GET para obter a lista de todos os alunos
@router.get("/", response_model=list[Student])
def get_students(db: Session = Depends(get_db)):
    # Chama o serviço para obter a lista de alunos do banco de dados
    return student_service.get_students(db)


# Define o endpoint POST para criar um novo aluno
@router.post("/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Chama o serviço para criar um novo aluno com os dados fornecidos
    return student_service.create_student(db, student)


# Define o endpoint GET para obter os detalhes de um aluno específico pelo ID
@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int, db: Session = Depends(get_db)):
    # Tenta buscar o aluno pelo ID no banco de dados
    try:
        return student_service.get_student_by_id(db, student_id)
    # Lança uma exceção HTTP 500 se ocorrer um erro durante a busca
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define o endpoint PUT para atualizar os dados de um aluno específico pelo ID
@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    # Tenta atualizar os dados do aluno com base no ID e nos novos dados fornecidos
    try:
        return student_service.update_student(db, student_id, student)
    # Lança uma exceção HTTP 500 se ocorrer um erro durante a atualização
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define o endpoint DELETE para remover um aluno específico pelo ID
@router.delete("/{student_id}", response_model=Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    # Tenta deletar o aluno com base no ID fornecido
    try:
        return student_service.delete_student(db, student_id)
    # Lança uma exceção HTTP 500 se ocorrer um erro durante a remoção
    except ValueError as e:
        return HTTPException(status_code=500, detail=str(e))


# Define o endpoint GET para obter a lista de livros emprestados por um aluno específico
@router.get("/{student_id}/borrowed_books", response_model=list[Book])
def get_borrowed_books(student_id: int, db: Session = Depends(get_db)):
    # Tenta buscar os livros emprestados pelo aluno com base no ID
    try:
        return student_service.get_borrowed_books(db, student_id)
    # Lança uma exceção HTTP 500 se ocorrer um erro durante a busca
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
