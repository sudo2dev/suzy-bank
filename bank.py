import util;

#transacoes - [(data,valor, saldo), ...]

def depositar(data, valor, transacoes):
	if valor <= 0:
		raise ValueError("[ERRO] valor invalido para deposito")
	novo_saldo = saldo(transacoes) + valor
	transacoes.append((data,valor,novo_saldo))
	return transacoes

def concilia_saldo(transacoes):
	saldo = 0
	for transacao in transacoes:
		saldo += transacao[1]
		if saldo != transacao[2]:
			raise Exception("[ERRO] conciliacao saldo!")
	return saldo

def verifica_qtd_saques(data, transacoes):
	contagem = 0
	for transacao in transacoes:
		if util.mesma_data(transacao[0], data) and transacao[1] < 0:
			contagem += 1
	return contagem

def saldo(transacoes):
	saldo_ = 0
	if len(transacoes) > 0:
		saldo_ = transacoes[-1][2]
	return saldo_

def sacar(data, valor, transacoes):
	LIMITE_SAQUES = 3
	VALOR_LIMITE  = 500

	valor_saldo = saldo(transacoes)	
	if verifica_qtd_saques(data,transacoes) >= LIMITE_SAQUES:
		raise Exception(f'[ERRO] ultrapassou limite de saques {LIMITE_SAQUES}')
	if valor <= 0:
		raise Exception('[ERRO] valor invalido: negativo')
	if valor > VALOR_LIMITE:
		raise Exception(f'[ERRO] valor > {VALOR_LIMITE}')
	if valor > valor_saldo:
		raise Exception('[ERRO] Saldo Insuficiente')
	novo_saldo = valor_saldo - valor
	transacoes.append((data, -valor, novo_saldo))
	return transacoes
