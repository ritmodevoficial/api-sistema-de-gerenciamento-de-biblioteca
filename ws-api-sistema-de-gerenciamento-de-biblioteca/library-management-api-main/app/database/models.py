# Importa as classes Column, Integer, String e ForeignKey do SQLAlchemy para definir colunas de tabelas.
from sqlalchemy import Column, Integer, String, ForeignKey
# Importa a função relationship para definir relacionamentos entre tabelas.
from sqlalchemy.orm import relationship
# Importa a classe Base que serve como base para a definição dos modelos.
from . import Base


# Define a classe Student, que representa a tabela "students" no banco de dados.
class Student(Base):
    __tablename__ = "students"  # Define o nome da tabela no banco de dados.

    # Define a coluna id como chave primária e índice.
    id = Column(Integer, primary_key=True, index=True)
    # Define a coluna name para armazenar o nome do estudante.
    name = Column(String)
    # Define a coluna department para armazenar o departamento do estudante.
    department = Column(String)
    # Define um relacionamento com a tabela Borrow, indicando que um estudante pode ter muitos livros emprestados.
    borrowed_books = relationship("Borrow", back_populates="student")


# Define a classe BookType, que representa a tabela "book_types" no banco de dados.
class BookType(Base):
    __tablename__ = "book_types"  # Define o nome da tabela no banco de dados.

    # Define a coluna id como chave primária e índice.
    id = Column(Integer, primary_key=True, index=True)
    # Define a coluna subject_name para armazenar o nome do tipo de livro.
    subject_name = Column(String)
    # Define um relacionamento com a tabela Book, indicando que um tipo de livro pode ter muitos livros associados.
    books = relationship("Book", back_populates="book_type")


# Define a classe Book, que representa a tabela "books" no banco de dados.
class Book(Base):
    __tablename__ = "books"  # Define o nome da tabela no banco de dados.

    # Define a coluna id como chave primária e índice.
    id = Column(Integer, primary_key=True, index=True)
    # Define a coluna name para armazenar o nome do livro.
    name = Column(String)
    # Define a coluna author para armazenar o nome do autor do livro.
    author = Column(String)
    # Define a coluna copy_number para armazenar o número de cópias do livro.
    copy_number = Column(Integer)
    # Define a coluna book_type_id como chave estrangeira que referencia a tabela book_types.
    book_type_id = Column(Integer, ForeignKey("book_types.id", ondelete="SET NULL", onupdate="CASCADE"))
    # Define um relacionamento com a tabela BookType, indicando a que tipo de livro este livro pertence.
    book_type = relationship("BookType", back_populates="books")
    # Define um relacionamento com a tabela Borrow, indicando que um livro pode ter muitos empréstimos.
    borrows = relationship("Borrow", back_populates="book")


# Define a classe Borrow, que representa a tabela "borrows" no banco de dados.
class Borrow(Base):
    __tablename__ = "borrows"  # Define o nome da tabela no banco de dados.

    # Define a coluna id como chave primária e índice.
    id = Column(Integer, primary_key=True, index=True)
    # Define a coluna student_id como chave estrangeira que referencia a tabela students.
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE"))
    # Define a coluna book_id como chave estrangeira que referencia a tabela books.
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE", onupdate="CASCADE"))
    # Define um relacionamento com a tabela Student, indicando qual estudante fez o empréstimo.
    student = relationship("Student", back_populates="borrowed_books")
    # Define um relacionamento com a tabela Book, indicando qual livro foi emprestado.
    book = relationship("Book", back_populates="borrows")
