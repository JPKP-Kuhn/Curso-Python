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
		self.Tetros()	
			#Cria os tetrominos, guardando-os em uma lista(matriz e superficie).
		
	def _Retangulos_Blocos(self):
		#Guarda os retângulos que representam os blocos. 
		self.SurfBlocos = [None]*7#Superficies individuais dos blocos.
		#Carrega as imagens, salva nas superficies. 
		BlocosCoresPath = "../Imagens/blocos.png"
		BlocosCores = pyg.image.load(BlocosCoresPath).convert()
		Trama = (self.Malha.get_width()/10, self.Malha.get_height()/20)#Tamanho da trama.
		BlocosCores = pyg.transform.scale(BlocosCores, (Trama[0]*7, Trama[1]) )
		#Criação dos retangulos
		for i in range(7):
			self.SurfBlocos[i] =pyg.Surface((Trama[0], Trama[1])) 			
			RetBloco = pyg.Rect((i*Trama[0],0),Trama)			
			self.SurfBlocos[i].blit(BlocosCores, (0,0),RetBloco)			
		#Teste de uso dos retangulos.	
		for i in range(7):
			self.Malha.blit(self.SurfBlocos[i],(i*Trama[0],i*Trama[1]) )
		
		 


