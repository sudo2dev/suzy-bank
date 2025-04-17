import bank 
import util 
from datetime import datetime

def le_data():
	data = input('digite a data ou <ENTER> para hj (dd-mm-aaaa)')
	return util.new_date(data)

def depositar(transacoes):
	try:
		data = le_data()
		valor = float(input('digite o valor do deposito: '))
		bank.depositar(data, valor, transacoes)
	except Exception as e:
		print(e)
	finally:
		saldo(transacoes)
		return transacoes

def sacar(transacoes):
	try:
		data = le_data()
		valor = float(input('digite o valor do saque: '))
		transacoes = bank.sacar(data,valor,transacoes)
	except Exception as e:
		print(e)
	finally:
		saldo(transacoes)
		return transacoes

def saldo(transacoes):
	saldo = bank.saldo(transacoes)
	print(f'Saldo: {saldo}')

def extrato(transacoes):
	if len(transacoes) == 0:
		print("Conta sem movimentação")
		return
	print(f'data\toperacao\tvalor\tsaldo')
	for t in transacoes:
		data = t[0].strftime('%d-%m-%Y')
		valor = t[1]
		opera = 'C' if valor > 0 else 'D'
		saldo = t[2]
		print(f'{data}\t{opera}\t{valor}\t{saldo}')

def sair():
	print('bye.')

def main():
	mensagem = (
		'[d] depositar\n'
		'[s] sacar\n'
		'[e] extrato\n'
		'[b] saldo\n'
		'[q] sair\n'
	)

	transacoes = [] #(data, valor, saldo)
	opcao = None
	while opcao != 'q':
		opcao = input(mensagem)
		print('===============\n')
		match opcao:
			case 'd' : depositar(transacoes)
			case 's' : sacar(transacoes)
			case 'e' : extrato(transacoes)
			case 'b' : saldo(transacoes)
			case 'q' : sair()
			case _   : print('opcao inválida')
		print('===============\n')

if __name__ == "__main__":
	main()