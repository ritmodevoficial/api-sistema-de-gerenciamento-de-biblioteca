# Importa a função create_engine para criar uma conexão com o banco de dados.
from sqlalchemy import create_engine
# Importa a classe URL para criar URLs de conexão.
from sqlalchemy.engine.url import URL
# Importa sessionmaker para criar uma fábrica de sessões para interagir com o banco de dados.
from sqlalchemy.orm import sessionmaker
# Importa declarative_base para criar uma base declarativa para os modelos.
from sqlalchemy.ext.declarative import declarative_base

# Cria uma classe base para os modelos que irão ser definidos, permitindo a criação de tabelas no banco de dados.
Base = declarative_base()

# Importa os modelos de dados (Student, BookType, Book, Borrow) definidos em um módulo chamado models.
from .models import Student, BookType, Book, Borrow

# Cria uma URL de conexão para o banco de dados PostgreSQL, definindo os parâmetros necessários.
url = URL.create(
    # Define o driver do banco de dados como PostgreSQL.
    drivername="postgresql",
    # Define o nome de usuário do banco de dados.
    username="postgres",
    # Define a senha do banco de dados (vazia neste caso).
    password="",
    # Define o host onde o banco de dados está rodando (neste caso, localmente).
    host="localhost",
    # Define o nome do banco de dados a ser utilizado.
    database="lmsdb",
    # Define a porta do banco de dados PostgreSQL (padrão é 5432).
    port=5432
)

# Cria um objeto engine que gerencia a conexão com o banco de dados usando a URL definida.
engine = create_engine(url)
# Cria uma fábrica de sessões que será associada ao engine, permitindo criar sessões de banco de dados.
Session = sessionmaker(bind=engine)
# Instancia uma sessão do banco de dados.
session = Session()

# Define uma função para configurar o banco de dados, criando tabelas se necessário.
def setup_database():
    try:
        # Cria todas as tabelas definidas nos modelos que herdam de Base, associando ao engine.
        Base.metadata.create_all(bind=engine)
        # Imprime uma mensagem de sucesso se as tabelas forem criadas.
        print("Tables created successfully!")
    except Exception as e:  # Captura qualquer exceção que ocorra durante a criação das tabelas.
        # Imprime uma mensagem de erro se a criação das tabelas falhar.
        print("An error occurred during table creation:", str(e))

# Função de dependência para obter uma sessão de banco de dados.
def get_db():
    # Instancia uma nova sessão do banco de dados.
    db = Session()
    try:
        # Usa o yield para retornar a sessão como um gerador, permitindo que seja utilizada em um contexto gerenciado.
        yield db
    finally:
        # Garante que a sessão seja fechada após o uso, liberando recursos.
        db.close()
