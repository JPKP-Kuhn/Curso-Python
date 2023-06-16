#coding:utf-8
import numpy as np
import pygame as pyg
import pygame.locals as pyl

class Tetromino: #Indica o tetromino e a rotacao que sofre.	
	'''
	Os tetrominos são indicados pelo tipo. 
	Cada Tetromino é elemento da lista 
	A rotação dos tetrominos segue o dicionario abaixo: 
	-3: -270^o
	-2: -180^o
	-1: -90^o
	 0:  0^o
	 1:  90^o
	 2:  180^o
	 3:  270^o		
	 
	 Todos os tetrominos devem começar na parte mais alta. 
	'''	
	def Tetros(self): 					
		#Criação das matrizes dos tetrominos
		self.BaseTetro = np.zeros((4,4), dtype = np.int_) #Base para os tetrominos
		self._Tetros = []	#Guarda formato dos tetrominos em forma de matriz		
		self.Tetro1()				
		self.Tetro2()
		self.Tetro3()
		self.Tetro4()
		self.Tetro5()
		self.Tetro6()
		self.Tetro7()
		self.Tetro8()	
		
		'''
		for i in range(len(self._Tetros)):	
			print("Tetromino ", i)		
			for key, value in self._Tetros[i].items():			
				print(key, end = ": \n")
				print(value)				
			print()
		'''	
		
		#Criação das superfícies dos tetrominos:
		#Cada tetromino possui tantas superficies quantas matrizes houver.

	#Tetromino 8: Extra
	def Tetro8(self):
		Tetro = {}	
		Tetro1 = np.copy(self.BaseTetro)
		Tetro1[0][1]=1
		Tetro1[1][0]=1
		Tetro1[1][2]=1
		Tetro1[2][1]=1
		for i in range(-3,4):
			Tetro[i] = Tetro1
		self._Tetros.append(Tetro)	


	#Tetromino 7: L
	def Tetro7(self):
		Tetro = {}	
		#Posicao 0
		Tetro1 = np.copy(self.BaseTetro)
		Tetro1[0][1]=1
		Tetro1[1][1]=1
		Tetro1[2][1]=1
		Tetro1[2][2]=1
		Tetro[0]=Tetro1
		#Posicao 90 e -270
		Tetro1 = np.copy(self.BaseTetro)
		Tetro1[1][1]=1
		Tetro1[1][2]=1
		Tetro1[1][3]=1
		Tetro1[0][3]=1
		Tetro[1]=Tetro[-3]=Tetro1
		#Posicao 180 e -180
		Tetro1 = np.copy(self.BaseTetro)
		Tetro1[0][1]=1
		Tetro1[0][2]=1
		Tetro1[1][2]=1
		Tetro1[2][2]=1
		Tetro[-2]=Tetro[2]=Tetro1
		#Posicao -90 e 270
		Tetro1 = np.copy(self.BaseTetro)
		Tetro1[0][1]=1
		Tetro1[0][2]=1
		Tetro1[0][3]=1
		Tetro1[1][1]=1
		Tetro[-1]=Tetro[3]=Tetro1
		self._Tetros.append(Tetro)		
			
	#Tetromino 6: J
	def Tetro6(self):
		Tetro = {}			
		#Posicao 0
		Tetro1 = np.copy(self.BaseTetro)
		Tetro1[0][2]=1
		Tetro1[1][2]=1
		Tetro1[2][2]=1
		Tetro1[3][1]=1
		Tetro[0]=Tetro1
		#Posicao 90 e -270
		Tetro1 = np.copy(self.BaseTetro)
		Tetro1[0][1]=1
		Tetro1[0][2]=1
		Tetro1[0][3]=1
		Tetro1[1][3]=1
		Tetro[1]=Tetro[-3]=Tetro1
		#Posicao 180 e -180
		Tetro1 = np.copy(self.BaseTetro)
		Tetro1[0][1]=1
		Tetro1[0][2]=1
		Tetro1[1][1]=1
		Tetro1[2][1]=1
		Tetro[-2]=Tetro[2]=Tetro1		
		#Posicao -90 e 270
		Tetro1 = np.copy(self.BaseTetro)
		Tetro1[0][1]=1
		Tetro1[1][1]=1
		Tetro1[1][2]=1
		Tetro1[1][3]=1
		Tetro[-1]=Tetro[3]=Tetro1
		self._Tetros.append(Tetro)	

		
	#Tetromino 5:
	def Tetro5(self):
		Tetro = {}	
		#Posicao 0,180,-180		
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[0][0] = 1
		Tetro1[0][1] = 1
		Tetro1[1][1] =1
		Tetro1[1][2] =1
		Tetro[0]=Tetro[2]=Tetro[-2]=Tetro1
		#Posicao (90 e -270) e (-90 e 270):
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[0][1] = 1
		Tetro1[1][1] = 1
		Tetro1[1][0] = 1
		Tetro1[2][0] =1
		Tetro[1]=Tetro[-3]=Tetro[3]=Tetro[-1]=Tetro1	
		#Inserção dos tetrominos		
		self._Tetros.append(Tetro)

	#Tetromino 4:
	def Tetro4(self):
		Tetro = {}		
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[0][1] = 1
		Tetro1[0][2] = 1
		Tetro1[1][1] =1
		Tetro1[1][2] =1
		for i in range(-3,4):
			Tetro[i] = Tetro1
		self._Tetros.append(Tetro)	
	
	#Tetromino 3:		
	def Tetro3(self):
		Tetro = {}		
		#Posicao 0:
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[0][1] = 1
		Tetro1[0][2] = 1
		Tetro1[1][0] =1
		Tetro1[1][1] =1
		Tetro[0]=Tetro1
		#Posicao (90 e -270) e (-90 e 270):
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[0][0] = 1
		Tetro1[1][0] = 1
		Tetro1[1][1] = 1
		Tetro1[2][1] =1
		Tetro[1]=Tetro[-3]=Tetro[3]=Tetro[-1]=Tetro1	
		#Posicao 180 e -180:
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[1][0] = 1
		Tetro1[1][1] = 1
		Tetro1[0][1] = 1
		Tetro1[0][2] =1
		Tetro[2]=Tetro[-2]=Tetro1
		#Inserção dos tetrominos		
		self._Tetros.append(Tetro)
		
	#Tetromino 1:	
	def Tetro1(self):
		Tetro = {}		
		Tetro1 = np.copy(self.BaseTetro)
		for i in range(4): 
			Tetro1[3][i] = 1
		Tetro[0] = Tetro[2]=Tetro[-2]=Tetro1
		Tetro2 = np.copy(self.BaseTetro)
		for i in range(4): 
			Tetro2[i][0] = 1
		Tetro[-1] =Tetro[1] = Tetro[3]=Tetro[-3]=Tetro2		
		self._Tetros.append(Tetro)			
		
	#Tetromino 2:		
	def Tetro2(self):
		Tetro = {}		
		#Posicao 0:
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[2][1] = 1
		Tetro1[3][0] = 1
		Tetro1[3][1] =1
		Tetro1[3][2] =1
		Tetro[0]=Tetro1
		#Posicao 90 e -270:
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[2][0] = 1
		Tetro1[1][1] = 1
		Tetro1[2][1] = 1
		Tetro1[3][1] =1
		Tetro[1]=Tetro[-3]=Tetro1
		#Posicao 180 e -180:
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[2][0] = 1
		Tetro1[2][1] = 1
		Tetro1[2][2] = 1
		Tetro1[3][1] =1
		Tetro[2]=Tetro[-2]=Tetro1
		#Posicao 270 e -90:
		Tetro1 = np.copy(self.BaseTetro)		
		Tetro1[1][0] = 1
		Tetro1[2][0] = 1
		Tetro1[2][1] = 1
		Tetro1[3][0] =1
		Tetro[3]=Tetro[-1]=Tetro1	
		#Inserção dos tetrominos		
		self._Tetros.append(Tetro)


if __name__=="__main__": 
	A = Tetromino()
	
	
