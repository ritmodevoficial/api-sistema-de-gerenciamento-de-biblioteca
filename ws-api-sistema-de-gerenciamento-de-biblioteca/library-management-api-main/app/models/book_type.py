# Importa a classe BaseModel do Pydantic para validação de dados.
from pydantic import BaseModel


# Define a classe BookType, que representa um modelo de dados para um tipo de livro.
class BookType(BaseModel):
    # Define a variável id como um inteiro obrigatório, representando a identificação do tipo de livro.
    id: int
    # Define a variável subject_name como uma string obrigatória para o nome do tipo de livro.
    subject_name: str

    # Configurações adicionais para a classe BookType.
    class Config:
        # Habilita o modo ORM para permitir a conversão automática de objetos ORM em modelos Pydantic.
        orm_mode = True
