#coding:utf-8
import pygame as pyg
import pygame.locals as pyl
class SurfScreen():
	def SurfScreen(self):
		self.Screen = pyg.display.set_mode((500,500),pyg.RESIZABLE, 32)
		self.ScreenAspectRatio = (16,9)	#Orienta no futuro as dimensoes. 
		self.SurfScreen_prep()
	
	def SurfScreen_prep(self):
		self.ScreenDim = (self.Screen.get_width(),self.Screen.get_height() )

	
	
		
