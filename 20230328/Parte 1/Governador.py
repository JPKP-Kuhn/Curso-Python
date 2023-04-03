#coding: utf-8

import Politicos as P

class Governador(P.Politico):
	def __init__(self, nome, partido, estado):
		P.Politico.__init__(self)
		self._estado = ''
		self._cargo = "Governador"
		self._set_nome(nome)
		self._set_partido(partido)
		self._set_estado(estado)

	def _set_estado(self, estado):
		self._estado = estado

	def _apresentacao(self):
		P.Politico._apresentacao(self)
		print("Meu estado é: ", self._estado)
#Governador no main