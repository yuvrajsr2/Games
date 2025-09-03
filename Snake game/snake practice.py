import pygame
from pygame.math import Vector2
import random

pygame.init()

cell_size = 20
cell_num = 40

window = pygame.display.set_mode((cell_size * cell_num, cell_num * cell_size))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(120)
    pygame.display.update()
