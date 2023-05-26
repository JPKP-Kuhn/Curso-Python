#-*- coding: utf-8  -*-

import os
import pygame

class Malha: 
	def __init__(self, colunas, linhas, compr_bloco, altura_bloco, resTela, PanoFundoEnd):
		self.placar = 0
		self.game_over = False

		self.bloco_largura = compr_bloco
		self.bloco_altura = altura_bloco

		self.area_comprimento = colunas * self.bloco_largura
		self.area_altura = linhas * self.bloco_altura

		self.min_coord = ((resTela[0] - self.area_comprimento - 80),(resTela[1] - self.area_altura) / 2)
        
		self.max_coord = (self.min_coord[0] + self.area_comprimento,self.min_coord[1] + self.area_altura)

        
		self.coord_centro = (self.min_coord[0] + (colunas // 2) * self.bloco_largura,
                             self.min_coord[1] + self.bloco_altura)

		self.colunas = colunas
		self.linhas = linhas
        # Cria matriz com linhas x colunas 
		self.trama = [[-1 for i in range(self.colunas)] for j in range(self.linhas)]

		self.PanoFundo = pygame.image.load(PanoFundoEnd).convert()
		self.PanoFundo = pygame.transform.scale(self.PanoFundo, (self.area_comprimento, self.area_altura))
		self.PanoFundo.set_alpha(200)
		

	def get_coord_centro_tela(self):
		return self.coord_centro


	def violaFronteira(self, tetromino_coords):
		for x, y in tetromino_coords:
			if x > self.max_coord[0] - self.bloco_largura or x < self.min_coord[0]:
				return True
		return False		

	def sobrepoe(self, tetromino_coords):
		lista_indices = self.convert_coords(tetromino_coords)

		for linha_indice, coluna_indice in lista_indices:
			if linha_indice >= self.linhas or self.trama[linha_indice][coluna_indice] >= 0:
				return True
		return False		


	def convert_coords(self, coords):
		lista_indices = []
		for coord in coords:
			coluna_indice = int((coord[0] - self.min_coord[0]) // self.bloco_largura)#Aqui entra o uso de floor division para evitar parte inteira			
			linha_indice = int((coord[1] - self.min_coord[1]) // self.bloco_altura)
			lista_indices.append((linha_indice, coluna_indice))
		return lista_indices	


	def mostra_Mensagem(self, Tela, font, color, message):
		text_surface = font.render(str(message), True, color).convert_alpha()
		text_x = self.min_coord[0] + (self.area_comprimento - text_surface.get_width()) / 2
		text_y = (self.min_coord[1] + self.area_altura) / 2
		Tela.blit(text_surface, (text_x, text_y))
		pygame.display.flip()	

	def is_game_over(self):
		return self.game_over

	def get_placar(self):
		return self.placar	





	def mostrador(self, Tela, color_blocks, invis):
		Tela.blit(self.PanoFundo, self.min_coord)
		for i in range(self.linhas):
			for j in range(self.colunas):
				if self.trama[i][j] >= 0:  
					
					color_index = self.trama[i][j]
					coord_x = self.min_coord[0] + j * self.bloco_largura
					coord_y = self.min_coord[1] + i * self.bloco_altura
					if invis==False:
						Tela.blit(color_blocks[color_index], (coord_x, coord_y))						
					

	def get_coord_bloco_aux(self, tetromino_coords):
		lista_indices = self.convert_coords(tetromino_coords)
		bottom = False
		sobrepoe = False
		#Posicao na ultima linha.
		for linha_indice, coluna_indice in lista_indices:
			if linha_indice >= self.linhas - 1:
				return tetromino_coords

		while not bottom and not sobrepoe:			
			for i in range(len(lista_indices)):
				linha_indice, coluna_indice = lista_indices[i]
				lista_indices[i] = (linha_indice + 1, coluna_indice)
				if self.trama[linha_indice + 1][coluna_indice] >= 0:
					sobrepoe = True
				elif linha_indice + 1 >= self.linhas - 1:
					bottom = True

		if sobrepoe:
			i = 0
			for linha_indice, coluna_indice in lista_indices:
				lista_indices[i] = (linha_indice - 1, coluna_indice)
				i += 1
		return self.conversor_indice(lista_indices)		
		#Chama funcao para converter indices


	def conversor_indice(self, indices):	
		coords_lista = []
		for index in indices:
			x = int(index[1] * self.bloco_largura + self.min_coord[0])
			y = int(index[0] * self.bloco_altura + self.min_coord[1])
			coords_lista.append((x, y))
		return coords_lista	
  

	def atualizar(self, coords, color_index, avancalinha):
		#trama é a malha por onde percorre cada um dos tetrominos
		lista_indices = self.convert_coords(coords)
		for linha_indice, coluna_indice in lista_indices:
			if linha_indice >= 0 and coluna_indice >= 0:
				self.trama[linha_indice][coluna_indice] = color_index

		# verifica linha completa
		for linha_indice, coluna_indice in lista_indices:
			if linha_indice == 0:  
				self.game_over = True
				avancalinha = True

			linha_completa = True
			for j in range(self.colunas):
				if self.trama[linha_indice][j] == -1:  
					linha_completa = False
					break

			
			if linha_completa:
				del self.trama[linha_indice]
				self.placar += 1				
				self.trama.insert(0, [-1 for i in range(self.colunas)])	
				avancalinha = True

	def get_coord_centro(self):
		return self.coord_centro
