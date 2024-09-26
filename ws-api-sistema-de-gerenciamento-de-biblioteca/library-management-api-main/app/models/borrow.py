# Importa a classe BaseModel do Pydantic para validação de dados.
from pydantic import BaseModel


# Define a classe Borrow, que representa um modelo de dados para um empréstimo de livro.
class Borrow(BaseModel):
    # Define a variável student_id como um inteiro obrigatório, representando a identificação do estudante que fez o empréstimo.
    student_id: int
    # Define a variável book_id como um inteiro obrigatório, representando a identificação do livro que foi emprestado.
    book_id: int

    # Configurações adicionais para a classe Borrow.
    class Config:
        # Habilita o modo ORM para permitir a conversão automática de objetos ORM em modelos Pydantic.
        orm_mode = True
