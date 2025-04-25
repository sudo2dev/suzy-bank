from .historico import Historico

class Conta:

    LIMITE_SAQUES = 3
    VALOR_LIMITE  = 500

    def __init__(self, numero, agencia, cliente):
        self.numero = numero
        self.agencia = agencia
        self._saldo  = 0
        self.historico = Historico()
        self.cliente = cliente

    @property
    def saldo(self):
        return self._saldo

    def _registrar(self, transacao):
        self.historico.adicionar_transacao(transacao)
    
    def sacar(self, valor):


        # valor_saldo = saldo(transacoes)	
        # if conta_saques(data,transacoes) >= LIMITE_SAQUES:
        #     raise ValueError(f'[ERRO] ultrapassou limite de saques {LIMITE_SAQUES}')
        if valor <= 0:
            raise ValueError('[ERRO] valor invalido: negativo')
        if valor > self._saldo:
            raise Exception('[ERRO] Saldo Insuficiente')

        self._saldo =  self._saldo - valor
        
        
        return self.saldo
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("[ERRO] valor invalido para deposito")
        # if conta_transacoes(data, transacoes) >= 10:
        #     raise Exception("[ERRO] ultrapassou limite de transacoes no dia: 10")
        # novo_saldo = self.saldo(transacoes) + valor
        # transacoes.append((data,valor,novo_saldo))

        self._saldo =  self._saldo + valor
        return self._saldo

    @staticmethod
    def nova_contax(cliente, numero): #nao utilizado?
        return Conta(numero, cliente)

    def __repr__(self):
        return f'[Conta: {self.numero}, {self.agencia}, {self.saldo}]'