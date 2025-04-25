from core.bank import Bank 
from util import util 
from tests.dados_para_teste import novo_banco_com_transacoes
from datetime import datetime

def le_data(mensagem = 'digite a data ou <ENTER> para hj (dd-mm-aaaa)'):
	data = input(mensagem)
	return util.new_date(data)

def informa_cliente(bank):
	cpf_cliente = input('Informe cpf do cliente: ')
	cliente = bank.pesquisa_cliente(cpf_cliente)
	if not cliente:
		raise Exception('[ERRO] cliente nao cadastrado')
	return cpf_cliente

def informa_conta(bank, cpf_cliente=None):
	no_conta = input('Informe no conta: ')
	conta = bank.pesquisa_conta(no_conta, cpf_cliente)
	if not conta:
		raise Exception('[ERRO] conta invalida')
	return no_conta 

def depositar(bank):
	# cliente, conta, data, valor
	try:
		cpf = informa_cliente(bank)
		no_conta = informa_conta(bank, cpf)
		data = le_data()
		valor = float ( input('digite o valor do deposito: ') or 0 )
		saldo = bank.depositar(cpf, no_conta, data, valor)
		print(saldo)
	except Exception as e:
		print(e)
	finally:
		# saldo(transacoes=transacoes)
		pass

def sacar(bank):
	try:
		cpf = informa_cliente(bank)
		no_conta = informa_conta(bank, cpf)
		data = le_data()
		valor = float(input('digite o valor do saque: '))
		saldo = bank.sacar(cpf, no_conta, data, valor)
		print(saldo)
	except Exception as e:
		print(e)
	finally:
		pass

def saldo(bank):
	try:
		no_conta = informa_conta(bank)
		saldo = bank.saldo(no_conta)
		print(f'Saldo: R$ {saldo:.2f}')
	except Exception as e:
		print(e)

def extrato(bank):
	try:
		conta = informa_conta(bank)
		transacoes = bank.extrato(conta)

		if len(transacoes) == 0:
			print("Conta sem movimentação")
			return
		print(f'data - hora\t\toperacao\tvalor\t\tsaldo')
		saldo = 0
		for t in transacoes:
			data = t.data.strftime('%d-%m-%Y %H:%M')
			valor = t.valor
			opera = t.nome
			saldo += t.valor_com_sinal
			print(f'{data}\t{opera}\t\tR$ {valor:11.2f}\tR$ {saldo:11.2f}')
	except Exception as e:
		print(e)

def sair():
	print('bye.')

def novo_usuario(bank):
	try:
		print('*Novo Usuário*')
		nome = input('Digite o nome: ')
		data = le_data('Data de nascimento: ')
		cpf  = input('Digite o cpf: ')
		end  = input('Digite o endereco: ')
		usr  = bank.novo_cliente(nome=nome, nascimento=data, cpf=cpf, endereco=end)
		print(usr)
	except Exception as e:
		print(e)

def nova_conta(bank):
	cta = None
	try:
		print('*Nova Conta*')
		cpf  = input('Digite o cpf do titular da conta: ')
		cta  = bank.nova_conta(cpf_usuario=cpf)
		print(cta)
	except Exception as e:
		print(e)

def listar_usuarios(bank):
	print('* Usuários *')
	for c in bank.clientes:
		print(c,bank.clientes[c])

def listar_contas(bank):
	print('* Contas *')
	for cliente in bank.clientes.values():
		print(cliente)
		for conta in cliente.contas:
			print('\t',conta)

def carrega_dados(bank):
	return novo_banco_com_transacoes()

def main():
	carrega_dados_simulados = False
	mensagem = (
		'[d] depositar\n'
		'[s] sacar\n'
		'[e] extrato\n'
		'[b] saldo\n'
		'[nu] novo usuario\n'
		'[nc] nova conta\n'
		'[lu] listar usuarios\n'
		'[lc] listar contas\n'
		'[q] sair\n'
	)
	bank1 = Bank()
	if (carrega_dados_simulados):
		bank1 = carrega_dados(bank1)
	opcao = None
	while opcao != 'q':
		opcao = input(mensagem)
		print('===============\n')
		match opcao:
			case 'nu' : novo_usuario(bank1)
			case 'nc' : nova_conta(bank1)
			case 'lu' : listar_usuarios(bank1)
			case 'lc' : listar_contas(bank1)
			case 'd' : depositar(bank1)
			case 's' : sacar(bank1)
			case 'e' : extrato(bank1)
			case 'b' : saldo(bank1)
			case 'q' : sair()
			case _   : print('opcao inválida')
		print('===============\n')

if __name__ == "__main__":
	main()