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
		self.TelaDim = [350,250]
		self.Screen = pyg.display.set_mode(self.TelaDim,pyg.RESIZABLE, 32)
			#Início do tamanho da tela
		self.comprimento = 50
		self.altura = 100			
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
			
			self.Screen.fill((0,0,150))
			tempAltura = self.Screen.get_height()
			tempComprimento = self.Screen.get_width()
			
			varx = -(1-self.Screen.get_width()/self.TelaDim[0])
			vary = -(1-self.Screen.get_height()/self.TelaDim[1])
			strg = "x: {0}, y = {1}".format(varx, vary)
			if ((varx!=0) and(vary!=0)):
				print(strg)
			self.comprimento=self.comprimento*(1+varx)
			self.altura*=(1+vary)
			self.TelaDim = [self.Screen.get_width(),self.Screen.get_height()]
			
			posx = self.Screen.get_width()/2-self.comprimento/2
			posy = self.Screen.get_height()/2-self.altura/2
			retangulo = pyg.Rect(posx, posy, self.comprimento, self.altura)
			pyg.draw.rect(self.Screen, (255,0,0), retangulo )
		
			pyg.display.update()
	
	

if __name__=="__main__": 
	MemoTetris()

