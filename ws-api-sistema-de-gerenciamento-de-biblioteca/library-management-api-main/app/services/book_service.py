# Importa a classe Session do SQLAlchemy para trabalhar com sessões de banco de dados.
from sqlalchemy.orm import Session
# Importa os modelos Book e BookType do módulo models para interagir com as tabelas correspondentes.
from ..database.models import Book as BookModel, BookType as BookTypeModel


# Função para obter todos os livros do banco de dados.
def get_all_books(db: Session) -> object:
    # Executa uma consulta para retornar todos os registros da tabela Book.
    return db.query(BookModel).all()


# Função para obter um livro específico pelo seu ID.
def get_book_by_id(db: Session, book_id: int) -> object:
    # Executa uma consulta para buscar o livro pelo ID.
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    # Se o livro não for encontrado, levanta uma exceção com uma mensagem de erro.
    if book is None:
        raise ValueError("Book not found!")
    return book


# Função para criar um novo livro no banco de dados.
def create_book(db: Session, book: dict):
    # Verifica se o tipo de livro existe no banco de dados.
    db_book_type = db.query(BookTypeModel).filter(BookTypeModel.id == book.book_type_id).first()
    if db_book_type is None:
        raise ValueError("Book type not found!")

    # Verifica se o campo id opcional existe.
    if book.id is not None:
        # Verifica se já existe um livro com o mesmo ID.
        db_book_id = db.query(BookModel).filter(BookModel.id == book.id).first()
        if db_book_id is not None:
            raise ValueError("Appointed id already exists!")

    # Verifica se já existe um livro com o mesmo nome e autor.
    db_book = db.query(BookModel).filter(BookModel.name == book.name, BookModel.author == book.author).first()

    # Se um livro com o mesmo nome e autor já existir, levanta um erro.
    if db_book is not None:
        raise ValueError("Book already exists!")

    # Cria uma nova instância de BookModel com os dados fornecidos e adiciona ao banco de dados.
    db_book = BookModel(**book.dict())
    db.add(db_book)  # Adiciona o livro à sessão do banco de dados.
    db.commit()  # Realiza a transação para persistir os dados no banco de dados.
    db.refresh(db_book)  # Atualiza a instância do livro com os dados mais recentes do banco de dados.

    return db_book  # Retorna o livro recém-criado.


# Função para atualizar um livro existente no banco de dados.
def update_book(db: Session, book_id: int, book):
    # Busca o livro pelo ID fornecido.
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    # Se o livro não for encontrado, levanta uma exceção com uma mensagem de erro.
    if db_book is None:
        raise ValueError("Book not found!")

    # Verifica se o tipo de livro existe no banco de dados.
    db_book_type = db.query(BookTypeModel).filter(BookTypeModel.id == book.book_type_id).first()

    if db_book_type is None:
        raise ValueError("Book type not found!")

    # Atualiza os atributos do livro com os novos valores fornecidos.
    for key, value in book.dict().items():
        setattr(db_book, key, value)  # Define o valor do atributo correspondente no livro.

    db.commit()  # Realiza a transação para persistir as alterações no banco de dados.
    db.refresh(db_book)  # Atualiza a instância do livro com os dados mais recentes do banco de dados.

    return db_book  # Retorna o livro atualizado.


# Função para deletar um livro do banco de dados.
def delete_book(db: Session, book_id: int):
    # Busca o livro pelo ID fornecido.
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    # Se o livro não for encontrado, levanta uma exceção com uma mensagem de erro.
    if db_book is None:
        raise ValueError("Book not found!")

    db.delete(db_book)  # Deleta o livro da sessão do banco de dados.
    db.commit()  # Realiza a transação para persistir a remoção no banco de dados.

    return db_book  # Retorna o livro que foi deletado.
