# Importa classes e funções do FastAPI
from fastapi import APIRouter, Depends, HTTPException
# Importa a sessão de conexão ao banco de dados do SQLAlchemy
from sqlalchemy.orm import Session
# Importa a função get_db para obter a conexão com o banco de dados
from ..database import get_db
# Importa o modelo Borrow do banco de dados para representar empréstimos
from ..database.models import Borrow as BorrowModel
# Importa o serviço relacionado aos empréstimos de livros
from ..services import borrow_service
# Importa o schema Borrow do módulo de modelos (esquema de dados para validação)
from ..models.borrow import Borrow as BorrowSchema

# Cria uma instância de roteador para gerenciar endpoints relacionados ao caixa (cashier)
router = APIRouter(
    # Define o prefixo para as rotas relacionadas ao caixa
    prefix="/cashier",
    # Define a tag "cashier" para a documentação da API
    tags=["cashier"],
    # Define uma resposta padrão para o erro 404 (Não encontrado)
    responses={404: {"description": "Not found"}},
)


# Define o endpoint POST para realizar um empréstimo de livro
@router.post("/borrow", response_model=BorrowSchema)
def lend_book(borrow: BorrowSchema, db: Session = Depends(get_db)):
    # Tenta realizar o empréstimo de um livro chamando o serviço correspondente
    try:
        # Chama o serviço borrow_book passando o banco de dados e os dados do empréstimo
        return borrow_service.borrow_book(db, **borrow.dict())
    # Captura qualquer erro de valor e lança uma exceção HTTP 500
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define o endpoint DELETE para realizar a devolução de um livro
@router.delete("/return/{borrow_id}")
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    # Tenta processar a devolução de um livro pelo ID do empréstimo
    try:
        # Chama o serviço return_book passando o banco de dados e o ID do empréstimo
        return borrow_service.return_book(db, borrow_id)
    # Captura qualquer erro de valor e lança uma exceção HTTP 500
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
