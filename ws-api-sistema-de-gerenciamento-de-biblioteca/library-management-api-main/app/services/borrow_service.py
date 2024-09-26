# Importa a classe Session do SQLAlchemy para trabalhar com sessões de banco de dados.
from sqlalchemy.orm import Session
# Importa os modelos Book, Borrow e Student do módulo models para interagir com as tabelas correspondentes.
from ..database.models import Book as BookModel, Borrow as BorrowModel, Student as StudentModel


# Função para emprestar um livro a um estudante.
def borrow_book(db: Session, student_id: int, book_id: int):
    # Busca o livro pelo ID fornecido.
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    # Busca o estudante pelo ID fornecido.
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()

    # Se o livro não for encontrado, levanta uma exceção com uma mensagem de erro.
    if db_book is None:
        raise ValueError("Book not found!")
    # Se o estudante não for encontrado, levanta uma exceção com uma mensagem de erro.
    elif db_student is None:
        raise ValueError("Student not found!")
    # Se não houver cópias disponíveis do livro, levanta uma exceção.
    elif db_book.copy_number < 1:
        raise ValueError("No available copies of the book!")
    # Se o estudante já tiver emprestado o mesmo livro, levanta uma exceção.
    elif db.query(BorrowModel).filter(BorrowModel.book_id == book_id, BorrowModel.student_id == student_id).first() is not None:
        raise ValueError("Student already borrowed this book!")
    # Se o estudante já tiver emprestado 3 livros, levanta uma exceção.
    elif len(db_student.borrowed_books) >= 3:
        raise ValueError("Student already borrowed 3 books!")

    # Cria uma nova instância de BorrowModel para registrar o empréstimo.
    borrow = BorrowModel(student_id=student_id, book_id=book_id)
    db.add(borrow)  # Adiciona o registro do empréstimo à sessão do banco de dados.
    db_book.copy_number -= 1  # Decrementa o número de cópias do livro.
    db.commit()  # Realiza a transação para persistir os dados no banco de dados.
    db.refresh(borrow)  # Atualiza a instância do empréstimo com os dados mais recentes do banco de dados.

    return borrow  # Retorna o registro do empréstimo.


# Função para retornar um livro emprestado.
def return_book(db: Session, borrow_id: int):
    # Busca o registro do empréstimo pelo ID fornecido.
    db_borrow = db.query(BorrowModel).filter(BorrowModel.id == borrow_id).first()
    # Se o empréstimo não for encontrado, levanta uma exceção com uma mensagem de erro.
    if db_borrow is None:
        raise ValueError("Borrow not found!")

    # Busca o livro correspondente ao empréstimo.
    db_book = db.query(BookModel).filter(BookModel.id == db_borrow.book_id).first()
    db.delete(db_borrow)  # Deleta o registro do empréstimo da sessão do banco de dados.
    db_book.copy_number += 1  # Incrementa o número de cópias do livro.
    db.commit()  # Realiza a transação para persistir as alterações no banco de dados.

    return {"message": "Book returned successfully"}  # Retorna uma mensagem de sucesso.
