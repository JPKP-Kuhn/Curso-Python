#coding: utf-8
import pygame as pyg
class SurfScreen(): 
	def SurfScreen(self): 
		self.Screen = pyg.display.set_mode(self._TamTela, 0, 32) #Tela principal		
		
	def MousePrep(self):
		x_i, y_i=pyg.mouse.get_pos()		
		if ((141<x_i<179)and(22<y_i<59)):
			self.flagB1b = True	#Flag para o botao1b										
		else: 
			self.flagB1b = False			
		if (400<x_i<450 and 32<y_i<75):	
			#Trocar por xi e yi
			self.flagB1a =True
		else: 
			self.flagB1a = False
		if (400<pyg.mouse.get_pos()[0]<450 and 95<pyg.mouse.get_pos()[1]<137):
			self.flagB3a = True
		else:
			self.flagB3a = False
		if (475<x_i<515 and 43<y_i<81):
			self.flagB3b = True
		else:
			self.flagB3b = False

			
	def Mouse_blit(self):	#Seleciona o tipo de mouse	
		MouseBound1 = False
		MouseBound2 = False
		if((pyg.mouse.get_pos()[0]!=0)and(pyg.mouse.get_pos()[1]!=0)):
			MouseBound1 = True
		if((pyg.mouse.get_pos()[0]!=self._TamTela[0]-1)and(pyg.mouse.get_pos()[1]!=self._TamTela[1])):
			MouseBound2 = True
		if (MouseBound1 and MouseBound2): 			
			if (self.MouseFlag ==True): 
				self.Screen.blit(self.MouseImage1,  #Mouse maozinha
					(pyg.mouse.get_pos()[0]+3,pyg.mouse.get_pos()[1]-7))
			else: 	
				self.Screen.blit(self.MouseImage2, #Mouse normal
					(pyg.mouse.get_pos()[0],pyg.mouse.get_pos()[1]))


