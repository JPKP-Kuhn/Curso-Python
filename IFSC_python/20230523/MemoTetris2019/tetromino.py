#-*- coding: utf-8  -*-
from random import randint


class Tetromino:
 
    i_tetromino_angulo_0 = ["....",
                           "####",
                           "....",
                           "...."]

   
    i_tetromino_angulo_90 = [".#..",
                            ".#..",
                            ".#..",
                            ".#.."]

    i_tetromino = (i_tetromino_angulo_0, i_tetromino_angulo_90,
                   i_tetromino_angulo_0, i_tetromino_angulo_90)

    # O tetromino
    o_tetromino_angulo_0 = ["##..",
                           "##..",
                           "....",
                           "...."]

    o_tetromino = (o_tetromino_angulo_0, o_tetromino_angulo_0,
                   o_tetromino_angulo_0, o_tetromino_angulo_0)

    # T tetromino
    t_tetromino_angulo_0 = [".#..",
                           "###.",
                           "....",
                           "...."]


    t_tetromino_angulo_90 = [".#..",
                            ".##.",
                            ".#..",
                            "...."]


    t_tetromino_angulo_180 = ["....",
                             "###.",
                             ".#..",
                             "...."]


    t_tetromino_angulo_270 = [".#..",
                             "##..",
                             ".#..",
                             "...."]

    t_tetromino = (t_tetromino_angulo_0, t_tetromino_angulo_90,
                   t_tetromino_angulo_180, t_tetromino_angulo_270)


    j_tetromino_angulo_0 = ["#...",
                           "###.",
                           "....",
                           "...."]


    j_tetromino_angulo_90 = [".##.",
                            ".#..",
                            ".#..",
                            "...."]


    j_tetromino_angulo_180 = ["....",
                             "###.",
                             "..#.",
                             "...."]


    j_tetromino_angulo_270 = [".#..",
                             ".#..",
                             "##..",
                             "...."]

    j_tetromino = (j_tetromino_angulo_0, j_tetromino_angulo_90,
                   j_tetromino_angulo_180, j_tetromino_angulo_270)


    l_tetromino_angulo_0 = ["..#.",
                           "###.",
                           "....",
                           "...."]


    l_tetromino_angulo_90 = [".#..",
                            ".#..",
                            ".##.",
                            "...."]

    l_tetromino_angulo_180 = ["....",
                             "###.",
                             "#...",
                             "...."]

    l_tetromino_angulo_270 = ["##..",
                             ".#..",
                             ".#..",
                             "...."]
    l_tetromino = (l_tetromino_angulo_0, l_tetromino_angulo_90,
                   l_tetromino_angulo_180, l_tetromino_angulo_270)

   
    s_tetromino_angulo_0 = [".##.",
                           "##..",
                           "....",
                           "...."]

    
    s_tetromino_angulo_90 = [".#..",
                            ".##.",
                            "..#.",
                            "...."]

    s_tetromino = (s_tetromino_angulo_0, s_tetromino_angulo_90,
                   s_tetromino_angulo_0, s_tetromino_angulo_90)

    # Z tetromino
    z_tetromino_angulo_0 = ["##..",
                           ".##.",
                           "....",
                           "...."]

    
    z_tetromino_angulo_90 = ["..#.",
                            ".##.",
                            ".#..",
                            "...."]

    z_tetromino = (z_tetromino_angulo_0, z_tetromino_angulo_90,
                   z_tetromino_angulo_0, z_tetromino_angulo_90)

    tetrominoes = (i_tetromino, o_tetromino, t_tetromino, j_tetromino,
                   l_tetromino, s_tetromino, z_tetromino)

    DeltaVeloc = 0.03  # segundos

    def __init__(self, bloco_dimensoes, coord, Velocidade):
        self.random_indice = randint(0,6)	#Pega numero aleatorio entre 0 e 6 (7 pecas). 
        self.random_tetromino = Tetromino.tetrominoes[self.random_indice]

        self.atual_angulo = 0
        self.atual_frame = self.random_tetromino[self.atual_angulo]

        self.bloco_comprimento = bloco_dimensoes[0]
        self.bloco_altura = bloco_dimensoes[1]


        self.coord_central = list(coord)#Usado na rotacao 

        self.blocos_coord = self.Coordenada_lista()

        # tempo convertido para seg
        self.normal_Velocidade = Velocidade
        self.Velocidade = self.normal_Velocidade
        self.tempo_usado = 0.0

    def Coordenada_lista(self):
        x, y = [self.coord_central[0] - self.bloco_comprimento, self.coord_central[1]
                - self.bloco_altura]
        tetromino_coords = []

        for i in range(len(self.atual_frame)):
            for char in self.atual_frame[i]:
                if char == '#':
                    tetromino_coords.append([x, y])
                x += self.bloco_comprimento
            x = self.coord_central[0] - self.bloco_comprimento
            y += self.bloco_altura
        return tetromino_coords

    def set_coords(self, coord_central):
        self.coord_central = list(coord_central)
        self.blocos_coord = self.Coordenada_lista()

    def get_coords(self):
        return self.blocos_coord

    def get_color_index(self):
        return self.random_indice

    def aumenta_veloc(self):
        self.Velocidade = Tetromino.DeltaVeloc

    def limpa_velocidade(self):
        self.Velocidade = self.normal_Velocidade

    def set_veloc(self, Velocidade):
        self.normal_Velocidade = Velocidade
        self.Velocidade = self.normal_Velocidade

    def mostra_tetromino(self, screen, color_blocks):
      for coord in self.blocos_coord:
            screen.blit(color_blocks[self.random_indice], coord)

    def move_cima(self):
        for coord in self.blocos_coord:
            coord[1] -= self.bloco_altura
        self.coord_central[1] -= self.bloco_altura

    def move_baixo(self, time):
        self.tempo_usado += time
        if self.tempo_usado >= self.Velocidade:
            self.tempo_usado = 0
            for coord in self.blocos_coord:
                coord[1] += self.bloco_altura
            self.coord_central[1] += self.bloco_altura

    def move_esquerda(self):
        self.coord_central[0] -= self.bloco_comprimento
        for coord in self.blocos_coord:
            coord[0] -= self.bloco_comprimento

    def move_direita(self):
        self.coord_central[0] += self.bloco_comprimento
        for coord in self.blocos_coord:
            coord[0] += self.bloco_comprimento

    def rotacao_antihoraria(self):
        if self.atual_angulo == 0:
            self.atual_angulo = 3
        else:
            self.atual_angulo -= 1

        self.atual_frame = self.random_tetromino[self.atual_angulo]
        self.blocos_coord = self.Coordenada_lista()

    def rotacao_horaria(self):
        self.atual_angulo = (self.atual_angulo + 1) % 4
        self.atual_frame = self.random_tetromino[self.atual_angulo]
        self.blocos_coord = self.Coordenada_lista()
