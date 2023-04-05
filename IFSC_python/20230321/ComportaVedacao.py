#coding: utf-8

class ComportaVedacao():
	def __init__(self):
		print("\t Comporta vedação")
		self._status = "Fechada"
		self._vazao_saida = 1.25 #Litros/segundo

	#Metodos
	def _abrirComporta(self):
		self._status = "Aberta"

	def _fecharComporta(self):
		self._status = "Fechada"

	def _get_status(self):
		return self._status
