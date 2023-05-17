#coding: utf-8

import pygame as pyg
import CaixaAcoplada as CA
from PygameBasics import*
from SurfDados import*
from SurfCaixa import*
from SurfScreen import*
import sys

class PygameCtrl(CA.CaixaAcoplada, PygameBasics, SurfScreen, SurfDados, SurfCaixa ): 
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
			self.MousePrep()	#Identifica regioes para controle do mouse.				
			self.SurfDados_Prep()				
			self.SurfCaixa_Prep()
			self.CA_ControleOperacional()	#Altera ambas as superficies
					
			self.Screen.fill(self.CorFundo)	
				#Evita que as imagens do mouse na tela fiquem estaticas no frame			
			self.Screen.blit(self.SurfDados, (400,30))#Posicao de entrada.
			self.Screen.blit(self.SurfCaixa, (10,10))#Posicao de entrada.		
			self.Mouse_blit()		
			pyg.display.update()				
			
