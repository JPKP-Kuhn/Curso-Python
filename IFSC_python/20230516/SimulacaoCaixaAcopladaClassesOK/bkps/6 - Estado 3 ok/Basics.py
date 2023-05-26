#coding: utf-8
import pygame as pyg

'''
Classe que faz registros do pygame para controle fora do loop principal.
Pode fazer registros de tempo
'''

class Basics(): 
	def _pygame_basics(self):
		#imagens da simulacao
		self._TamTela = (680,480)
		self.CorFundo = (220,220,220)		
		self.BIF= "../Imagens/CaixaAcoplada.png"
		self.MIF1= "../Imagens/CursorMouse1.png" 
		self.MIF2= "../Imagens/CursorMouse2.png" 
		ValvulaImage1Path = '../Imagens/botao1.png'
		ValvulaImage2Path = '../Imagens/botao2.png'
							
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
		
		#Controle de cliques de mouse
		#Botoes B1 são os que aparecem já no inicio da simulacao
		self.flagB1a = False	#Localiza o botao de liga
		self.flagB1b = False	#Localiza o botao da valvula. 		
		self.flagB2a = False	#Localiza botao de desliga. #Depois do estado 2		
				
		#Botao da valvula
		self.BotaoValvulaImage1 = pyg.image.load(ValvulaImage1Path).convert_alpha()
		self.BotaoValvulaImage1b = pyg.image.load(ValvulaImage1Path).convert()
		self.BotaoValvulaImage2 = pyg.image.load(ValvulaImage2Path).convert_alpha()			
		self.BotaoValvulaImage1=pyg.transform.scale(self.BotaoValvulaImage1,(512*0.08,512*0.08))
		self.BotaoValvulaImage1b=pyg.transform.scale(self.BotaoValvulaImage1b,(512*0.08,512*0.08))	
		self.BotaoValvulaImage2=pyg.transform.scale(self.BotaoValvulaImage2,(512*0.08,512*0.08))
		
		
	def _Controle_tempo(self):
		self.clock = pyg.time.Clock()	#Inicializa o contador de tempo.			
		self.cronometro = False
		self.time_check = 0	#Verifica se passou 60 seg;
		self.TempoTotalSeg = 0
		self.TempoTotalMin = 0
	
	def _Controle_posicao_mouse(self):
		x_i, y_i=pyg.mouse.get_pos()		
		if ((141<x_i<179)and(22<y_i<59)):
			self.flagB1b = True	#Flag para o botao1b										
		else: 
			self.flagB1b = False			
		if (400<pyg.mouse.get_pos()[0]<450 and 32<pyg.mouse.get_pos()[1]<75):
			self.flagB1a =True
		else: 
			self.flagB1a = False		

	
	def _Controle_vazao_entrada(self):
		self.VolumeCaixa = 0
		self.ControleTempoVolume = 0	
		#Calculo do tempo necessário para preencher uma linha. 
		TempoEnchimento = self._nivel_maximo/self._valvula._vazao_entrada
		self.TempoPreenchimentoLinha = (TempoEnchimento*1000)/self.nlines 
			#Tempo em milissegundos 		
	
	def _Controle_vazao_saida(self):
		self.ControleTempoVolume = 0
		TempoEsvaziamento = self._nivel_maximo/self._comporta._vazao_saida
		self.TempoRemocaoLinha = (TempoEsvaziamento*1000)/self.nlines 	
		
		

