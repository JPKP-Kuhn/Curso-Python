#coding:utf-8
import pygame as pyg
import pygame.locals as pyl


'''
Cria as superficies individuais de cada tetromino. 
self.SurfBlocos = [] é uma lista de cada um dos retângulos que formam os tetrominos.
self.Trama é uma tupla com a dimensão da trama (cada quadradinho) da malha. 
O método pega cada retângulo e altera as dimensoes para o tamanho da trama e faz o blit em SurfBlocos
'''

class SurfTetrominos():

	def _Superficies_Blocos(self):
		#Guarda as superficies para cada bloco individual. 
		self.SurfBlocos = [None]*self.Ntetros	#Superficies individuais dos blocos.
		#Carrega as imagens, salva nas superficies. 
		self.Trama = (self.Malha.get_width()/10, self.Malha.get_height()/20)
			#Tamanho da trama (quadrado que guarda o bloco individual).		
		self.BlocosCores = pyg.transform.scale(self.BlocosCores, (self.Trama[0]*7, self.Trama[1]) )
			#self.BlocosCores definido em _pygame_basics()
		#Criação das superficies dos blocos
		
		for i in range(self.Ntetros ):	#São 8 tetrominos usados, no clássico sao 7. 
			self.SurfBlocos[i] =pyg.Surface((self.Trama[0], self.Trama[1])) 			
			RetBloco = pyg.Rect((i*self.Trama[0],0),self.Trama)			
			self.SurfBlocos[i].blit(self.BlocosCores, (0,0),RetBloco)	#Faz o blit do retangulo. 		



	'''
	self.SupTetro é uma lista de dicionarios, para ver o padrão 2 do tetromino 0 basta fazer self.SupTetro[0][2]
	'''	
	def _Superficies_Tetrominos(self): 	
		self.SurfTetros = []	#Cria lista para guardar as superfícies dos tetrominos. 
		self.SurfTetroBase = pyg.Surface((self.Trama[0]*4,self.Trama[1]*4))#Cria superficie 4x4 blocos
		self.SurfTetroBase=self.SurfTetroBase.convert_alpha()	#Torna transparente a superficie. 
		self.SurfTetroBase.fill((0,0,0,0))#Deixa a superficie transparente, com alpha = 0		
		self.SupTetro = []	#Lista das superficies dos tetrominos. 		
		for tetro in range(len(self._Tetros)):	#Enumera os tetrominos, serve tambem para as cores dos blocos.
			DicPadraoTetromino = {}	#Guarda um padrao do tetromino tetro.
			#Passa por cada Tetromino, exceto o extra, que vai ter cores aleatorias para os blocos. 
			#self._Tetros definido em Tetrominos.py. São os formatos dos tetrominos.
			#É uma lista de dicionarios. Key varia de -3 a 3 (inclusive) indicando cada rotacao do tetromino.
			#Value é a matriz que representa o tetromino.
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


		


	
	
		
