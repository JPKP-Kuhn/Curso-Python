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
		self.MouseCtrl = True
		self._pygame_basics()	#Etapa 1			
		self._pygame_loop()
		
		
		
		

		
			
			
	def _pygame_loop(self):
		while True:
			for event in pyg.event.get(): 
				if event.type==pyg.QUIT:
					pyg.quit(); sys.exit(1)			
			
			self.Screen.blit(self.SurfCaixa, (10,10))#Posicao de entrada.			
			self.Screen.blit(self.SurfDados, (400,30))#Posicao de entrada.
			self.tick = self.clock.tick()#Guarda o tempo para alterar 			
			self._visor_tempo_operacao()
			pyg.display.update()	
			
				
			
			
			
			
