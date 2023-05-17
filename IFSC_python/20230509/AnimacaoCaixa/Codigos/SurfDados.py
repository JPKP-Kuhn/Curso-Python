import pygame as pyg

class SurfDados():
    def SurfDados_definicao(self):
        self.SurfDados = pyg.Surface([260,400]) 
			#Define o tamanho da superficie
        self.SurfDadosCor = (120,120,120) #Cinza fraco
        self.Branco = (255, 255, 255)
        self.SurfDados.fill(self.SurfDadosCor)
        self.RetanguloGrande = pyg.Rect((10,350),(240,40))
        self.RetanguloEstado = pyg.Rect((120,5),(120,40))

        #Fontes usadas
        self.FontArial15 = pyg.font.SysFont("Arial", 15)

        #Imagem do botao liga-desliga
        self.ImagemLigaDesl = pyg.image.load(self._BotaoLigaDesl).convert_alpha()
        altura = self.ImagemLigaDesl.get_height()
        comprimento = self.ImagemLigaDesl.get_width()
        reducao = 15
        self.ImagemLigaDesl=pyg.transform.scale(self.ImagemLigaDesl, (comprimento/reducao, altura/reducao))
        #Retângulo do botao liga desl
        self.retanguloIMagemBotaLiga=pyg.Rect((0,0), (self.ImagemLigaDesl.get_width(), self.ImagemLigaDesl.get_height()))
        self.retanguloImagemBotaoDesl=pyg.Rect(self.ImagemLigaDesl.get_width()/2.0), (self.ImagemLigaDesl.get_width()/2,self.ImagemLigaDesl.get_height())

        #self.ImagemLiga = pyg.draw.rect(self.retanguloIMagemBotaLiga)
        self.SurfDados.blit(self.ImagemLigaDesl, (5,5))

    def _SurfDados_atualizacao(self):
        self.RetanguloRelogio = pyg.draw.rect(self.SurfDados , (255,255,255),self.RetanguloGrande)
        if (self._Estado==0):
            texto_estado = "Caixa Vazia"
        elif (self._Estado==1):
            texto_estado = "Caixa enchendo"
        elif self._Estado==2:
            texto_estado = "Caixa cheia"
        elif self._Estado==3:
            texto_estado = ""

        texto_estado = self.FontArial15.render(texto_estado, True, (0,0,0))

        self.RetanguloEstado = pyg.draw.rect(self.SurfDados , (255,255,255),self.RetanguloEstado)
        self.SurfDados.blit(texto_estado, (120,13))

        self._Cronometro()
        self.SurfDados.blit(self.TextoTempo, (160,360))	
