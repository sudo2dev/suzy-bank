from .transacao import Transacao

class Deposito(Transacao):

    def __init__(self, data, valor):
        super().__init__(data, valor)

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta._registrar(self) #transformar em uma unica transacao
    
    @property
    def valor_com_sinal(self):
        return self.valor

