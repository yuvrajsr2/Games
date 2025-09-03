import pygame, sys


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.x = 100
        self.y = 100
        self.sprites.append(pygame.image.load('Walk_Down_1.png'))
        self.sprites.append(pygame.image.load('Walk_Down_2.png'))
        self.sprites.append(pygame.image.load('Walk_Down_3.png'))
        self.sprites.append(pygame.image.load('Walk_Down_4.png'))
        self.sprites.append(pygame.image.load('Walk_Down_5.png'))
        self.sprites.append(pygame.image.load('Walk_Down_6.png'))
        self.sprites.append(pygame.image.load('Walk_Down_7.png'))
        self.sprites.append(pygame.image.load('Walk_Down_8.png'))
        self.sprites.append(pygame.image.load('Walk_Down_9.png'))
        self.sprites.append(pygame.image.load('Walk_Down_1.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def attack(self):
        self.attack_animation = True

    def update(self, speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0

            self.y += 1

            self.rect = self.image.get_rect()
            self.rect.topleft = [self.x, self.y]


        self.image = self.sprites[int(self.current_sprite)]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player()
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.attack()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.attack_animation = False
                player.current_sprite = 0

    # Drawing
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.50)
    pygame.display.flip()
    clock.tick(60)
