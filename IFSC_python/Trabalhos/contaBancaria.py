#coding: utf-8
import datetime
from random import randint

class contaBancaria():
    def __init__(self):
        self._nome = ''
        self._numero_conta = ''
        self._dataAbertura = datetime.date.today().ctime()
        self._saldo = 0
        self._extrato = []

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
    
    def _get_saldo(self):
        return self._saldo

    def _set_numero_conta(self):
        numero_conta = str(randint(100000000,999999999))
        numero_conta = numero_conta[:8]+ '-'+ numero_conta[8:]
        self._numero_conta = numero_conta

    def _set_deposito(self):
        pass

    def _get_retirada(self):
        pass

    def _get_saldoExtrato(self):
        pass
