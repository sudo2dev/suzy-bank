from core.bank import *
from datetime import datetime
from .meu_assert import *

def test_novo_usuario():
    nome = "Joao"
    cpf  = '123'
    data_nascimento = datetime(2000,1,1)
    endere = "Rua a"
    bank1 = Bank();
    user1 = Cliente(cpf, nome, data_nascimento, endere) #//cpf, nome, data_nascimento, endereco):
    #//def novo_usuario(self, /, nome, nascimento, cpf, endereco):
    bank1.novo_cliente(nome=nome, cpf=cpf, nascimento=data_nascimento, endereco=endere)
    user2 = bank1.pesquisa_cliente(cpf)
    meu_assert( len(bank1.clientes)==1 )
    print(user1, user2)
    assert(user1 == user2)

test_novo_usuario()