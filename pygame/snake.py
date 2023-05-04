import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def pontuacao(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto = fonte.render(mensagem, True, cor)
    return texto

score = 0
texto_pontos = pygame.Surface((520,30))
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)] #a cobra e uma lista de segmentos, tupla com valor de x e y pra mostrar onde tá o quadrado
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    screen.fill((220, 220, 220))

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score += 1
        texto_pontos = pontuacao(pontuacao, 40, (255,255,255))
        print(score)

    screen.blit(texto_pontos, (520, 30))
    

    #pro resto do corpo acompanhar
    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #direções, snake[0] seria a cabeça da cobra
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] -10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] +10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    screen.fill((0,0,0)) #limpar a tela
    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos) #sprite, com um quadro 10,10

    pygame.display.update()