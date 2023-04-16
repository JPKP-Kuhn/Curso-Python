#coding: utf-8
import random as r
import time

class Operacao: #Só pra guardar dados
	_recebimento = -1
	_retirada = -1
	_data = ''

class Correntista():
	def __init__(self, nome, data, saldo=100):
		self._nome = nome
		self._data = data
		self._saldo = saldo
		self._conta = 0
		self._extrato = []
		self._operacoes = []
		self._set_Numero_conta()

	#Funções setters
	def _set_Numero_conta(self)	:
		#Gera numero entre 1 e 2000
		self._conta = r.randint(1, 2000)

	def _set_Deposito(self, recebimento, data):
		A = Operacao()
		A._recebimneto = recebimento
		A._data = data
		self._saldo+=A._recebimento
		self._operacoes.append(A)

	def _set_Retirada(self, retirada, data):
		A = Operacao()
		A._retirada = retirada
		self._saldo -=A._retirada
		A.data = data
		self._operacoes.append[A]

	#Funções getters:
	def _get_Operacoes(self):
		for i in range(len(self._operacoes)):
			if (self._operacoes[i].recebimento != -1):
				print("Depósito de: ", self._operacoes[i]._recebimento)
			else:
				print("Retirada de: ", self._operacoes[i]._retirada)
				print("\tem", self._operacoes[i]._data)
				print("Saldo: ", self._saldo)

	def _get_dados_correntistas(self):
		print("Dados do correntista", self._nome)
		print("\tConta: ", self._conta)
		print("\tSaldo: ", self._saldo)

		return self._data
