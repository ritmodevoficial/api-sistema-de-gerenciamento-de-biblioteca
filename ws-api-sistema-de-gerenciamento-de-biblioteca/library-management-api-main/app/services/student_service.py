# Importa a classe Session do SQLAlchemy para trabalhar com sessões de banco de dados.
from sqlalchemy.orm import Session
# Importa a exceção HTTPException do FastAPI para lançar erros HTTP.
from fastapi import HTTPException
# Importa o modelo Student do módulo models para interagir com a tabela correspondente.
from ..database.models import Student as StudentModel
# Importa o modelo StudentCreate do módulo student para criação de estudantes.
from ..models.student import StudentCreate


# Função para obter todos os estudantes do banco de dados.
def get_students(db: Session):
    return db.query(StudentModel).all()  # Retorna a lista de todos os estudantes.


# Função para obter um estudante específico pelo seu ID.
def get_student_by_id(db: Session, student_id: int):
    # Busca o estudante pelo ID fornecido.
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    # Se o estudante não for encontrado, levanta uma exceção HTTP 404.
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student  # Retorna o estudante encontrado.


# Função para criar um novo estudante no banco de dados.
def create_student(db: Session, student: StudentCreate):
    # Cria uma nova instância de StudentModel usando os dados do estudante.
    db_student = StudentModel(**student.dict())
    db.add(db_student)  # Adiciona o estudante à sessão do banco de dados.
    db.commit()  # Realiza a transação para persistir os dados.
    db.refresh(db_student)  # Atualiza a instância do estudante com os dados mais recentes do banco de dados.
    return db_student  # Retorna o estudante criado.


# Função para atualizar as informações de um estudante existente.
def update_student(db: Session, student_id: int, student_update: StudentCreate):
    # Busca o estudante pelo ID fornecido.
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()

    # Se o estudante não for encontrado, levanta uma exceção HTTP 404.
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Atualiza os atributos do estudante com os novos dados fornecidos.
    for key, value in student_update.dict().items():
        setattr(db_student, key, value)
    db.commit()  # Realiza a transação para persistir as alterações.
    db.refresh(db_student)  # Atualiza a instância do estudante com os dados mais recentes do banco de dados.
    return db_student  # Retorna o estudante atualizado.


# Função para deletar um estudante do banco de dados.
def delete_student(db: Session, student_id: int):
    # Busca o estudante pelo ID fornecido.
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()

    # Se o estudante não for encontrado, levanta uma exceção HTTP 404.
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(db_student)  # Remove o estudante da sessão do banco de dados.
    db.commit()  # Realiza a transação para persistir as alterações.
    return db_student  # Retorna o estudante deletado.


# Função para obter os livros emprestados por um estudante específico.
def get_borrowed_books(db: Session, student_id: int):
    # Busca o estudante pelo ID fornecido.
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()

    # Se o estudante não for encontrado, levanta uma exceção HTTP 404.
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Adiciona os detalhes dos livros emprestados à lista.
    borrowed_books_list = []
    for borrow in db_student.borrowed_books:
        borrowed_books_list.append(borrow.book)  # Adiciona cada livro à lista de livros emprestados.
    return borrowed_books_list  # Retorna a lista de livros emprestados.
