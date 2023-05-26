#coding: utf-8
		
import pygame as pyg
import pygame.locals as pyl
import sys

class SurfDados():  
	def SurfDados(self):	#Observar que nao é funcao construtora 
		self.SurfDados = pyg.Surface([260,400])	#Cria superficie para área de dados
		self.SurfDadosCor = (120,120,120)		#cinza escuro
		self.Branco = (255,255,255)				#Cor Branca		
		self.BotaoLiga = 1	#0-off	1-on	Ativacao do botao liga. 
		self.BotaoLigaCtrl = False
		self.BotaoDesliga = 0 #0-off	1-on	Ativacao do botao desliga.	

		#Retângulos de informacoes:	
		self.FontA15 = pyg.font.SysFont('Arial', 15)		

		
		
		
	def SurfDados_Prep(self):		
		self.SurfDados.fill(self.SurfDadosCor)	#pinta a superficie.
		self._visor_tempo_operacao()	#Insere o visor do relogio.	
		self._retangulo_processo()		#insere o visor do processo.				
		self._retangulo_botao_liga_desl()	#Insere botao liga-desliga
		self._visor_Atividade_Caixa()		
		
		
		
	'''
	Define o retângulo que mostra o processo em operação.
	'''
	def _retangulo_processo(self): 
		self.RetanguloProcesso = pyg.Rect((10,150),(240,140))	#Pos Entrada, dimensoes.	
		self.RetProcesso = pyg.draw.rect(self.SurfDados, self.Branco, self.RetanguloProcesso) 
			#Blit do retangulo na tela.		 
		Texto_Processo = "Processo: "
		if (self.Estado ==0): 
			Texto_Processo+="Caixa vazia ociosa."
		elif (self.Estado==1): 
			Texto_Processo+="Caixa enchendo"	
		elif (self.Estado==2): 
			Texto_Processo+="Caixa cheia d'água"	
		elif (self.Estado==3): 
			Texto_Processo+="Caixa esvaziando"	
		elif (self.Estado==4): 
			Texto_Processo+="Caixa em manutenção"			
		Texto_Processo = self.FontA15.render(Texto_Processo, True, (0,0,0))	#Cria imagem do texto
		self.SurfDados.blit(Texto_Processo, (15,160))	#Blit do texto na posicao
		
		
	'''
	Prepara regiao para insercao do visor de tempo de operação.
	'''				
	def _visor_tempo_operacao(self):	
		#Criação do retângulo:	
		self.RetanguloTempo = pyg.Rect((10,350),(240,40))	#Pos Entrada, dimensoes.		
		self.RetTempo = pyg.draw.rect(self.SurfDados,(255,255,255), self.RetanguloTempo)
				#Blit do retangulo de tempo na tela. 					
		TextoTempoOperacao = self.FontA15.render('Tempo de operação:', True, (0,0,0))		
		self.SurfDados.blit(TextoTempoOperacao, (15, 360)) #Blit do texto
		TextoTempoOperacao = self.FontA15.render('Tempo de operação:', True, (0,0,0))		
		self.SurfDados.blit(TextoTempoOperacao, (15, 360)) #Blit do texto
		TextoTempo = "{0:02d} : {1:02d}".format(self.TempoTotalMin, self.TempoTotalSeg)
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
	
	'''
	Prepara regiao para insercao do botao de liga desliga.
	'''		
	def _retangulo_botao_liga_desl(self): 
		self.StartImage =pyg.image.load(self.OnOffImage).convert_alpha()
		self.StartImageDark =pyg.image.load(self.OnOffImageDark).convert_alpha()			
		reducao = 15	#Taxa de reducao da figura do botao de liga/desliga. 
		base = self.StartImage.get_width()
		altura = self.StartImage.get_height()
		self.StartImage=pyg.transform.scale(self.StartImage,(base/reducao,altura/reducao))
		self.StartImageDark=pyg.transform.scale(self.StartImageDark,(base/reducao,altura/reducao))
		
		#Cria retângulo para inserção do botao de liga
		self.retImageOnButton = pyg.Rect((0,0),(self.StartImage.get_width()/2,
				self.StartImage.get_height()))
		self.retImageOffButton = pyg.Rect((self.StartImage.get_width()/2+2,0),(self.StartImage.get_width()+2,
				self.StartImage.get_height()))		
										
		if 	(self.Estado == 0): 	#Caixa nao iniciada. 			
			#mouse dentro do quadrado para acionar a caixa muda para maozinha.
			if (400<pyg.mouse.get_pos()[0]<450 and 32<pyg.mouse.get_pos()[1]<75):
				self.MouseFlag=False	#Orienta o mouse a virar mãozinha.								
				if (self.MouseClicked==True):
					self.Estado =1	#A caixa passa para regime de enchimento.
					self.MouseFlag=True
					self.cronometro = True					
				self.SurfDados.blit( self.StartImage, (5,5), self.retImageOnButton )				
			else:
				self.MouseFlag=True
				self.SurfDados.blit( self.StartImageDark, (5,5), self.retImageOnButton )					
		elif(self.Estado==1):
			self.SurfDados.blit( self.StartImage, (5,5), self.retImageOnButton )					
		elif(self.Estado==2):
			 self.SurfDados.blit( self.StartImage, (5,5), self.retImageOffButton )
		elif(self.Estado==3): 
			self.SurfDados.blit( self.StartImage, (5,5), self.retImageOffButton )	 
		elif(self.Estado==4): #Esvaziar a caixa e mandar para manutenção.
			self.SurfDados.blit( self.StartImageDark, (5,5), self.retImageOffButton )
		
		self.MouseClicked = False	#desmarca o clique.	
		self._visor_Atividade_Caixa()	#Escreve no visor a opcao de ligar/Desligar
		
		
						
	def _visor_Atividade_Caixa(self):		
		self.retImageOnOffButton = pyg.Rect((0,0),(self.StartImage.get_width()/2,
				self.StartImage.get_height()))			
		#Fontes usadas:
		fonteBase = pyg.font.SysFont('Arial', 16)	
		if(self.Estado==0):
			if(self.MouseFlag==True): 
				Caixa = fonteBase.render('Clique para iniciar a caixa', True, (255,255,255))	#Branco				
				#self.SurfDados.blit( self.StartImage, (5,5), self.retImageOnButton )
			else:
				Caixa = fonteBase.render('Clique para iniciar a caixa', True, (155,200,100))	#Verde musgo
				#self.SurfDados.blit( self.StartImage, (5,5), self.retImageOnButton )
				#self.MouseFlag =True	#Passa mouse para maozinha.				
		elif(self.Estado==4): 
			Caixa = fonteBase.render('Caixa em manutenção', True, (255,255,255))
		elif(self.Estado==3): 
			Caixa = fonteBase.render("Desativar Caixa", True, (255,255,255))	#Caixa pode ser desativada se estiver cheia.
		else:
			if(self.DesativarCaixa==False): 
				Caixa= fonteBase.render('Caixa em uso', True, (255,255,255))
			else:
				Caixa = fonteBase.render('Desativar caixa', True, (255,255,255))
				
		self.SurfDados.blit(Caixa, (65, 10))		

