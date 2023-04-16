#coding: utf-8
import ClasseCorrentista as CC

class CorrentistaCartaoCredito(CC.Correntista):
	def __init__(self):
		CC.Correntista.__init__(self)
		self._limite = 0
		self._OpInterncaional = False

class CorrentistaEspecial(CC.Correntista):
	def __init__(self):
	CC.Correntista.__init__(self)
	self._limite_cheque = 0
	self._renda = 0
	self._juros_cheques = 0
	self._saldo_medio = 0
