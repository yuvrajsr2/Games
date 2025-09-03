import pygame

pygame.init()

Width, Height = 800, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Client")


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color


def redrawWindow():
    window.fill((255, 255, 255))


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    redrawWindow()

    clock.tick(60)
    pygame.display.update()
