#coding:utf-8
import pygame as pyg
import pygame.locals as pyl
import numpy as np
class SurfMalha():
	#Dados estaticos
	def SurfMalhaMatriz(self):
		linhas= 20
		colunas = 10
		self.MalhaMatriz = np.zeros(linhas*colunas)
		np.reshape(self.MalhaMatriz, (linhas,colunas))
		print(self.MalhaMatriz)		
		self.BIF = '../Imagens/malha_quadriculada.png'
		

				
	#Dados Dinamicos
	def SurfMalha(self):		
		MalhaDim = [self.ScreenDim[0]/2, self.ScreenDim[1]*0.9]
		borda = self.ScreenDim[1]*0.05 #Borda tirada do eixo y
		self.Malha = pyg.Surface(MalhaDim)
		self.MalhaBIF = pyg.image.load(self.BIF).convert_alpha()
		self.MalhaBIF = pyg.transform.scale(self.MalhaBIF, MalhaDim)
		self.Malha.blit(self.MalhaBIF, (0,0))
		
		#Teste de blitting:
		self._Retangulos_Blocos()
		
		self.MalhaPos=(self.ScreenDim[0]/2-borda,borda)
		
		

		
