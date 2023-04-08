#coding: utf-8
import datetime
from random import randint

class contaBancaria():
    def __init__(self):
        self._nome = ''
        self._numero_conta = ''
        self._dataAbertura = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._saldo = 0
        self._extrato = []

    def _set_numero_conta(self):
        numero_conta = str(randint(100000000,999999999))
        numero_conta = numero_conta[:8]+ '-'+ numero_conta[8:]
        self._numero_conta = numero_conta

    def _set_correntista(self, nome, saldo ):
        self._nome = nome
        self._set_numero_conta()
        self._saldo = saldo

    def _get_correntista(self):
        return {
            "Nome": self._nome,
            "Data de abertura": self._dataAbertura,
            "Numero Conta": self._numero_conta
        }


    def deposito(self, valor):
        self._saldo += valor
        self._set_extrato('Depósito', valor)
        return self._saldo

    def retirada(self, valor):
        if valor > self._saldo:
           print('Saldo insuficiente!')
        else: 
            self._saldo -= valor
            self._set_extrato('Retirada', valor)
        
        return self._saldo


    def _get_saldo(self):
        return self._saldo
    
    def _set_extrato(self, tipo, valor):
        self._extrato.append({
            'Tipo': tipo, 
            'Valor': valor,
            'Data': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
    
    def _get_extrato(self):
        return self._extrato

    
class Chequeespecial(contaBancaria):
    pass