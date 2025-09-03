# Imports
import pygame
import time
import math
from utils import scale, blit_rotate

# Initialize
pygame.init()

# Constants
GRASS = scale(pygame.image.load('imgs/grass.jpg'), 2)
TRACK = scale(pygame.image.load('imgs/track.png'), 0.75)

TRACK_BORDER = scale(pygame.image.load('imgs/track-border.png'), 0.75)
FINISH = pygame.image.load('imgs/finish.png')

RED_CAR = scale(pygame.image.load('imgs/red-car.png'), 0.5)
GREEN_CAR = scale(pygame.image.load('imgs/green-car.png'), 0.5)

# Screen
Width, Height = TRACK.get_width(), TRACK.get_height()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Racing game")


# Abstract car class
class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    # Rotate method
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    # draw method
    def draw(self, win):
        blit_rotate(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def slow_down(self):
        pass



# Player Car class inherits from Abstract car
class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (150, 180)


# Draw function draws the images
def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(screen)
    pygame.display.update()


# Images list
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
# Calling Player Car class in player_car var
player_car = PlayerCar(4, 4)


# Game loop
clock = pygame.time.Clock()
fps = 60
running = True
while running:
    clock.tick(fps)

    # Call the draw func
    draw(screen, images, player_car)

    # Event to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Keys to rotate the car
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        player_car.move_forward()

pygame.quit()
