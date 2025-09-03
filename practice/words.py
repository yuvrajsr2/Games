import pygame

pygame.init()

Width, Height = 500, 500
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("TEST")


x, y = 250, 200
width, height = 50, 50


def display():
    pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.init():
            running = False

    display()

    pygame.display.update()