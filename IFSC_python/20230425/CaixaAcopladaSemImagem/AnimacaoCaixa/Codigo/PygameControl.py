#coding: utf-8

import  CaixaAcoplada as CA
import pygame as pyg
import pygame.locals as pyl
import sys

class PygameCtrl(CA.CaixaAcoplada):
    def __init__(self):
        CA.CaixaAcoplada.__init__(self)
        #Metodos pygame
        pyg.init() #Inicia o pygamae
        self._TamTela = (680, 480)
        self._CorFundo = (220, 220, 220)
        self._BIF = "../Imagens/CaixaAcoplada.png"
        self._MIF1 = "../Imagens/CursorMouse1.png"
        self._MIF2 = "../Imagnes/CursosrMouse2.png"
        self._clock = pyg.time.Clock() #aviso ao pygame que vamos usar um relógio
        self.ContTempoSeg = 0
        self.ContTempoAcumulado = 0

        self._Screen = pyg.display.set_mode(self._TamTela, 0, 32)
        self._dados_Tela()
        self._BackImage=pyg.image.load(self._BIF).convert()
        self._pygame_loop()

    def _dados_Tela(self):
        
        self.tick = self._clock.tick() #Faz a 1º marcação de tempo. Inicia o relógio.
       
        #Criação do relógio
        self._RetanguloRelogio = pyg.draw.rect(self._Screen, (255,255,255), pyg.Rect((410, 405),(240,40)))
        FontTempoOperacao = pyg.font.SysFont("Arial", 15)
        self.ContTempoAcumulado+=self.tick
        print(self.ContTempoSeg)
        self.ContTempoSeg = self.ContTempoAcumulado/1000 #Marca o tempo em segundos
        self.ContTempoMin = (self.ContTempoAcumulado/1000)/60
        self.TempoMin =1
        self.TempoSeg = 1
        TextoTempo = "{0:02d}:{1:02d}".format(int(self.ContTempoMin), int(self.ContTempoSeg))
        TextoTempo = FontTempoOperacao.render(TextoTempo, True, (0,0,0))
        self._Screen.blit(TextoTempo, (440,250))


    def _pygame_loop(self):
        while True:
            for event in pyg.event.get():
                if event.type == pyl.QUIT:
                    pyg.quit()
                    sys.exit(1)
            self._Screen.fill(self._CorFundo)
            self._Screen.blit(self._BackImage, [10,10])
            self._dados_Tela()
            print(pyg.mouse.get_pos)
            pyg.display.update()