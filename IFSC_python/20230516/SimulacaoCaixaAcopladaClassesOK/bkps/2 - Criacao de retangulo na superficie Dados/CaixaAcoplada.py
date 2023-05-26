#coding: utf-8
import ComportaVedacao as CV
import ValvulaAlimentacao as VA
import AlavancaAcionamento as AA
import time #Funções de manipulacao de tempo.

class CaixaAcoplada(): 
	def __init__(self):
		print("Caixa acoplada criada")
		#Atributos-variaveis da caixa 
		self._nivel_maximo = 6.0	#volume em litros 
		self._nivel_agua = 0
		self._nivel_minimo = 0.1
		
		#Atributos-objeto da caixa
		self._comporta = CV.ComportaVedacao()
		self._valvula = VA.ValvulaAlimentacao()	
		self._alavanca = AA.AlavancaAcionamento()	
		
		#Metodos da caixa
		#self._encher()
	
	def _descarga(self): 
		print("\tDescarga pressionada.")
		self._alavanca._set_status("Aberto")
		print("Status = ", self._alavanca._get_status())
		self._comporta._abrirComporta()
		while(self._nivel_agua>self._nivel_minimo): 
			print("Nivel da água: {:.2f}".format(self._nivel_agua))
			self._nivel_agua-=self._comporta._vazao_saida
			time.sleep(1/self._comporta._vazao_saida)
		if (self._nivel_agua<self._nivel_minimo):
			self._nivel_agua=self._nivel_minimo
		print("Nivel da água: {:.2f}".format(self._nivel_agua))
		self._encher()
		self._alavanca._incrementa_contador()
		
			
		
	
	def _encher(self):
		print("Rotina para encher vaso")
		self._comporta._fecharComporta()
		self._valvula._abrirValvula()
		'''
		print("Status") 
		print(self._comporta._get_status())
		print(self._valvula._get_status())
		'''		
		while(self._nivel_agua<self._nivel_maximo):	
			print("\tNivel de água: {:.2f}".format(self._nivel_agua))		
			self._nivel_agua+=self._valvula._get_vazao_entrada()
			#time.sleep(0.3)
			time.sleep(1/self._valvula._vazao_entrada)
		if (self._nivel_agua>self._nivel_maximo): 
			self._valvula._fecharValvula()
			self._nivel_agua= self._nivel_maximo	
		print("\tNivel de água: {:.2f}".format(self._nivel_agua))			
			 
			

