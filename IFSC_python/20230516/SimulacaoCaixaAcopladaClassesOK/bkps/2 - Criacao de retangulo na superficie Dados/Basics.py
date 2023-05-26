#coding: utf-8
import pygame as pyg
class Basics(): 
	def _pygame_basics(self):
		#imagens da simulacao
		self._TamTela = (680,480)
		self.CorFundo = (220,220,220)
		self.OnOffImage = "Imagens/BotaoOnOff.jpg"
		self.OnOffImageDark = "Imagens/BotaoOnOffDark.jpg"
		self.BIF= "Imagens/CaixaAcoplada.png"
		self.MIF1= "Imagens/CursorMouse1.png" 
		self.MIF2= "Imagens/CursorMouse2.png" 
		self.Botao1= "Imagens/botao1.png"
		self.Botao2= "Imagens/botao2.png"		
					
		pyg.init() #Inicializa o pygame, permite chamar funções.			
		
		#Definicao de Superfícies 		
		self.SurfScreen()	#Cria superficie básica.
		self.SurfCaixa() 	#Cria superficie para caixa acoplada e define imagem		
		self.SurfDados()	#tela de informacoes
		
		
		
		
		

