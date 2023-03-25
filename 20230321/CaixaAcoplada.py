#coding: utf-8
import ComportaVedacao as CV
import ValvulaAlimentacao as VA
import AlavancaAcionamento as AA
import time #Funções de manipulação de tempo

class CaixaAcoplada(): 
	def __init__(self): #função construtuora, colocarei funções nessa classe
		print("Caixa acoplada criada")
		#Atributos-variáveis da caixa
		self._nivel_maximo = 6.0 #volume em litros
		self._nivel_agua = 0
		self._nivel_minimo = 0.1

		#Atributos-objetos da caixa
		self._comporta = CV.ComportaVedacao()
		self._valvula = VA.ValvulaAlimnetacao()
		self._alavanca = AA.AlavancaAcionamento()


	def _descarga(self):
		#pass
		print("\tDescarga pressionada.")
		self._alavanca._set_status("Aberto")
		print("Status = ", self._alavanca._get_status())
		self._comporta._abrirComporta()
		while(self._nivel_agua>self._nivel_minimo):
			print("Nivel da água: {:.2f}".format(self._nivel_agua))
			self._nivel_agua -= self._comporta._vazao_saida
			time.sleep(0.4)
		if(self._nivel_agua<self._nivel_minimo):
			self._nivel_agua=self._nivel_minimo
		print("Nivel da água: {:.2f}".format(self._nivel_agua))
		self._encher()
		self._alavanca._incremento_contador()

	def _encher(self):
		print("Encher")
		self._comporta._fecharComporta()
		self._valvula._abrirValvula()
		'''
		print(self._comporta._get_status())
		print(self._valvula._get_status())
		#print(self._comporta._get_status())
		'''
		while(self._nivel_agua<self._nivel_maximo):
			print("\tNível de água: {:.2f}".format(self._nivel_agua))
			self._nivel_agua += self._valvula._get_vazao_entrada()
			time.sleep(1/self._valvula._vazao_entrada)
		if (self._nivel_agua>self._nivel_maximo):
			self._valvula._fecharValvula()
			self._nivel_agua = self._nivel_maximo
			print("\tNível de água: {:.2f}".format(self._nivel_agua))



