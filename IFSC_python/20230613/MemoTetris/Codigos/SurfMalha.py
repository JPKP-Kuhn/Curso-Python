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
		self.MalhaMatriz =self.MalhaMatriz.reshape(20,10)		
		print(self.MalhaMatriz)		
		self.BIF = '../Imagens/malha_quadriculada.png'
		


	#Se os blocos estão corretos deverá aparecer em diagonal os retangulos. 		
	def _Teste_Blit_Blocos(self):
		for i in range(self.Ntetros):
			self.Malha.blit(self.SurfBlocos[i],(i*self.Trama[0],i*self.Trama[1]) )
		


	'''
    if event.type == pygame.KEYDOWN:
      if event.key == K_LEFT:
        keys_pressed_list.append("left")
      if event.key == K_RIGHT:
        keys_pressed_list.append("right")
      if event.key == K_UP:
        keys_pressed_list.append("up")
      if event.key == K_DOWN:
        keys_pressed_list.append("down")
      if event.key == K_a:
        keys_pressed_list.append("a")
      if  event.key == K_d:
        keys_pressed_list.append("b")
      if event.key == K_w:
        keys_pressed_list.append("w")
      if event.key == K_s:
        keys_pressed_list.append("s")
      if event.key == K_SPACE:
        keys_pressed_list.append("space")
      if event.key == K_q:
        keys_pressed_list.append("q")
      if event.key == K_e:
        keys_pressed_list.append("e")
    if event.type == pygame.MOUSEBUTTONDOWN:
      keys_pressed_list.append("click")
	'''
	
	def _Teste_blit_Tetrominos(self):
		self.Malha.blit(self.SupTetro[(self.TetroAtual%7)][self.Rotacao%7-3], (5*self.Trama[0], (self.TempoTotalSeg%20)*self.Trama[1]) )

		


	
	def _Teste_Rotacao_Tetrominos(self):
		pass			
		
				
	#Dados Dinamicos
	def SurfMalha(self):		
		MalhaDim = [self.ScreenDim[0]/2, self.ScreenDim[1]*0.9]
		borda = self.ScreenDim[1]*0.05 
			#Borda tirada do eixo y, tem o objetivo de tirar a borda da malha. 
		self.MalhaPos=(self.ScreenDim[0]/2-borda,borda)
		self.Malha = pyg.Surface(MalhaDim)
		self.MalhaBIF = pyg.image.load(self.BIF).convert_alpha()
		self.MalhaBIF = pyg.transform.scale(self.MalhaBIF, MalhaDim)
		self.Malha.blit(self.MalhaBIF, (0,0))
		
		self._Superficies_Blocos()	
			#Em cada nova redimensionamento deve-se construir a superficie de cada bloquinho. 				
		self._Teste_Blit_Blocos()	#Blit de teste dos tetrominos.
			
		self._Superficies_Tetrominos()	#Requer os blocos já montados em _Superficies_Blocos(self)		
		
		
		
		#Cada Tetromino em queda
		self._Teste_blit_Tetrominos()
				
		#Teste de rotacao dos blocos. 
		
		
		
		
		
		
		
		

		
