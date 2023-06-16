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
				

	def SurfMalha_prep(self):		
		MalhaDim = [self.ScreenDim[0]/2, self.ScreenDim[1]*0.9]
		borda = self.ScreenDim[1]*0.05 #Borda tirada do eixo y
		self.SurfMalha = pyg.Surface(MalhaDim)
		BIF = '../Imagens/malha_quadriculada.png'
		self.MalhaBIF = pyg.image.load(BIF).convert_alpha()
		self.MalhaBIF = pyg.transform.scale(self.MalhaBIF, MalhaDim)
		self.SurfMalha.blit(self.MalhaBIF, (0,0))
		
		self.MalhaPos=(self.ScreenDim[0]/2-borda,borda)
		
		

		
