#coding: utf-8
import pygame as pyg
class SurfScreen(): 
	def SurfScreen(self): 
		self.Screen = pyg.display.set_mode(self._TamTela, 0, 32) #Tela principal
		
		
	def Mouse_Prep(self): 
		MouseImage1 = pyg.image.load(self.MIF1).convert_alpha()
		self.MouseImage1 = pyg.transform.scale(MouseImage1,(21,29))	
		MouseImage2 = pyg.image.load(self.MIF2).convert_alpha()
		self.MouseImage2 = pyg.transform.scale(MouseImage2,(25,35))		
		pyg.mouse.set_visible(False)	#Remove a imagem original do mouse.	
		


