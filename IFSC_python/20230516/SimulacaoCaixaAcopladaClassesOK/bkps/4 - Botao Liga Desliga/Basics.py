#coding: utf-8
import pygame as pyg
class Basics(): 
	def _pygame_basics(self):
		#imagens da simulacao
		self._TamTela = (680,480)
		self.CorFundo = (220,220,220)
		self.OnOffImage = "../Imagens/BotaoOnOff.jpg"
		self.OnOffImageDark = "../Imagens/BotaoOnOffDark.png"
		self.BIF= "../Imagens/CaixaAcoplada.png"
		self.MIF1= "../Imagens/CursorMouse1.png" 
		self.MIF2= "../Imagens/CursorMouse2.png" 
		self.Botao1= "../Imagens/botao1.png"
		self.Botao2= "../Imagens/botao2.png"
		
		
					
		pyg.init() #Inicializa o pygame, permite chamar funções.
		self._Controle_tempo()	#Controle de tempo (self.cronometro inicia o relogio.)

		#Controlador de mouse
		self.MouseClicked = False	#Informa se houve clique de mouse
		self.MouseFlag = True		#Flag para utilizar mouse em posicoes definidas.
									#True: seta, False: mão
		#Definicao de Superfícies 		
		self.SurfScreen()	#Cria superficie básica.
		self.SurfCaixa() 	#Cria superficie para caixa acoplada e define imagem
		self.SurfDados()	#tela de informacoes
		self.Mouse_Prep()	#Prepara imagens usadas no mouse. 
		
		
		
	def _Controle_tempo(self):
		self.clock = pyg.time.Clock()	#Inicializa o contador de tempo.
		#self.tick = 0.		
		self.cronometro = False
		self.time_check = 0	#Verifica se passou 60 seg;
		self.TempoTotalSeg = 0
		self.TempoTotalMin = 0					
	
		
		
		
		
		

