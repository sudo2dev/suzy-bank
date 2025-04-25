from core.bank import *
from datetime import datetime
from collections import namedtuple
from .dados_para_teste import *
from .meu_assert import *

def test_nova_conta():
    user1 = novo_usuario()
    bank1 = Bank()
    bank1.novo_cliente(nome=user1.nome, cpf=user1.cpf, nascimento=user1.data_nascimento, endereco=user1.endereco)
    meu_assert( len(bank1.clientes)==1 )
    bank1.nova_conta(user1.cpf)
    user2 = bank1.pesquisa_cliente(user1.cpf)
    # meu_assert(user2)
    print(user2)

def test_transacao():
    bank1 = novo_banco()
    bank1 = registra_transacoes(bank1, should_print=True)

test_nova_conta()
test_transacao()
