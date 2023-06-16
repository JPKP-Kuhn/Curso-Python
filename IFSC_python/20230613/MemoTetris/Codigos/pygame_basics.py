#coding:utf-8
import sys
import pygame as pyg
import pygame.locals as pyl
from SurfScreen import*
import sys

class pygame_basics:
	def _pygame_basics(self):		
		pyg.init()
		#Criacao dos valores estáticos usados. 
		self.SurfScreen()
		self.SurfMalhaMatriz()	
		self.Ntetros = 8 #Numero de tetrominos usados. Padrão é 7
		self.Tetros()	#Cria os tetrominos, guardando-os em uma lista(matriz e superficie).
		#self.PrintTetros()	#Impressao para teste. 
		
		#Inicializacao do relogio:
		self.ControleInicialTempo()
		
		#Fontes usadas
		self.FontA15=pyg.font.SysFont("Arial", 15)		
		
		#Carregamento de imagens fixas
		BlocosCoresPath = "../Imagens/blocos.png"
		self.BlocosCores = pyg.image.load(BlocosCoresPath).convert()	
			#Uso em _Superficie_Blocos()
		
		#Controle de movimento dos tetrominos
		self.Rotacao = 0
		self.TetroAtual = 0
					
		
		
	def ControleInicialTempo(self):
		self.clock = pyg.time.Clock()
		self.time_check = 0	#Verifica se passou 60 seg;
		self.TempoTotalSeg = 0
		self.TempoTotalMin = 0
		self.tick = self.clock.tick()

	def ControleTempo(self):
		self.tick =  self.clock.tick()
		self.time_check += self.tick		
		self.TempoTotalSeg = int(self.time_check/1000.)		
		if (self.time_check>=(60*1000)): #1 minuto passado
			self.time_check = 0
			self.TempoTotalSeg = 0
			self.TempoTotalMin+=1
			
		
		
				
				
		
		
		


