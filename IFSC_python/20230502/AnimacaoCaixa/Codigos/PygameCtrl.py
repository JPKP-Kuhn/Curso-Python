#coding: utf-8

import CaixaAcoplada as CA
import pygame as pyg
import pygame.locals as pyl
from Basics import*
import sys

class PygameCtrl(CA.CaixaAcoplada, Basics):
	def __init__(self): 
		CA.CaixaAcoplada.__init__(self)
		#Metodos pygame
		pyg.init()	#Inicia o pygame		
		self._ConstantesPygame()
		self._ControleTempo()
		
		self._Screen=pyg.display.set_mode(self._TamTela, 0, 32)
		self._SurfCaixa_definicao()
		self._SurfDados_definicao()
		self._pygame_loop()
	
	
	def _pygame_loop(self):
		
		while True:
			for event in pyg.event.get(): 
				if event.type==pyl.QUIT: 
					pyg.quit(); sys.exit(1)
			self._Screen.fill(self._CorFundo)			
			self._Screen.blit(self.SurfCaixa,[10,10])
			self._SurfDados_atualizacao()
			self._Screen.blit(self.SurfDados,(400,30))			
			
			#print(pyg.mouse.get_pos())
			pyg.display.update()
		
		
