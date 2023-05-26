#-*- coding: utf-8  -*-

import os
import pygame

class Menu:
    def __init__(self, titulo, PanoFundoMenu, Resolucao_tela, fonte):
        self.titulo = titulo
        self.PanoFundo = pygame.image.load(PanoFundoMenu).convert()
        self.PanoFundo = pygame.transform.scale(self.PanoFundo, Resolucao_tela)
        self.itens = []
        self.margem_y = 50 # marca espaco entre itens no eixo y
        self.item_escolhido = 0
        self.Fonte_titulo =  pygame.font.Font(fonte, 60)
        self.Fonte_subtitulo =  pygame.font.Font(fonte, 45)
        self.Coord_Titulo = (Resolucao_tela[0]/2, Resolucao_tela[1]/40+self.margem_y)  #Em tupla para nao ser alterado
        self.cor_texto = (0, 0, 0)
        self.cor_usada = (255, 12, 12)

    def PrepEscrita(self, font,message, color):
        text = font.render(str(message), True, color)
        text = text.convert_alpha() 
        return text       

    def mostra_tela(self, tela_modo): 
        tela_modo.blit(self.PanoFundo, (0, 0))
        title_surface = self.PrepEscrita(self.Fonte_titulo, self.titulo, self.cor_texto)
        tela_modo.blit(title_surface, (self.Coord_Titulo[0] - title_surface.get_width()/2, self.Coord_Titulo[1]))

        # blit menu items
        inicial_y = self.margem_y  
        for i in range(len(self.itens)):
            if i == self.item_escolhido:
                cor = self.cor_usada
            else:
                cor = self.cor_texto

            item_surface = self.PrepEscrita(self.Fonte_titulo, self.itens[i], cor)
            tela_modo.blit(item_surface, (self.Coord_Titulo[0] - item_surface.get_width()/2, self.Coord_Titulo[1] + inicial_y))
            inicial_y += self.margem_y

    def verificaAcao(self,event):        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if self.item_escolhido== 0: #Primeira acao é sempre nula
                self.item_escolhido = len(self.itens) - 1  
                              
            else:
                self.item_escolhido -= 1    #Dimiui uma 
                
                
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self.item_escolhido = (self.item_escolhido + 1) % len(self.itens)
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            
            return self.itens[self.item_escolhido]
        
        return None





    def add_item(self, item):
        self.itens.append(item)
        
