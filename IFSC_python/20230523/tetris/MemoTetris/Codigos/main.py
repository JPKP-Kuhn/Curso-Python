#coding:utf-8
import sys
import pygame as pyg
import pygame.locals as pyl
from SurfScreen import*
from SurfMalha import*
from SurfDados import*
from pygame_basics import *

class MemoTetris(SurfScreen, SurfMalha, SurfDados, pygame_basics):
	def __init__(self):
		self._pygame_basics()
		self._pygame_loop()
			
			

		
	
	def _pygame_loop(self): 
		while True: 
			for event in pyg.event.get():
				if event.type ==pyl.QUIT:
					pyg.quit(); sys.exit(1)
				
				if event.type==pyl.KEYDOWN: 
					if event.key==pyl.K_ESCAPE:
						pyg.quit(), 
						sys.exit()				
			self.Screen.fill((0,0,50))
			self.SurfScreen_prep()
			self.SurfMalha_prep()
			self.SurfDados_prep()
			
			self.Screen.blit(self.SurfMalha, self.MalhaPos)
			
			
			pyg.display.update()
	
	

if __name__=="__main__": 
	MemoTetris()

