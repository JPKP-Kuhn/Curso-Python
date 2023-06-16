#coding:utf-8
import sys
import pygame as pyg
import pygame.locals as pyl

'''
Geracao de uma tela de tamanho variavel com retangulo de tamanho fixo no meio. 


'''

class MemoTetris():
	def __init__(self):
		
		pyg.init()
		self.Screen = pyg.display.set_mode((350,250),pyg.RESIZABLE, 32)
			#Início do tamanho da tela
		self._pygame_loop()
	
	def _pygame_loop(self): 
		while True: 
			for event in pyg.event.get():
				if event.type ==pyl.QUIT:
					pyg.quit(); sys.exit(1)
				
			if event.type==pyl.KEYDOWN: 
					if event.key==pyl.K_ESCAPE:
						pyg.quit()
						sys.exit()	
			
			self.Screen.fill((0,0,50))
			comprimento = 50
			altura = 100
			
			posx = self.Screen.get_width()/2-comprimento/2
			posy = self.Screen.get_height()/2-altura/2
			retangulo = pyg.Rect(posx, posy, comprimento, altura)
			pyg.draw.rect(self.Screen, (255,0,0), retangulo )
		
			pyg.display.update()
	
	

if __name__=="__main__": 
	MemoTetris()

