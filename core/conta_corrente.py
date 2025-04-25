class ContaCorrete(Conta):
    def __init__(self, numero, agencia ):
        super(numero, agencia)

    def sacar(self, valor):
        if valor > VALOR_LIMITE:
            raise ValueError(f'[ERRO] valor > {VALOR_LIMITE}')
        
        self.sacar(valor)