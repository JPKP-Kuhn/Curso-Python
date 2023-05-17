#coding: utf-8
import pygame as pyg

class Basics():
	def _ConstantesPygame(self):
		self._TamTela=(680,480)   
		self._CorFundo = (220,220,220)
		self._BIF = "../Imagens/CaixaAcoplada.png"
		self._MIF1 = "../Imagens/CursorMouse1.png"
		self._MIF2 = "../Imagens/CursorMouse2.png"
		self._BotaoLigaDesl = "../Imagens/BotaoOnOff.jpg"
		
	def _ControleTempo(self):
		self.clock = pyg.time.Clock()	
			#aviso ao pygame que vamos ter um relogio.
		self.ContTempoSeg = 0
		self.ContTempoMin = 0
		self.ContTempoAcumulado = 0
				

	def _Cronometro(self): 
		TextoTempoOperacao = self.FontArial15.render("Tempo de operação: ", self.SurfDados, True, (255,255,255))		
			#Transforma o texto em figura.
		self.SurfDados.blit(TextoTempoOperacao,(15,360))	
		
		self.tick = self.clock.tick()	#Faz a primeira marcacao de tempo em milissegundos.Inicia o relogio.	
		self.ContTempoAcumulado+=self.tick #Acumulo os milissegundos
		self.ContTempoSeg = int(self.ContTempoAcumulado/1000)
		if(self.ContTempoAcumulado>=60*1000):
			self.ContTempoAcumulado=0
			self.ContTempoMin+=1
			self.ContTempoSeg=0		
		TextoTempo = "{0:02d}:{1:02d}".format(int(self.ContTempoMin), int(self.ContTempoSeg))
		self.TextoTempo = self.FontArial15.render(TextoTempo, True, (0,0,0))

				
		
	
		
		
