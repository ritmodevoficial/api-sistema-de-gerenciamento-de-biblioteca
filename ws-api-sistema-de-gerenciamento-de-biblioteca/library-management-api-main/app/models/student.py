# Importa a classe BaseModel do Pydantic para validação de dados.
from pydantic import BaseModel


# Modelo usado ao criar um novo estudante.
class StudentCreate(BaseModel):
    # Define a variável name como uma string obrigatória para o nome do estudante.
    name: str
    # Define a variável department como uma string obrigatória para o departamento do estudante.
    department: str


# Modelo usado ao recuperar ou atualizar um estudante, herda de StudentCreate.
class Student(StudentCreate):
    # Define a variável id como um inteiro obrigatório, representando a identificação do estudante.
    id: int

    # Configurações adicionais para a classe Student.
    class Config:
        # Habilita o modo ORM para permitir a conversão automática de objetos ORM em modelos Pydantic.
        orm_mode = True
