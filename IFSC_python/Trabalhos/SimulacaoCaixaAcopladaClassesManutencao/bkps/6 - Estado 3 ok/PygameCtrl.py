#coding: utf-8

import pygame as pyg
import CaixaAcoplada as CA
from Basics import*
from SurfDados import*
from SurfCaixa import*
from SurfScreen import*
import sys

class PygameCtrl(CA.CaixaAcoplada, Basics, SurfScreen, SurfDados, SurfCaixa ): 
	def __init__(self): 
		CA.CaixaAcoplada.__init__(self)		
		self._pygame_basics()	#Carregamento inicial			
		self._pygame_loop()		#Atualizacao frame a frame	
		
		
			
	def _pygame_loop(self):
		while True:
			for event in pyg.event.get(): 
				if event.type==pyg.QUIT:
					pyg.quit(); sys.exit(1)	
				if event.type==pyl.MOUSEBUTTONDOWN:	
					self.MouseClicked = True
			
			self.tick = self.clock.tick()	#Guarda o tempo para alterar futuramente.
			self._Controle_posicao_mouse()	#Identifica regioes para controle do mouse.				
			self.SurfDados_Prep()				
			self.SurfCaixa_Prep()
			
			self.Mouse_Prep()	#SurfScreen.py			
			self.Screen.fill(self.CorFundo)	
				#Evita que as imagens do mouse na tela fiquem estaticas no frame
			self.Screen.blit(self.SurfDados, (400,30))#Posicao de entrada.
			self.Screen.blit(self.SurfCaixa, (10,10))#Posicao de entrada.

			#Mostra o tipo de mouse
			if((pyg.mouse.get_pos()[0]!=0)and(pyg.mouse.get_pos()[1]!=0)):
				if (self.MouseFlag ==True): 
					self.Screen.blit(self.MouseImage1, 
						(pyg.mouse.get_pos()[0]-7,pyg.mouse.get_pos()[1]+3) )
				else: 	
					self.Screen.blit(self.MouseImage2, 
						(pyg.mouse.get_pos()[0],pyg.mouse.get_pos()[1])  )
					
			pyg.display.update()	
			
				
			
			
			
			
