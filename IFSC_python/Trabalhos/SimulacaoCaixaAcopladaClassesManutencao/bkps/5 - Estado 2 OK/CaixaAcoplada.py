#coding: utf-8
import ComportaVedacao as CV
import ValvulaAlimentacao as VA
import AlavancaAcionamento as AA
import time #Funções de manipulacao de tempo.
import pygame as pyg

'''
As rotinas da classe CaixaAcoplada não podem ser chamadas a toda hora. 
São métodos e constantes que são modificadas fora do loop principal. 
Basicamente são controles e registros de controle. 
Podem ser usadas para registro de estado.
'''

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
		
		self.Estado = 0	#Estados que a caixa pode estar
							#0 - ociosa (antes de iniciar)
							#1 - Caixa enchendo
							#2 - Caixa cheia de água
							#3 - Caixa esvaziando
							#4 - Caixa vazia para manutenção
							
		
		self.DesativarCaixa = False					

	#Controle Operacional da caixa acoplada. 	
	def CA_ControleOperacional(self):
		if 	(self.Estado == 0): 	#Caixa nao iniciada. 
			self.CA_Estado0()			#Definido em CaixaAcoplada. 				
		elif(self.Estado==1):
			self.CA_Estado1()			
		elif(self.Estado==2):
			 self.CA_Estado2()
		elif(self.Estado==3): 
			self.CA_Estado3()	 
		elif(self.Estado==4): #Esvaziar a caixa e mandar para manutenção.
			self.CA_Estado4()
		 
	
	def CA_Estado0(self): 
		#mouse dentro do quadrado para acionar a caixa muda para maozinha.
		if (400<pyg.mouse.get_pos()[0]<450 and 32<pyg.mouse.get_pos()[1]<75):
			self.MouseFlag=False	#Orienta o mouse a virar mãozinha.								
			if (self.MouseClicked==True):
				self.Estado =1	#A caixa passa para regime de enchimento.
				self.MouseFlag=True
				self.cronometro = True	
				self._Controle_vazao_entrada()	#Inicia contagem de tempo para simulacao
												#do enchimento da caixa 				
			self.SurfDados.blit( self.StartImage, (5,5), self.retImageOnButton )				
		else:
			self.MouseFlag=True
			self.SurfDados.blit( self.StartImageDark, (5,5), self.retImageOnButton )					
		self.MouseClicked = False	#desmarca o clique do mouse.	
	
	def CA_Estado1(self):
		self.SurfDados.blit( self.StartImage, (5,5), self.retImageOnButton )		
		self.SurfCaixa_enchimento()
	

	def CA_Estado2(self):
		self.SurfCaixaLinhaDagua()
		self.SurfDados.blit( self.OkImage, (5,5) )
		self.SurfDados.blit( self.StartImage, (5,70), self.retImageOffButton)

	def CA_Estado3(self):
		self.SurfDados.blit( self.StartImage, (5,5), self.retImageOffButton )

	def CA_Estado4(self):
		self.SurfDados.blit( self.StartImageDark, (5,5), self.retImageOffButton )

	
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
			 
			

