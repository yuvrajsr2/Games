import random
import pygame

pygame.init()

Width, Height = 1000, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Space Invaders")

score = 0
score_font = pygame.font.Font('freesansbold.ttf', 60)
x, y, width, height = 10, 10, 200, 25
valid = False
high_score = 0


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

        self.boundary()

    def boundary(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= Width:
            self.rect.right = Width
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= Height:
            self.rect.bottom = Height

        if self.rect.bottom >= 700:
            self.kill()


class Alien(pygame.sprite.Sprite):
    def __init__(self, img, x, y, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(center=(x, y))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed


class Laser(pygame.sprite.Sprite):
    def __init__(self, img, pos, speed):
        super().__init__()
        # Loading the image and giving it a pos
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(center=pos)
        # Creating a attribute of speed parameter
        self.speed = speed

    def update(self):
        # Moving the laser up by speed
        self.rect.centery -= self.speed


spaceship = SpaceShip('player.png', 300, 300)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

alien_group = pygame.sprite.Group()
alien_event = pygame.USEREVENT
pygame.time.set_timer(alien_event, 100)

laser_group = pygame.sprite.Group()

clock = pygame.time.Clock()
running = True
while running:

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == alien_event:
            image = 'enemy.png'
            x_pos = random.randrange(0, 1000)
            y_pos = random.randrange(-500, -50)
            x_move = random.randrange(-1, 1)
            y_move = random.randrange(4, 10)
            alien = Alien(image, x_pos, y_pos, x_move, y_move)
            alien_group.add(alien)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_laser = Laser('bullet.png', mouse, 15)
                laser_group.add(new_laser)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if valid is False:
                if 400 <= mouse[0] <= 600 and 300 <= mouse[1] <= 350:
                    valid = True
                    width = 200
                    alien_group.empty()
                    laser_group.empty()
                    score = 0

    window.fill((0, 0, 0))
    if valid is False:
        button_text = score_font.render("Start", True, (255, 255, 255))
        pygame.draw.rect(window, (255, 60, 0), (400, 300, 200, 50))
        window.blit(button_text, (425, 300))

    pygame.draw.rect(window, (255, 0, 0), (x, y, 200, 25))
    pygame.draw.rect(window, (0, 255, 0), (x, y, width, height))

    if width <= 0:
        valid = False

    score_text = score_font.render(f'Score: {score}', True, (255, 255, 255))
    window.blit(score_text, (700, 20))

    if valid:
        laser_group.draw(window)
        laser_group.update()

        spaceship_group.draw(window)
        spaceship_group.update()

        alien_group.draw(window)
        alien_group.update()

        if pygame.sprite.spritecollide(spaceship_group.sprite, alien_group, True):
            width -= 20

        for laser in laser_group:
            if pygame.sprite.spritecollide(laser, alien_group, True):
                score += 1

    clock.tick(60)
    pygame.display.update()
