import pygame

pygame.init()

Width = 800
Height = int(Width * 0.8)

window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("HI")


# define player action variables
moving_left = False
moving_right = False

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        super().__init__()
        img = pygame.image.load('img/player/Idle/0.png')
        self.image = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self):
        window.blit(self.image, self.rect)

player = Soldier(200, 200, 3)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_ESCAPE:
                running = False


    player.draw()

    pygame.display.update()
    clock.tick(60)