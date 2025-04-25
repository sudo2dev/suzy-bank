from .cliente import Cliente
from .conta import Conta
from .deposito import Deposito
from .saque import Saque

class Bank:

    def __init__(self):
        self.clientes = {}
        self.qtd_contas = 0

    def novo_cliente(self, /, nome, nascimento, cpf, endereco):
        novo_cliente = Cliente(cpf, nome, nascimento, endereco)
        try:
            cliente = self.pesquisa_cliente(cpf)
            raise Exception('[ERRO] cpf ja cadastrado')
        except:
            pass           
        self.clientes[cpf] = novo_cliente # adicionar o numero das contas?
        return self.clientes[cpf]

    def novo_numero_conta(self):
        return f'{(self.qtd_contas + 1)}';

    def nova_conta(self, /, cpf_usuario, agencia='0001'):
        cliente = self.pesquisa_cliente(cpf_usuario)
        if not cliente:
            raise Exception('[ERRO] cpf não cadastrado')
        no_conta = self.novo_numero_conta()
        nova_conta = Conta(no_conta, agencia, cliente)
        cliente.adicionar_conta(nova_conta)
        self.qtd_contas += 1
        return nova_conta

    def pesquisa_cliente(self, cpf_cliente):
        cliente = self.clientes.get(cpf_cliente, None)
        if not cliente:
            raise Exception("Conta não encontrada")
        return cliente

    def extrato(self, no_conta):
        conta = self.pesquisa_conta(no_conta)
        return conta.historico.transacoes()

    def pesquisa_conta(self, no_conta, cpf_cliente = None,):
        if cpf_cliente:
            cliente = self.pesquisa_cliente(cpf_cliente)
            conta = cliente.procura_conta(no_conta)
            return conta
        else:
            for cliente in self.clientes.values():
                try:
                    # print(cliente)
                    conta = cliente.procura_conta(no_conta)
                    return conta
                except:
                    pass
        raise Exception("Conta não encontrada")

    def depositar(self, cpf_cliente, no_conta, data, valor):
        cliente  = self.pesquisa_cliente(cpf_cliente)
        conta    = cliente.procura_conta(no_conta)
        deposito = Deposito(data, valor)
        cliente.realizar_transacao(conta, deposito)
        return conta.saldo

    def sacar(self, cpf_cliente, no_conta, data, valor):
        cliente  = self.pesquisa_cliente(cpf_cliente)
        conta    = cliente.procura_conta(no_conta)
        saque = Saque(data, valor)
        cliente.realizar_transacao(conta, saque)
        return conta.saldo

    def saldo(self, no_conta, cpf_cliente=None):
        conta  = self.pesquisa_conta(no_conta, cpf_cliente)
        return conta.saldo

    def estatisticas(self):
        result = "=====================================\n"

        for cliente in self.clientes.values():
            result += f"\n{cliente}\n"
            for conta in cliente.contas:
                result += f'\t{conta}\n'
        result += "\n"
        result += f"total de clientes: {len(self.clientes)}\n"
        result += f"total de contas: {self.qtd_contas}"
        result += "\n\n================================="
        return result

# def concilia_saldo(transacoes):
#     saldo = 0
#     for transacao in transacoes:
#         saldo += transacao[1]
#         if saldo != transacao[2]:
#             raise Exception("[ERRO] conciliacao saldo!")
#     return saldo

# def conta_saques(data, transacoes):
#     contagem = 0
#     for transacao in transacoes:
#         if util.mesma_data(transacao[0], data) and transacao[1] < 0:
#             contagem += 1
#     return contagem

# def conta_transacoes(data, transacoes):
#     contagem = 0
#     for transacao in transacoes:
#         if util.mesma_data(transacao[0], data):
#             contagem += 1
#     return contagem
