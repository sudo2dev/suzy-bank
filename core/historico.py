from util.util import mesma_data
class Historico:

    def __init__(self):
        self.historico = []

    def adicionar_transacao(self, transacao):
        self.historico.append(transacao)

    def conta_transacoes(self, data):
        total = 0
        for transacao in self.historico:
            if mesma_data(data, transacao.data):
                total += 1
        return total

    def conta_transacoes(self, tipo):
        total = 0
        for transacao in self.historico:
            if tipo == transacao.__name__:
                total += 1
        return total

    def transacoes(self):
        return self.historico

    