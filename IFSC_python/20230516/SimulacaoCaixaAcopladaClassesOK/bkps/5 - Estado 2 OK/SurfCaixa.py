#coding: utf-8
import pygame as pyg
import numpy as np
class SurfCaixa(): 
	def SurfCaixa(self): 
		self.SurfCaixa = pyg.Surface([378,456])	#Cria superficie para Caixa Acoplada
		self.BackImage = pyg.image.load(self.BIF).convert()	
		self.nlines = 0	#Numero de linhas que simula a agua.
		self.NivelAgua = []	#Vetor que guarda as retas que simulam a entrada de água.
		self.CaixaMatrizAgua()
		self.VolumeCaixa = 0		#Controle de volume
		self.TempoCaixa = 0			#Controle de tempo para enchimento ou esvaziamento.	

	#Matriz que guarda as linhas que simulam a entrada de água na caixa. 
	def CaixaMatrizAgua(self): 	
		k=6; p = 7	
		Lim = [None]*6
		Lim[0]= ((73-k,173-p),(210-k,146-p))
		Lim[1] = ((73-k,187-p),(240-k,161-p))
		Lim[2] = ((73-k,192-p),(247-k,167-p))
		Lim[3] = ((72-k,263-p),(238-k,232-p))
		Lim[4] = ((80-k,284-p),(232-k,247-p))
		Lim[5] = ((99-k,288-p),(223-k,257-p))
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
		x_i, y_i=pyg.mouse.get_pos()		
		if ((141<x_i<179)and(22<y_i<59)):
			flagB1b = True	#Flag para o botao1b							
		else: 
			flagB1b = False		
		if(self.Estado==2): #Caixa pronta para uso. Botao para cima.
			if (flagB1b): 
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
		#Faz o blit das linhas da água.
		self.SurfCaixaLinhaDagua()
		
		#Lança comando para levantar o botao da válvula e mudar de estado.
		if(self.VolumeCaixa==self.nlines): 	
			self.Estado = 2
	
	def SurfCaixaLinhaDagua(self): 
		for i in range(self.VolumeCaixa):	
			pyg.draw.line(self.SurfCaixa,(0,0,255),*self.NivelAgua[(self.nlines-1)-i],width=1)		
		
	
	
	def SurfCaixa_Prep(self):	#Roda esta funcao a cada iteracao.		
		self.SurfCaixa.blit(self.BackImage,[0,0])	#Cola a imagem da caixa.
		self.SurfCaixaBotaoValvula()				#Cola o botao da valvula. 
		self.CA_ControleOperacional()	#Controle da caixa. Definição em CaixaAcoplada.py	
		

			
		
		'''
		#Calculo dos tempos de enchimento e esvaziamento.		
		TempoEnchimento = self._nivel_maximo/self._valvula._vazao_entrada
		self.TempoPreenchimento = (TempoEnchimento*1000)/self.nlines
		TempoEsvaziamento = self._nivel_maximo/self._comporta._vazao_saida
		self.TempoEsvaziamento = (TempoEsvaziamento*1000)/self.nlines
		print("Pre = ", self.TempoPreenchimento, "Esv = ", self.TempoEsvaziamento)
		'''
		
		
		'''
		if ((134<x_i<184)and(43<y_i<66)): #Mouse na regiao do botao da valvula.
			flag = False
		if (flag):#Mouse fora da regiao do botao da valvula.
			if (self.Estado ==1): 
				flag2 = 0	#Botao da valvula para cima
			else: 
				flag2 = 2	#Botao esta apertado
		else: #Mouse na regiao do botao da valvula.	
			if(self.Estado==1):			
				if (self.MouseClicked ==True): 					
					flag2 = 2	#Botao da valvula apertado.
					self.Estado = 3 #Troca o estado
					self._clock_segundos=0	#zera a contagem.
					#self.MouseClicked =False	#Desmarca o clique do mouse
				else: 
					flag2 = 1	#Botao da valvula para cima e sombreado.					 	
			else:				
				flag2=2#Enchendo ou esvaziando o botao esta apertado				
		
		if (flag2==0): 
			self.Screen.blit(self.ValvulaImage1, (137,29))
		elif(flag2==1):
			self.Screen.blit(self.ValvulaImage1b, (137,29))	
		else: 
			self.Screen.blit(self.ValvulaImage2, (137,29))	
			
		'''	

