#coding: utf-8
		
import pygame as pyg
import pygame.locals as pyl
import CaixaAcoplada as CA
#import sys

class SurfDados():
	####################### Controles Estáticos #####################
	def SurfDados(self):	#Observar que nao é funcao construtora 
		self.SurfDados_Parametros_Gerais()			
		self.SurfDados_Parametros_Botoes()
		self.SurfDados_Parametros_Retangulos()
	
	def SurfDados_Parametros_Gerais(self): 
		self.SurfDados = pyg.Surface([260,400])	#Cria superficie para área de dados
		self.SurfDadosCor = (120,120,120)		#cinza escuro
		self.Branco = (255,255,255)				
		self.Preto = (0,0,0)					
		self.VerdeMusgo = (155,200,100)			
		#Fontes utilizadas 
		self.FontA15 = pyg.font.SysFont('Arial', 15)	
		self.fonteBase = pyg.font.SysFont('Arial', 16)	
			
	
	def SurfDados_Parametros_Retangulos(self):
		self.RetanguloProcesso = pyg.Rect((10,150),(240,140))	
		self.RetanguloTempo = pyg.Rect((10,350),(240,40))	
		#Cria retângulo para inserção do botao de liga e de desliga
		self.retImageOnButton = pyg.Rect((0,0),(self.StartImage.get_width()/2,
				self.StartImage.get_height()))
		self.retImageOffButton = pyg.Rect((self.StartImage.get_width()/2+2,0),(self.StartImage.get_width()+2,
				self.StartImage.get_height()))		
		self.retImageOnOffButton = pyg.Rect((0,0),(self.StartImage.get_width()/2,
				self.StartImage.get_height()))
		self.retImageMaintenance = pyg.Rect((0,0), (self.Maintenance.get_width(),
				self.Maintenance.get_height()))
		
	
	def SurfDados_Parametros_Botoes(self):
		#Imagens
		self.OnOffImage = "../Imagens/BotaoOnOff.jpg"
		self.ManutencaoImage = "../Imagens/Manutencao.png"
		self.OnOffImageDark = "../Imagens/BotaoOnOffDark.png"
		self.OkImage = "../Imagens/DedoApontando.png"
		self.EspereImage = "../Imagens/mao_espere.png"

		#Carregando as imagens, com fundo transparente
		self.StartImage =pyg.image.load(self.OnOffImage).convert_alpha()
		self.Maintenance =pyg.image.load(self.ManutencaoImage).convert_alpha()
		self.StartImageDark =pyg.image.load(self.OnOffImageDark).convert_alpha()
		self.OkImage=pyg.image.load(self.OkImage).convert_alpha()
		self.EspereImage=pyg.image.load(self.EspereImage).convert_alpha()

		reducao = 15	#Taxa de reducao da figura do botao de liga/desliga. 
		base = self.StartImage.get_width()
		altura = self.StartImage.get_height()

		#Reconfiguração do tamanho das imagens
		self.StartImage=pyg.transform.scale(self.StartImage,(base/reducao,altura/reducao))
		self.Maintenance=pyg.transform.scale(self.Maintenance,(self.Maintenance.get_width()/5.5,self.Maintenance.get_height()/5.5))
		self.StartImageDark=pyg.transform.scale(self.StartImageDark,(base/reducao,altura/reducao))
		self.OkImage=pyg.transform.scale(self.OkImage,(self.OkImage.get_width()/12,self.OkImage.get_height()/12))		
		self.EspereImage=pyg.transform.scale(self.EspereImage,(43,43))	
	
	
	####################### Controles Dinâmicos #####################	
	def SurfDados_Prep(self):		
		self.SurfDados.fill(self.SurfDadosCor)	#pinta a superficie.
		self._visor_tempo_operacao()	#Insere o visor do relogio.	
		self._retangulo_processo()		#insere o visor do processo.		
		self._visor_Atividade_Caixa()	#Escreve no visor a opcao de ligar/Desligar
		

	def _retangulo_processo(self): 
		self.RetProcesso = pyg.draw.rect(self.SurfDados, self.Branco, self.RetanguloProcesso) 
			#Blit do retangulo na tela.	
		vol = self.VolumeCaixa/self.nlines*self._nivel_maximo	
		if self.VolumeCaixa>1:
			volumeAtual = "Volume: {:.1f} litros".format(vol)
		else: 
			volumeAtual = "Volume: {:.1f} litro".format(vol)
		volumeAtual = self.FontA15.render(volumeAtual, True, self.Preto)				 
		Texto_Processo = "Processo: "
		if (self.Estado ==0): 
			Texto_Processo+="Caixa vazia ociosa."
		elif (self.Estado==1): 
			Texto_Processo+="Caixa enchendo"
			vazaoEntrada = "Vazão de entrada: {:.1f} litro/seg".format(self._valvula._vazao_entrada)
			vazaoEntrada = self.FontA15.render(vazaoEntrada, True, self.Preto)
			self.SurfDados.blit(vazaoEntrada, (15,200))						
		elif (self.Estado==2): 
			Texto_Processo+="Caixa cheia d'água"				
		elif (self.Estado==3): 
			Texto_Processo+="Caixa esvaziando"	
			vazaoSaida = "Vazão de saída: {:.1f} litro/seg".format(self._comporta._vazao_saida)
			vazaoSaida = self.FontA15.render(vazaoSaida, True, self.Preto)
			self.SurfDados.blit(vazaoSaida, (15,200))				
		elif (self.Estado==4): 
			Texto_Processo+="Caixa em manutenção"
			vazaoSaida = "Vazão de saída: {:.1f} litro/seg".format(self._comporta._vazao_saida)		
			vazaoSaida = self.FontA15.render(vazaoSaida, True, self.Preto)
			
		Texto_Processo = self.FontA15.render(Texto_Processo, True, self.Preto)	#Cria imagem do texto
		self.SurfDados.blit(Texto_Processo, (15,160))	#Blit do texto na posicao
		self.SurfDados.blit(volumeAtual, (15,180))	
		

	def _visor_tempo_operacao(self):			
		self.RetTempo = pyg.draw.rect(self.SurfDados,self.Branco, self.RetanguloTempo)
				#Blit do retangulo de tempo na tela. 					
		TextoTempoOperacao = self.FontA15.render('Tempo de operação:', True, self.Preto)		
		self.SurfDados.blit(TextoTempoOperacao, (15, 360)) #Blit do texto
		TextoTempoOperacao = self.FontA15.render('Tempo de operação:', True, self.Preto)		
		self.SurfDados.blit(TextoTempoOperacao, (15, 360)) #Blit do texto
		TextoTempo = "{0:02d} : {1:02d}".format(self.TempoTotalMin, self.TempoTotalSeg)
		TextoTempo = self.FontA15.render(TextoTempo, True, self.Preto)		
		self.SurfDados.blit(TextoTempoOperacao, (15, 360)) #Blit do texto
		self.SurfDados.blit(TextoTempo, (160, 360)) #Blit do texto		
		if (self.cronometro): #Cronometro iniciou com o enchimento da caixa.  
			self.time_check += self.tick
			self.TempoTotalSeg = int(self.time_check/1000.)
			if (self.time_check>=(60*1000)): #1 minuto passado
				self.time_check = 0
				self.TempoTotalSeg = 0
				self.TempoTotalMin+=1
				

	def _visor_Atividade_Caixa(self):		
		if(self.Estado==0):
			if(self.MouseFlag==True): 
				Caixa = self.fonteBase.render('Clique para iniciar a caixa', True, self.Branco)	#Branco			
			else:
				Caixa = self.fonteBase.render('Clique para iniciar a caixa', True, self.VerdeMusgo)	#Verde musgo
			self.SurfDados.blit(Caixa, (65, 10))
		elif(self.Estado==1): 
			Caixa = self.fonteBase.render('Caixa enchendo', True, self.Branco)					
			self.SurfDados.blit(Caixa, (65, 10))		
		elif(self.Estado==2): 
			Caixa = self.fonteBase.render('Caixa pronta para uso', True, self.Branco)
			Caixa2 = self.fonteBase.render('Aperte a descarga na caixa', True, self.Branco)
			Caixa3 = self.fonteBase.render("Desativar a caixa", True, self.Branco)
			Caixa4 = self.fonteBase.render("para manutenção", True, self.Branco)
			self.SurfDados.blit(Caixa, (50, 15))
			self.SurfDados.blit(Caixa2, (50, 30))
			self.SurfDados.blit(Caixa3, (60, 73))
			self.SurfDados.blit(Caixa4, (60, 88))
		elif(self.Estado==3): 
			Caixa = self.fonteBase.render("Caixa Esvaziando", True, self.Branco)
				#Caixa pode ser desativada se estiver cheia.
			self.SurfDados.blit(Caixa, (60, 20))
		elif(self.Estado==4): 
			Caixa = self.fonteBase.render('Caixa em manutenção', True, self.Branco)
		else:
			if(self.DesativarCaixa==False): 
				Caixa= self.fonteBase.render('Caixa em uso', True, self.Branco)
			else:
				Caixa = self.fonteBase.render('Desativar caixa', True, self.Branco)
				
		

