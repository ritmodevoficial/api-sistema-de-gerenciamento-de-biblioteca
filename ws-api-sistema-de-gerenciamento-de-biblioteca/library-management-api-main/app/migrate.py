# Importa a função create_engine do SQLAlchemy para criar uma conexão com o banco de dados.
from sqlalchemy import create_engine
# Importa a função sessionmaker do SQLAlchemy para criar uma fábrica de sessões.
from sqlalchemy.orm import sessionmaker
# Importa a função declarative_base do SQLAlchemy para definir a base das classes de modelo.
from sqlalchemy.ext.declarative import declarative_base
# Importa a classe URL do SQLAlchemy para facilitar a criação de URLs de conexão com o banco de dados.
from sqlalchemy.engine.url import URL

# Cria uma classe base para os modelos de dados usando o SQLAlchemy.
Base = declarative_base()

# Importa os modelos de dados do módulo database.
from database import Student, BookType, Book, Borrow

# Cria uma URL de conexão com o banco de dados PostgreSQL.
url = URL.create(
    drivername="postgresql",  # Define o tipo do banco de dados.
    username="postgres",      # Nome de usuário para acessar o banco de dados.
    password="",              # Senha do banco de dados (deixa vazia se não houver).
    host="localhost",         # Define o host do banco de dados.
    database="lmsdb",        # Nome do banco de dados a ser utilizado.
    port=5432                 # Porta do banco de dados.
)

# Cria um objeto engine para a conexão com o banco de dados usando a URL criada.
engine = create_engine(url)

# Cria uma fábrica de sessões com configurações para não realizar commit ou flush automaticamente.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Remove todas as tabelas existentes no banco de dados.
Base.metadata.drop_all(engine)

# Recria todas as tabelas no banco de dados com base nos modelos definidos.
Base.metadata.create_all(engine)

# Exibe uma mensagem informando que o reset do banco de dados foi concluído.
print("Database reset complete.")
