#coding: utf-8
		
import pygame as pyg

class SurfDados():  
	def SurfDados(self):	#Observar que nao é funcao construtora 
		self.SurfDados = pyg.Surface([260,400])	#Cria superficie para área de dados
		self.SurfDadosCor = (120,120,120)		#cinza escuro
		self.SurfDados.fill(self.SurfDadosCor)	#pinta a superficie.
		
		#Retângulos de informacoes:
		self.RetanguloGrande = pyg.Rect((10,350),(240,40))	#Pos Entrada, dimensoes.			
		
		self._retangulo_botao_liga_desl()					#Insere botao liga-desliga
		self.FontA15 = pyg.font.SysFont('Arial', 15)
		
		#Controle de tempo
		self.clock = pyg.time.Clock()	#Inicializa o contador de tempo.
		#self.tick = 0.		
		self.cronometro = True
		self.time_check = 0	#Verifica se passou 60 seg;
		self.TempoTotalSeg = 0
		self.TempoTotalMin = 0
		
		
		
		
		
	
	'''
	Prepara regiao para insercao do botao de liga desliga.
	'''	
	def _retangulo_botao_liga_desl(self): 
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
				
		#Colocar um dos itens abaixo para ver o botao funcionando				
		#self.SurfDados.blit( self.StartImage1, (5,5))	#Mostra toda a imagem
		#self.SurfDados.blit( self.StartImage1, (5,5), self.retImageOnOffButton )
			#Mostra a imagem limitada ao botao verde. 
	
	
			
	def _visor_tempo_operacao(self):	
		#Criação do retângulo:			
		self.RetTempo = pyg.draw.rect(self.SurfDados,(255,255,255), self.RetanguloGrande)
				#Faz o blit do retangulo na tela. 					
		TextoTempoOperacao = self.FontA15.render('Tempo de operação:', True, (0,0,0))		
		self.SurfDados.blit(TextoTempoOperacao, (15, 360)) #Blit do texto
		TextoTempoOperacao = self.FontA15.render('Tempo de operação:', True, (0,0,0))		
		self.SurfDados.blit(TextoTempoOperacao, (15, 360)) #Blit do texto
		TextoTempo = "{0:02d} : {1:02d}".format(self.TempoTotalMin, self.TempoTotalSeg)
		print(TextoTempo)
		TextoTempo = self.FontA15.render(TextoTempo, True, (0,0,0))		
		self.SurfDados.blit(TextoTempoOperacao, (15, 360)) #Blit do texto
		self.SurfDados.blit(TextoTempo, (160, 360)) #Blit do texto
		
		if (self.cronometro): #Cronometro iniciou com o enchimento da caixa.  
			self.time_check += self.tick
			self.TempoTotalSeg = int(self.time_check/1000.)
			if (self.time_check>=(60*1000)): #1 minuto passado
				self.time_check = 0
				self.TempoTotalSeg = 0
				self.TempoTotalMin+=1
		

