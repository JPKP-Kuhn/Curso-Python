#coding: utf-8
import sys
import pygame
from pygame.locals import* #abrir imagem

TamTela = (640,480) #tamanho da tela do pygame horizontal/vertical, funcionará em qualquer computador
screen = pygame.display.set_mode(TamTela, 0, 32) #Criação da superfície inicial, (tamanho, onde inicia, frames/segundo (acima de 24 tem ilusão de movimento))
Cor_Fundo = (200,200,200) #Padrão RGB, cinza claro
BIF1 = "IFSC_python/20230404/Imagens/CaixaAcoplada.png" #Background Image Figure
MIF1 = "IFSC_python/20230404/Imagens/CursorMouse1.png" #MIF Mouse image file
back = pygame.image.load(BIF1).convert() #Background, convert pro pygame já deixar ela guardada pra agilizar o processo
mouse = pygame.image.load(MIF1).convert_alpha()
MIF1_width=mouse.get_rect().width
MIF1_height=mouse.get_rect().height
# print("Posição X: ", MIF1_width, "Posição Y: ", MIF1_height) #Vai ser a posição da figura do mouse, seu tamanho

#Diminuindo o tamanho do mouse
mouse=pygame.transform.scale(mouse, (MIF1_width*0.25, MIF1_height*0.25))
pygame.mouse.set_visible(False)

print("Tamanho do background: ", mouse.get_width(), mouse.get_height())

clock = pygame.time.Clock() #Inicia um relógio com tempo zero.

#Posições das retas
x_i=110
y_i=240
y_aux = y_i
lim_y_cima=300
PreencheX=[]
PreencheY=[]
#tempo_passado = clock.tick() #marquei o tempo inicial
tempo_acumulado = 0
tempo_passado_segundos = 0
Check_tempo=0
veloc = -30



while True: #1000/32 tempo em milissegundos para mostrar a tela, o computador em regra faz 1000 operações/s, são 32 frames
    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit() #botão pra fechar a tela
            sys.exit(1)
    tempo_passado=clock.tick()
    tempo_passado_segundos += tempo_passado/500
    if (Check_tempo==(int(tempo_passado_segundos)-1)):
        Check_tempo = int(tempo_passado_segundos)
        print(Check_tempo, "segundos")
        y_aux -= 3
        PreencheX.append(x_i)
        PreencheY.append(y_aux)

        pygame.draw.line(screen, (0, 0, 250), (x_i,y_i), (x_i+150,y_aux)) #superfície, cor, posição inicial e final
    tempo_passado = clock.tick()

    screen.fill(Cor_Fundo)
    screen.blit(back, (10,10)) #Colar a superfície de backgrond na posição (10, 10)
    x,y = pygame.mouse.get_pos() #Obtem a posição do mouse dentro da janela do pygame a cada loop (1000 loops/segundo)
    #x-=mouse.get_width()/2 #posiciona metade da figura do mouse
    #y-=mouse.get_height()/2
    x-=4
    y-=5
    screen.blit(mouse, (x, y))
    
    tempo_passado = clock.tick()
    for i in range(len(PreencheX)):
         pygame.draw.line(screen, (0, 0, 250), (x_i+120,PreencheY[i]-veloc/2), (x_i-30,PreencheY[i]-1.5*veloc)) #superfície, cor, posição inicial e final
    tempo_passado = clock.tick()


    pygame.display.update()



