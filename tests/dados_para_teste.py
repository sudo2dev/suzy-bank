from core.bank import *
from datetime import datetime
from collections import namedtuple

def novo_usuario(shoud_print=False):
    User = namedtuple('User',['nome','cpf', 'data_nascimento', 'endereco'])
    user1 = User("maria",'125',datetime(2000,2,2),"Rua c")
    if shoud_print: print(user1)
    return user1

def depositos():
    Deposito = namedtuple('Deposito',['cpf_cliente','no_conta', 'data', 'valor'])
    
    deposito1 = Deposito("123",'1',datetime(2010,1,1),110)
    deposito2 = Deposito("123",'1',datetime(2010,1,2),100)
    deposito3 = Deposito("123",'1',datetime(2010,2,1),150)
    deposito4 = Deposito("123",'1',datetime(2010,2,1),100)
    deposito5 = Deposito("123",'1',datetime(2010,2,2),150)
    deposito6 = Deposito("123",'2',datetime(2010,3,3),150)
    
    return [deposito1, deposito2, deposito3, deposito4, deposito5, deposito6]

def saques():
    Saque = namedtuple('saque',['cpf_cliente','no_conta', 'data', 'valor'])
    saque1 = Saque("123",'1',datetime(2010,1,1),100)
    saque2 = Saque("123",'1',datetime(2010,1,2),100)
    saque3 = Saque("123",'1',datetime(2010,2,3),10)
    saque4 = Saque("123",'1',datetime(2010,2,3),10)
    saque5 = Saque("123",'1',datetime(2010,2,3),10)
    saque5 = Saque("123",'1',datetime(2010,2,3),10)
    saque6 = Saque("123",'2',datetime(2010,4,3),20)
    
    return [saque1, saque2, saque3, saque4, saque5, saque6]

def novo_banco(shoud_print = False):
    User = namedtuple('user1',['nome','cpf', 'data_nascimento', 'endereco'])
    user1 = User("joao",'123',datetime(2000,1,1),"Rua a")
    user2 = User("jose",'124',datetime(2001,1,1),"Rua b")
    bank1 = Bank()
    bank1.novo_cliente(nome=user1.nome, cpf=user1.cpf, nascimento=user1.data_nascimento, endereco=user1.endereco)
    bank1.novo_cliente(nome=user2.nome, cpf=user2.cpf, nascimento=user2.data_nascimento, endereco=user2.endereco)
    
    bank1.nova_conta(user1.cpf)
    bank1.nova_conta(user1.cpf)
    bank1.nova_conta(user2.cpf)
    bank1.nova_conta(user2.cpf)
    bank1.nova_conta(user2.cpf)
    if shoud_print: print(bank1.estatisticas())
    return bank1

def registra_transacoes(bank, should_print=False):
    bank1 = bank
    for d in depositos():
        if should_print: 
            print(*d)
        bank1.depositar(*d)
    for s in saques():
        try:
            if should_print: 
                print(*s)
            bank1.sacar(*s)
        except Exception as e:
            print(e)
    if should_print:
        print(bank1.estatisticas())
    
    return bank1

def novo_banco_com_transacoes(shoud_print=False):
    bank1 = novo_banco()
    bank1 = registra_transacoes(bank1)
    if shoud_print: print(bank1.estatisticas())
    return bank1
