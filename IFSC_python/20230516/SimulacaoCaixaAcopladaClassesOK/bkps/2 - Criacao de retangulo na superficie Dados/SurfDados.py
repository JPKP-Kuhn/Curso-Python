#coding: utf-8
		
import pygame as pyg

class SurfDados():  
	def SurfDados(self):	#Observar que nao é funcao construtora 
		self.SurfDados = pyg.Surface([260,400])	#Cria superficie para área de dados
		self.SurfDadosCor = (120,120,120)		#cinza escuro
		self.SurfDados.fill(self.SurfDadosCor)	#pinta a superficie.
		
		
		
		#self._botao_liga_desl()					#Insere botao liga-desliga
		self._visor_tempo_operacao()
		
		
		#self.SurfDados.blit( self.StartImage1, (5,5), self.retImageOnOffButton )#Para fazer teste.
		
	
		
	def _botao_liga_desl(self): 
		self.BotaoLigaDesl = 1	#0-off	1-on
		self.StartImage =pyg.image.load(self.OnOffImage).convert_alpha()
		self.StartImageDark =pyg.image.load(self.OnOffImageDark).convert_alpha()		
		reducao = 15	#Taxa de reducao da figura do botao de liga/desliga. 
		base = self.StartImage.get_width()
		altura = self.StartImage.get_height()
		self.StartImage1=pyg.transform.scale(self.StartImage,(base/reducao,altura/reducao))
		self.StartImage1Dark=pyg.transform.scale(self.StartImageDark,(base/reducao,altura/reducao))
		#Cria retângulo para inserção do botao de liga-desl
		self.retImageOnOffButton = pyg.Rect((0,0),(self.StartImage1.get_width()/2,
				self.StartImage1.get_height()))	
				
			
	def _visor_tempo_operacao(self):	
		#Criação do retângulo:
		RetanguloGrande = pyg.Rect((10,350),(240,40))	#Pos Entrada, dimensoes.	
		self.RetTempo = pyg.draw.rect(self.SurfDados,(255,255,255), RetanguloGrande)
				#Faz o blit do retangulo na tela. 		
		FontTempoOperacao = pyg.font.SysFont('Arial', 15)		
			
			
		#TextoTempoOperacao = FontTempoOperacao.render('Tempo de operação:', True, (0,0,0))		
		#self.SurfDados.blit(TextoTempoOperacao, (15, 360)) #Blit do texto

