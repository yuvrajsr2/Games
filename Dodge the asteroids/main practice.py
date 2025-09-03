import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST")


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False










"""
import pygame

pygame.init()

Width, Height = 800, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("TEST")


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        image = pygame.image.load(path)
        self.image = pygame.transform.scale(image, (80, 60))
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.boundary()

    def boundary(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= Width:
            self.rect.right = Width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Height:
            self.rect.bottom = Height

spaceship = SpaceShip('spaceship.png', 400, 450, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.mouse.set_visible(False)
    window.fill((42, 45, 51))

    spaceship_group.draw(window)
    spaceship_group.update()
    pygame.display.update()
    clock.tick(120)


pygame.QUIT()
"""