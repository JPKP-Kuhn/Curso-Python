#coding: utf-8
import pygame as p


class PygameCtrl():
	def __init__(self):
		self._cor_fundo=(200,200,200)
		self._tam_tela = (640,480)
		self._BIF1 = "Imagens/CaixaAcoplada.png"
		self._Botao1Imagem = "Imagens/botao1.png"
		self._Botao2Imagem = "Imagens/botao2.png"
		
		self._MIF1 = "Imagens/CursorMouse.png"

		self.initPygame()

	def _initPygame(self):
		pygame.init()
		self.Screen = p.display().set_mode(self._tam_tela, 0, 32)
		self.BackImage = p.image.load(self._BIF1).convert()
		self.MouseImage = p.image.load(self._MIF1).convert_alpha()
		self.screen.fill(self._cor_fundo)

		self.Botao1 = p.image.load(self._Botao1Imagem).convert_alpha()
		self.Botao1b = p.image.load(self._Botao1Imagem).convert()
		self.Botao2 = p.image.load(self._Botao2Imagem).convert()
		Botao_largura = self.Botao1.get_rect().width
		Botao_altura = self.Botao1.get_rect().height
		self.Botao1=p.transform.scale(self.Botao1, (Botao_largura*0.08, Botao_altura*0.08))

if __name__=="__main__":
	Jogo1 = PygameCtrl()
