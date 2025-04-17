import bank 
import util 
from datetime import datetime

def le_data(mensagem = 'digite a data ou <ENTER> para hj (dd-mm-aaaa)'):
	data = input(mensagem)
	return util.new_date(data)

def informa_conta(contas):
	no_conta = int(input('Informe no conta: '))
	conta = bank.pesquisa_conta(contas, no_conta)
	if not conta:
		raise Exception('[ERRO] conta invalida')
	return conta 

def depositar(contas):
	transacoes = None
	try:
		conta = informa_conta(contas)
		transacoes = conta['transacoes']
		data = le_data()
		valor = float(input('digite o valor do deposito: '))
		bank.depositar(data, valor, transacoes)
	except Exception as e:
		print(e)
	finally:
		saldo(transacoes=transacoes)
		# return transacoes

def sacar(contas):
	transacoes = None
	try:
		conta = informa_conta(contas)
		transacoes = conta['transacoes']
		data = le_data()
		valor = float(input('digite o valor do saque: '))
		transacoes = bank.sacar(data,valor,transacoes)
	except Exception as e:
		print(e)
	finally:
		saldo(transacoes=transacoes)

def saldo(contas=None, transacoes=None):
	try:
		if not transacoes:
			conta = informa_conta(contas)
			transacoes = conta['transacoes']
		saldo = bank.saldo(transacoes)
		print(f'Saldo: R$ {saldo:.2f}')
	except Exception as e:
		print(e)

def extrato(contas):

	try:
		conta = informa_conta(contas)
		transacoes = conta['transacoes']
		if len(transacoes) == 0:
			print("Conta sem movimentação")
			return
		print(f'data - hora\t\toperacao\tvalor\t\tsaldo')
		for t in transacoes:
			data = t[0].strftime('%d-%m-%Y %H:%M')
			valor = t[1]
			opera = 'C' if valor > 0 else 'D'
			saldo = t[2]
			print(f'{data}\t{opera}\t\tR$ {valor:11.2f}\tR$ {saldo:11.2f}')
	except Exception as e:
		print(e)

def sair():
	print('bye.')

def novo_usuario(usuarios):
	try:
		print('*Novo Usuário*')
		nome = input('Digite o nome: ')
		data = le_data('Data de nascimento: ')
		cpf  = input('Digite o cpf: ')
		end  = input('Digite o endereco: ')
		usr  = bank.novo_usuario(usuarios, nome=nome, nascimento=data, cpf=cpf, endereco=end)
		print(usr)
	except Exception as e:
		print(e)
	return usuarios

def nova_conta(usuarios, contas):
	cta = None
	try:
		print('*Nova Conta*')
		cpf  = input('Digite o cpf do titular da conta: ')
		cta  = bank.nova_conta(usuarios, contas, cpf_usuario=cpf)
		print(cta)
	except Exception as e:
		print(e)

def listar_usuarios(usuarios):
	print('* Usuários *')
	for c in usuarios:
		print(c,usuarios[c])

def listar_contas(contas):
	print('* Contas *')
	for c in contas:
		print(c,contas[c])

def carrega_dados(usuarios, contas):
	usuarios['123'] = {'nome':"Joao", 'data_nascimento':datetime.today(), 'endereco':""}
	usuarios['124'] = {'nome':"Joao", 'data_nascimento':datetime.now()  , 'endereco':""}
	contas[1] = {'agencia': '0001', 'cpf_usuario':123, 'transacoes':[]}
	contas[2] = {'agencia': '0001', 'cpf_usuario':124, 'transacoes':[]}
	contas[3] = {'agencia': '0001', 'cpf_usuario':123, 'transacoes':[]}

def main(carrega_dados_simulados = False):
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
	usuarios = {}
	contas = {}
	if (carrega_dados_simulados):
		carrega_dados(usuarios, contas)
	opcao = None
	while opcao != 'q':
		opcao = input(mensagem)
		print('===============\n')
		match opcao:
			case 'nu' : novo_usuario(usuarios)
			case 'nc' : nova_conta(usuarios, contas)
			case 'lu' : listar_usuarios(usuarios)
			case 'lc' : listar_contas(contas)
			case 'd' : depositar(contas)
			case 's' : sacar(contas)
			case 'e' : extrato(contas)
			case 'b' : saldo(contas)
			case 'q' : sair()
			case _   : print('opcao inválida')
		print('===============\n')

if __name__ == "__main__":
	main(True)