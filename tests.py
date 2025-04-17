import bank
import util
import traceback
from datetime import datetime

def print_origem(origem, e):
    print(f"[🛑 Erro: {e}", end='|')
    print(f"📄 Linha {origem.lineno} no arquivo '{origem.filename}', função '{origem.name}':", end='|')
    print(f"🔧 Código que falhou: {origem.line}]", end="")

def meu_assertx(afirmacao, mensagem=""):
    try:
        assert afirmacao, mensagem
        print('.', end="")
    except AssertionError as e:
        tb = traceback.extract_tb(e.__traceback__)
        tb = traceback.extract_stack()[-2]

        # Se a stack trace tiver mais de 1 frame, tente pegar a origem correta
        if len(tb) > 1:
            # Pega o frame mais próximo de 'meu_assert' que não seja ele mesmo
            origem = next((frame for frame in reversed(tb) if frame.name != "meu_assert"), tb[0])
        else:
            origem = tb[0]  # No caso de erro direto em 'meu_assert', usa o próprio frame

        print_origem(origem, e)

        # raise  # Opcional: relança a exceção para interromper a execução

def meu_assert2(afirmacao, mensagem="",profundidade=-1):
    assert afirmacao, mensagem
    
    try:
        assert afirmacao, mensagem
        print('.',end="")
    except AssertionError as e:
        print('x',end="")

def meu_assert(condicao, mensagem=None):
    if condicao:
        print('.', end='')
    else:
        # Pega a última chamada antes de `meu_assert`
        tb = traceback.extract_stack()[-2]
        erro = f'File "{tb.filename}", line {tb.lineno}, in {tb.name} >> {tb.line} >> AssertionError: {mensagem}'
        print(erro, end="")

def test_date(value,expected):
    date = util.new_date(value) 
    expected = expected
    meu_assert (util.mesma_data(date, expected))

def test_mesma_data():
    d1 = datetime.now()
    d2 = datetime(2025,4,17)
    d3 = datetime(2025,5,17)
    d4 = datetime(2024,5,17)
    d5 = datetime(2025,4,17)

    meu_assert (util.mesma_data(d1, d1))
    meu_assert (util.mesma_data(d1, d2))
    meu_assert (not(util.mesma_data(d1, d3)))
    meu_assert (not(util.mesma_data(d1, d4)))
    meu_assert (not(util.mesma_data(d3, d2)))
    meu_assert (not(util.mesma_data(d2, d4)))
    meu_assert (not(util.mesma_data(d3, d4)))
    meu_assert ((util.mesma_data(d1, d5)))
    meu_assert ((util.mesma_data(d2, d5)))
    meu_assert (not(util.mesma_data(d3, d5)))
    meu_assert (not(util.mesma_data(d4, d5)))
    meu_assert ((util.mesma_data(d5, d5)))

def test_deposito():
    d = datetime.now()
    transacoes = [(d,100, 100)]
    result = bank.depositar(d,100,[])
    meu_assert (result == transacoes)
    try:
        bank.depositar(d,-100,[])
    except Exception as e:
        meu_assert (str(e) == "[ERRO] valor invalido para deposito")

def test_saque():
    d = datetime(2000,10,10)
    transacoes = [(d,100, 100)]
    result = bank.sacar(d,100,transacoes)
    expected1 = (d,-100,0)
    meu_assert (result[-1] == expected1)
    try:
        bank.sacar(d,-100,[])
    except Exception as e:
        mesg = str(e)
        mensagens = ['[ERRO] valor invalido: negativo', "[ERRO] valor > 500" , "[ERRO] Saldo Insuficiente", "[ERRO] ultrapassou limite de saques 3"]
        meu_assert (mesg in mensagens)

def test_saldo():
    d = datetime(2000,10,10)
    transacoes = [(d,100, 100)]
    meu_assert (bank.saldo(transacoes) == 100)
    transacoes = [(d,100, 100),(d,-10,90)]
    meu_assert (bank.saldo(transacoes) == 90)
    transacoes = []
    meu_assert (bank.saldo(transacoes) == 0)
    
