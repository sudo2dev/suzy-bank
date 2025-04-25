from core.pessoa_fisica import PessoaFisica

class Cliente(PessoaFisica):
    
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta);

    def procura_conta(self, no_conta):
        for conta in self.contas:
            if conta.numero == no_conta:
                return conta
        raise Exception("Conta não encontrada")

    def __eq__(self, outro):
        return self.cpf == outro.cpf and self.nome == outro.nome and self.data_nascimento == outro.data_nascimento and \
        self.endereco == outro.endereco and len(self.contas) == len(outro.contas)

    def __str__(self):
        return f'Cliente: [{self.nome}, {self.cpf}, {self.data_nascimento.strftime("%d-%m-%Y")},\
{self.endereco}, tem {len(self.contas)} contas]'