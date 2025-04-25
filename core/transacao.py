from abc import ABC, abstractmethod

class Transacao(ABC):
    def __init__(self, data, valor):
        self._data  = data
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @property
    def data(self):
        return self._data

    @abstractmethod
    def valor_com_sinal(self):
        pass

    @property
    def nome(self):
        return type(self).__name__[0]

    @abstractmethod
    def registrar(self, conta):
        pass