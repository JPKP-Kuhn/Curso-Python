#coding: utf-8

class ComportaVedacao(): 
	def __init__(self): 
		print("\t Comporta de vedação criada.")
		self._status = "Fechada"
		self._vazao_saida = 5 #litros/segundo
	
	#Metodos
	def _abrirComporta(self): 
		self._status = "Aberta"
			
	def _fecharComporta(self): 
		self._status = "Fechada"
	
	def _get_status(self): 
		return self._status	
		
