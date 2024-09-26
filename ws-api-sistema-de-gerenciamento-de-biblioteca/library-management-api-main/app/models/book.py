# Importa a classe Optional do módulo typing para permitir valores opcionais nas variáveis.
from typing import Optional

# Importa as classes BaseModel e NonNegativeInt do Pydantic para validação de dados.
from pydantic import BaseModel, NonNegativeInt


# Define a classe Book, que representa um modelo de dados para um livro.
class Book(BaseModel):
    # Define a variável id como um inteiro opcional.
    id: Optional[int]
    # Define a variável name como uma string obrigatória para o nome do livro.
    name: str
    # Define a variável author como uma string obrigatória para o autor do livro.
    author: str
    # Define a variável copy_number como um inteiro não negativo obrigatório, representando o número de cópias do livro.
    copy_number: NonNegativeInt
    # Define a variável book_type_id como um inteiro opcional, referindo-se ao tipo do livro.
    book_type_id: Optional[int] = None

    # Configurações adicionais para a classe Book.
    class Config:
        # Habilita o modo ORM para permitir a conversão automática de objetos ORM em modelos Pydantic.
        orm_mode = True
