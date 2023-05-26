#coding: utf-8

class AlavancaAcionamento(): 
	def __init__(self): 
		self._contador= 0
		self._status = "Fechado"
	
	def _set_status(self, opcao): 
		if(opcao == "Aberto") :
			self._status ="Aberto"
		else: 
			self._status ="Fechado"	
	
	def _incrementa_contador(self): 
		self._contador+=1
	
	def _get_status(self):
		return self._status		
