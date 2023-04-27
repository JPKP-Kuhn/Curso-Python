import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update()