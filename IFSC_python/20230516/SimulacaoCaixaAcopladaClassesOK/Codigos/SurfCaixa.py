#coding: utf-8
import pygame as pyg
import numpy as np
class SurfCaixa(): 
	#Controles Estaticos
	def SurfCaixa(self): 
		self.SurfCaixa = pyg.Surface([378,456])	#Cria superficie para Caixa Acoplada
		self.BackImage = pyg.image.load(self.BIF).convert()	
		self.nlines = 0	#Numero de linhas que simula a agua.
		self.NivelAgua = []	#Vetor que guarda as retas que simulam a entrada de água.
		self.CaixaMatrizAgua()
		self.TempoCaixa = 0			#Controle de tempo para enchimento ou esvaziamento.		

	#Controles Dinâmicos		
	def SurfCaixa_Prep(self):	#Roda esta funcao a cada iteracao.		
		self.SurfCaixa.blit(self.BackImage,[0,0])	#Cola a imagem da caixa.
		self.SurfCaixaBotaoValvula()				#Cola o botao da valvula. 
	
	#Matriz que guarda as linhas que simulam a entrada de água na caixa. 		
	def CaixaMatrizAgua(self): 			
		Lim = [None]*6
		Lim[0]= ((67,166),(204,139))
		Lim[1] = ((67,180),(234,154))
		Lim[2] = ((67,185),(241,160))
		Lim[3] = ((66,256),(231,225))
		Lim[4] = ((74,277),(226,240))
		Lim[5] = ((93,281),(217,250))
		Taxa = 1.1	#Deixa mais denso o preenchimento da agua com as retas. 
		n=[int(10*Taxa),int(3*Taxa),int(27*Taxa),int(6*Taxa),int(4*Taxa)]
		for i in range(len(n)):
			self.nlines +=n[i] 
			EsqX1 = np.linspace(Lim[i][0][0],Lim[i+1][0][0],n[i])		
			EsqY1 = np.linspace(Lim[i][0][1],Lim[i+1][0][1],n[i])
			DirX1 = np.linspace(Lim[i][1][0],Lim[i+1][1][0],n[i])
			DirY1 = np.linspace(Lim[i][1][1],Lim[i+1][1][1],n[i])
			for j in range(n[i]):				
				PosX = (EsqX1[j],EsqY1[j])
				PosY =(DirX1[j],DirY1[j])			
				self.NivelAgua.append( (PosX, PosY) )

	#Define o botão da válvula.			
	#Define a flag para o botao1b (Botao 1 black), que é o pronto para ser apertado.
	def SurfCaixaBotaoValvula(self): 			
		if(self.Estado==2): #Caixa pronta para uso. Botao para cima.
			if (self.flagB1b): 
				self.SurfCaixa.blit(self.BotaoValvulaImage1b, (126,18))
			else: 
				self.SurfCaixa.blit(self.BotaoValvulaImage1, (126,18))	
		else: 
			self.SurfCaixa.blit(self.BotaoValvulaImage2, (126,18))		

	def SurfCaixa_enchimento(self): 
		self.ControleTempoVolume+=self.tick
		if (self.ControleTempoVolume>=self.TempoPreenchimentoLinha):
			self.VolumeCaixa+=1
			self.ControleTempoVolume = 0		
		self.SurfCaixaLinhaDagua()	#Faz o blit das linhas da água.			
		if(self.VolumeCaixa==self.nlines): 	#Completou as linhas, muda de estado.
			self.Estado = 2	#Caixa está cheia. 
	
	def SurfCaixa_esvaziamento(self):
		self.SurfDados.blit( self.EspereImage, (5,5), self.retImageOnButton )
		self.ControleTempoVolume+=self.tick		
		if (self.ControleTempoVolume>self.TempoRemocaoLinha):
			self.VolumeCaixa-=1			
			self.ControleTempoVolume = 0		
		self.SurfCaixaLinhaDagua()	#Faz o blit das linhas da água.			
		if(self.VolumeCaixa==0): 	#Lança comando para levantar o botao da válvula e mudar de estado.
			self.Estado = 1			#Caixa retorna ao regime de enchimento. 

	def SurfCaixaLinhaDagua(self): 
		for i in range(self.VolumeCaixa):	
			pyg.draw.line(self.SurfCaixa,(0,0,255),*self.NivelAgua[(self.nlines-1)-i],width=1)

	def SurfCaixa_Manutencao(self):
		for i in range(self.VolumeCaixa):	
			pyg.draw.line(self.SurfCaixa,(0,0,255),*self.NivelAgua[(self.nlines-1)-i],width=1)
		
		
	
