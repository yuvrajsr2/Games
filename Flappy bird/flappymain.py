import pygame

pygame.init()

Width, Height = 700, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("TEST")


bg = pygame.image.load('background-day.png').convert()

floorImg = pygame.image.load('base.png')
floor_x = 0

def scale(img, width, height):
    return pygame.transform.scale(img, (width, height))


def floor():
    global floor_x

    window.blit(scale(floorImg, 700, 100), (floor_x, Height - 100))
    window.blit(scale(floorImg, 700, 100), (floor_x + 600, Height - 100))

    if floor_x <= - 600:
        floor_x = 0

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(scale(bg, 700, 600), (0, 0))

    floor()
    floor_x -= 5

    pygame.display.update()
    clock.tick(60)