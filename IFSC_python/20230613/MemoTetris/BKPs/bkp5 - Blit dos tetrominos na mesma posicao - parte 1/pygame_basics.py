#coding:utf-8
import sys
import pygame as pyg
import pygame.locals as pyl
from SurfScreen import*

class pygame_basics:
	def _pygame_basics(self):		
		pyg.init()

		self.SurfScreen()
		self.SurfMalhaMatriz()		
		self.Tetros()	#Cria os tetrominos, guardando-os em uma lista(matriz e superficie).
		#self.PrintTetros()	#Impressao para teste. 
		
	#Tem que ser uma função da parte dinamica do jogo, porque pode ser que seja redimensionada a tela. 
	def _Superficies_Blocos(self):
		#Guarda as superficies para cada bloco individual. 
		self.SurfBlocos = [None]*7	#Superficies individuais dos blocos.
		#Carrega as imagens, salva nas superficies. 
		BlocosCoresPath = "../Imagens/blocos.png"
		BlocosCores = pyg.image.load(BlocosCoresPath).convert()
		self.Trama = (self.Malha.get_width()/10, self.Malha.get_height()/20)#Tamanho da trama.
		BlocosCores = pyg.transform.scale(BlocosCores, (self.Trama[0]*7, self.Trama[1]) )
		#Criação das superficies dos blocos
		for i in range(7):
			self.SurfBlocos[i] =pyg.Surface((self.Trama[0], self.Trama[1])) 			
			RetBloco = pyg.Rect((i*self.Trama[0],0),self.Trama)			
			self.SurfBlocos[i].blit(BlocosCores, (0,0),RetBloco)	#Faz o blit do retangulo. 		

	'''
	self.SupTetro é uma lista de dicionarios, para ver o padrão 2 do tetromino 0 basta fazer self.SupTetro[0][2]
	'''	
	def _Superficies_Tetrominos(self): 
		self.SurfTetros = []	#Cria lista para guardar as superfícies dos tetrominos. 
		self.SurfTetroBase = pyg.Surface((self.Trama[0]*4,self.Trama[1]*4))#Cria superficie
		self.SurfTetroBase=self.SurfTetroBase.convert_alpha()	#Torna transparente a superficie. 
		self.SurfTetroBase.fill((0,0,0,0))#Deixa a superficie transparente, com alpha = 0		
		self.SupTetro = []	#Lista das superficies dos tetrominos. 
		for tetro in range(len(self._Tetros)-1):	#Enumera os tetrominos, serve tambem para as cores dos blocos.
			DicPadraoTetromino = {}	#Guarda um padrao do tetromino tetro.
			#Passa por cada Tetromino, exceto o extra, que vai ter cores aleatorias para os blocos. 
			for padrao, mat in self._Tetros[tetro].items():		
				Stetro = pyg.Surface.copy(self.SurfTetroBase) #Faz uma copia da superficie base para cada padrao
				for i in range(4):
					for j in range(4):
						if mat[i][j]==1:
							Stetro.blit(self.SurfBlocos[tetro], (self.Trama[0]*i,self.Trama[1]*j) )				
				DicPadraoTetromino[padrao] = Stetro		#Guarda no dicionario a superficie feita. 						
			self.SupTetro.append(DicPadraoTetromino)

	def PrintTetros(self):
		print("Quantidade de Tetros: ", len(self._Tetros))
		print(self._Tetros[0])		
		for i in range(len(self._Tetros)):			
			print("Tetromino :", i)
			for key, value in self._Tetros[i].items():
				print("Padrão ", key)
				print(value)
			print("####################")	


		
				
				
		
		
		


