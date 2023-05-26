#coding: utf-8
import ComportaVedacao as CV
import ValvulaAlimentacao as VA
import AlavancaAcionamento as AA
#import pygame as pyg

'''
Caixa Acoplada altera condições das duas superficies definidas na simulação.
Guarda as variáveis estáticas e dinâmicas da caixa. 
'''

class CaixaAcoplada(): 
	def __init__(self):
		print("Caixa acoplada criada")
		#Atributos-variaveis da caixa 
		self._nivel_maximo = 6.0	#volume em litros 		
		self._nivel_minimo = 0.1
		self.VolumeCaixa = 0		#Controle de volume
		
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
	
	#Controle Operacional da caixa acoplada. 	
	def CA_ControleOperacional(self):
		if 	(self.Estado == 0): 	#Caixa nao iniciada. 
			self.CA_Estado0()		#Definido em CaixaAcoplada. 				
		elif(self.Estado==1):
			self._valvula._status = "Aberta"
			self._comporta._status = "Fechada"
			self.CA_Estado1()			
		elif(self.Estado==2):
			self._valvula._status = "Fechada"
			self._comporta._status = "Fechada"
			self.CA_Estado2()
		elif(self.Estado==3): 
			self._comporta._status = "Aberta"
			self._valvula._status = "Fechada"
			self.CA_Estado3()				
		elif(self.Estado==4): 		#Esvaziar a caixa e mandar para manutenção.
			self._comporta._status = "Aberta"
			self._valvula._status = "Fechada"
			self.CA_Estado4()
	
	def CA_Estado0(self): 		
		if (self.flagB1a):
				#mouse dentro do quadrado para acionar a caixa muda para maozinha.
			self.MouseFlag=False	#Orienta o mouse a virar mãozinha.								
			if (self.MouseClicked==True):
				self.Estado =1	#A caixa passa para regime de enchimento.
				self.MouseFlag=True
				self.cronometro = True	
				self._Controle_vazao_entrada()	#Inicia contagem de tempo para simulacao do enchimento da caixa 				
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
		self._valvula._status = "Fechada"		
		if(self.flagB1b):	#Localiza vizinhança do botao da valvula			
			self.MouseFlag=False	#Troca a figura do mouse para mãozinha
			if (self.MouseClicked==True):
				self.Estado =3	#A caixa passa para regime de esvaziamento
				self.MouseFlag=True
				self._Controle_vazao_saida()	#Inicia contagem de tempo para simulacao do esvaziamento da caixa			
		else:
			self.MouseFlag=True		#Volta o mouse para seta								
		self.MouseClicked = False	#desmarca o clique do mouse.	

	def CA_Estado3(self):	#Esvaziamento
		self._valvula._status = "Aberta"		
		self.SurfCaixa_esvaziamento()
		self._alavanca._incrementa_contador() 

	def CA_Estado4(self):
		if(self.flagB3a): #Localiza vizinhança do botao para manutenção
			self.SurfDados.blit( self.StartImageDark, (5,5), self.retImageOffButton )
			self.MouseFlag=False
			if(self.MouseClicked==True):
				self.Estado=3 #Inicia a manutenção
				self.MouseFlag=True
				self._Controle_vazao_saida()

	def _Controle_vazao_entrada(self):
		self.VolumeCaixa = 0
		self.ControleTempoVolume = 0	
		#Calculo do tempo necessário para preencher uma linha. 
		TempoEnchimento = self._nivel_maximo/self._valvula._vazao_entrada
		self.TempoPreenchimentoLinha = (TempoEnchimento*1000)/self.nlines 
			#Tempo em milissegundos 		
	
	def _Controle_vazao_saida(self):
		self.ControleTempoVolume = 0
		TempoEsvaziamento = self._nivel_maximo/self._comporta._vazao_saida
		self.TempoRemocaoLinha = (TempoEsvaziamento*1000)/self.nlines 				

