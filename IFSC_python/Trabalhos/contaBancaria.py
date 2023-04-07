#coding: utf-8
import datetime
import random

class contaBancaria():
    def __init__(self):
        self._nome = ''
        self._numero_conta = ''
        self._dataAbertua = datetime.date.today().ctime()
        self._saldo = -1
        self._extrato = []

    def _set_user(self, nome, numero_conta, dataAbertura, saldo ):
        self._nome = nome
        self._numero_conta = numero_conta
        self._dataAbertura = dataAbertura
        self._saldo = saldo

    def _set_numero_conta(self):
        numero_conta = random

    def _set_deposito(self):
        pass

    def _get_retirada(self):
        pass

    def _get_saldoExtrato(self):
        pass

    def _get_correntista(self):
        pass