def test_conta_saques():
    # Data de referência para o teste
    data_referencia = datetime(2025, 4, 16, 10)

    # Transações simuladas
    transacoes = [
        (datetime(2025, 4, 17, 10, 0), 100, 100),  # mesma data
        (datetime(2025, 4, 17, 15, 30), 200, 300),  # mesma data
        (datetime(2025, 4, 16, 9, 0), -10, 290),      # data diferente
        (datetime(2025, 4, 16, 9, 0), -10, 280),      # data diferente
        (datetime(2025, 4, 16, 9, 0), -10, 270),      # data diferente
        (datetime(2025, 4, 16, 9, 0), -20, 250),      # data diferente
        (datetime(2025, 4, 18, 11, 0), 50, 300)     # data diferente
    ]

    meu_assert(bank.concilia_saldo(transacoes) == transacoes[-1][2])
    meu_assert(bank.conta_transacoes(data_referencia, transacoes) == 4)
    # Esperado: 2 transações na data 16/04/2025
    resultado = bank.conta_saques(data_referencia, transacoes)
    meu_assert (resultado == 4, f"Esperado 2 saques, mas obteve {resultado}")

    # Teste com nenhuma transação na data
    data_sem_transacoes = datetime(2025, 4, 17)
    resultado = bank.conta_saques(data_sem_transacoes, transacoes)
    meu_assert (resultado == 0, f"Esperado 0 saques, mas obteve {resultado}")

    # Teste com todas transações na mesma data
    todas_mesma_data = [
        (datetime(2025, 4, 17, 8, 0), 100, 100),
        (datetime(2025, 4, 17, 9, 0), 200, 300),
        (datetime(2025, 4, 17, 10, 0), 150, 450)
    ]
    resultado = bank.conta_saques(data_referencia, todas_mesma_data)
    meu_assert (resultado == 0, f"Esperado 3 saques, mas obteve {resultado}")

def test_novo_usuario():
    usuarios = {}
    nome = "Joao"
    cpf  = '123'
    data_nascimento = datetime(2000,1,1)
    endere = "Rua a"
    bank.novo_usuario(usuarios, nome=nome, cpf=cpf, nascimento=data_nascimento, endereco=endere)
    meu_assert(len(usuarios)==1)

def test_nova_conta():
    nome = "Joao"
    cpf  = '123'
    data_nascimento = datetime(2000,1,1)
    endere = "Rua a"

    usuarios = {'123':{'nome':'joao'}}
    contas   = {}
    
    try:
        bank.nova_conta(usuarios, contas, agencia='0001', cpf_usuario= '122')
    except Exception as e:
        pass
    bank.nova_conta(usuarios, contas, agencia='0001', cpf_usuario= '123')
    bank.nova_conta(usuarios, contas, agencia='0001', cpf_usuario= '123')
    meu_assert(len(contas) == 2)

def test_pesquisa_conta():
    contas = {}
    contas[1] = {'numero': 1, 'agencia': '0001', 'cpf_usuario':123, 'transacoes':[]}
    contas[2] = {'numero': 2, 'agencia': '0001', 'cpf_usuario':124, 'transacoes':[]}
    contas[3] = {'numero': 3, 'agencia': '0001', 'cpf_usuario':123, 'transacoes':[]}
    meu_assert(bank.pesquisa_conta(contas, 1)   == contas[1])
    meu_assert(bank.pesquisa_conta(contas, '1') == None)
    meu_assert(bank.pesquisa_conta(contas, 3) == contas[3])

test_date('01-01-2000',datetime(2000,1,1))
test_date('0-01-2000',datetime(2025,4,17))
test_mesma_data()
test_saldo()
test_deposito()
test_saque()
test_conta_saques()
test_novo_usuario()
test_nova_conta()
test_pesquisa_conta()