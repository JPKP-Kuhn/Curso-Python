#coding: utf-8

import pygame as pyg
import CaixaAcoplada as CA
from SurfDados import*
from SurfCaixa import*
from SurfScreen import*
import sys

class PygameCtrl(CA.CaixaAcoplada, SurfDados, SurfCaixa, SurfScreen): 
	def __init__(self): 
		CA.CaixaAcoplada.__init__(self)
		self._pygame_basics()		
		self._pygame_loop()
		
		
		
	def _pygame_basics(self):
		#imagens da simulacao
		self._TamTela = (680,480)
		self.CorFundo = (220,220,220)
		self.OnOffImage = "Imagens/BotaoOnOff.jpg"
		self.OnOffImageDark = "Imagens/BotaoOnOffDark.jpg"
		self.BIF= "Imagens/CaixaAcoplada.png"
		self.MIF1= "Imagens/CursorMouse1.png" 
		self.MIF2= "Imagens/CursorMouse2.png" 
		self.Botao1= "Imagens/botao1.png"
		self.Botao2= "Imagens/botao2.png"		
					
		pyg.init() #Inicializa o pygame, permite chamar funções.			
		
		#Definicao de Superfícies 		
		self.SurfScreen()	#Cria superficie básica.
		self.SurfCaixa() 	#Cria superficie para caixa acoplada e define imagem		
		self.SurfDados()	#tela de informacoes
		

		
			
			
	def _pygame_loop(self):
		while True:
			for event in pyg.event.get(): 
				if event.type==pyg.QUIT:
					pyg.quit(); sys.exit(1)			
			
			self.Screen.blit(self.SurfCaixa, (10,10))#Posicao de entrada.			
			self.Screen.blit(self.SurfDados, (400,30))#Posicao de entrada.			
			
			pyg.display.update()	
			
				
			
			
			
			
