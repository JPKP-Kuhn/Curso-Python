#coding: utf-8
import pygame as pyg
class SurfCaixa(): 
	def SurfCaixa(self): 
		self.SurfCaixa = pyg.Surface([378,456])	#Cria superficie para Caixa Acoplada	
		self.BackImage = pyg.image.load(self.BIF).convert()	
		self.SurfCaixa.blit(self.BackImage,[0,0])	#Cola a imagem da caixa.	

