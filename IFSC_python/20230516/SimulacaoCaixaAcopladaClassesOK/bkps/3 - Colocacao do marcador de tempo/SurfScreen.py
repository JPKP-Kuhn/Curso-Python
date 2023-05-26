#coding: utf-8
import pygame as pyg
class SurfScreen(): 
	def SurfScreen(self): 
		self.Screen = pyg.display.set_mode(self._TamTela, 0, 32) #Tela principal
		self.Screen.fill(self.CorFundo)

