import util;

def procura_cpf(usuarios, cpf):
	return usuarios.get(cpf, None)

def novo_usuario(usuarios, /, nome, nascimento, cpf, endereco):
	cpf_cadastrado = procura_cpf(usuarios, cpf)
	if cpf_cadastrado:
		raise Exception('[ERRO] cpf ja cadastrado')
	usuarios[cpf] = {'nome': nome, 'data_nascimento':nascimento, 'endereco':endereco} # adicionar o numero das contas?
	return usuarios[cpf]

def novo_numero_conta(contas):
	if (len(contas) == 0):
		return 1
	return max(contas.keys()) + 1

def nova_conta(usuarios, contas, /, cpf_usuario, agencia='0001'):
	cpf_cadastrado = procura_cpf(usuarios, cpf_usuario)
	if not cpf_cadastrado:
		raise Exception('[ERRO] cpf não cadastrado')
	no_conta = novo_numero_conta(contas)
	contas[no_conta] = {'numero': no_conta, 'agencia': agencia, 'cpf_usuario':cpf_usuario, 'transacoes':[]} # adicionar o numero das contas?
	return contas[no_conta]

def pesquisa_conta(contas, conta):
	return contas.get(conta, None)

#transacoes - [(data,valor, saldo), ...]

def depositar(data, valor, transacoes):
	if valor <= 0:
		raise ValueError("[ERRO] valor invalido para deposito")
	if conta_transacoes(data, transacoes) >= 10:
		raise Exception("[ERRO] ultrapassou limite de transacoes no dia: 10")
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

def conta_saques(data, transacoes):
	contagem = 0
	for transacao in transacoes:
		if util.mesma_data(transacao[0], data) and transacao[1] < 0:
			contagem += 1
	return contagem

def conta_transacoes(data, transacoes):
	contagem = 0
	for transacao in transacoes:
		if util.mesma_data(transacao[0], data):
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
	if conta_saques(data,transacoes) >= LIMITE_SAQUES:
		raise ValueError(f'[ERRO] ultrapassou limite de saques {LIMITE_SAQUES}')
	if valor <= 0:
		raise ValueError('[ERRO] valor invalido: negativo')
	if valor > VALOR_LIMITE:
		raise ValueError(f'[ERRO] valor > {VALOR_LIMITE}')
	if valor > valor_saldo:
		raise Exception('[ERRO] Saldo Insuficiente')
	novo_saldo = valor_saldo - valor
	transacoes.append((data, -valor, novo_saldo))
	return transacoes
