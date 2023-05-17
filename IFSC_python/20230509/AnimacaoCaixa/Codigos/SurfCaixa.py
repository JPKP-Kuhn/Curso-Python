#coding: utf-8
import pygame as pyg

class SurfCaixa():
    def SurfCaixa_definicao(self):
        self.SurfCaixa=pyg.Surface([378,456])
        self._BackImage=pyg.image.load(self._BIF).convert()
        self.SurfCaixa.blit(self._BackImage, [0,0])

    def _SurfDados_atualizacao():
        pass