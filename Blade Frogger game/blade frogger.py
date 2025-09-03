# Import
import pygame
import random

# Initialize pygame
pygame.init()

# Setting up the window
Width, Height = 1000, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Blade Frogger")

road = pygame.image.load('road.png')
road1 = pygame.transform.scale(road, (280, 1000))
road2 = pygame.transform.rotate(road1, 90)


def add_num(num1=10):
    return num1 + num1


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.vel = 10
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walk_up = [pygame.image.load('Walk_Up_1.png'), pygame.image.load('Walk_Up_2.png'),
                        pygame.image.load('Walk_Up_3.png'), pygame.image.load('Walk_Up_4.png'),
                        pygame.image.load('Walk_Up_5.png'), pygame.image.load('Walk_Up_6.png'),
                        pygame.image.load('Walk_Up_7.png'), pygame.image.load('Walk_Up_8.png'),
                        pygame.image.load('Walk_Up_9.png')]

        self.walk_down = [pygame.image.load('Walk_Down_1.png'), pygame.image.load('Walk_Down_2.png'),
                          pygame.image.load('Walk_Down_3.png'), pygame.image.load('Walk_Down_4.png'),
                          pygame.image.load('Walk_Down_5.png'), pygame.image.load('Walk_Down_6.png'),
                          pygame.image.load('Walk_Down_7.png'), pygame.image.load('Walk_Down_8.png'),
                          pygame.image.load('Walk_Down_9.png')]

        self.walk_left = [pygame.image.load('Walk_Side_1.png'), pygame.image.load('Walk_Side_2.png'),
                          pygame.image.load('Walk_Side_3.png'), pygame.image.load('Walk_Side_4.png'),
                          pygame.image.load('Walk_Side_5.png'), pygame.image.load('Walk_Side_6.png'),
                          pygame.image.load('Walk_Side_7.png'), pygame.image.load('Walk_Side_8.png'),
                          pygame.image.load('Walk_Side_9.png')]

        self.current_walk_up = 0
        self.current_walk_down = 0
        self.current_walk_left = 0
        self.image = self.walk_down[0]

        # Checking if any of these is truue and if true then changing self.image
        if self.up is True:
            self.image = self.walk_up[self.current_walk_up]
        elif self.down is True:
            self.image = self.walk_down[self.current_walk_down]
        elif self.left is True:
            self.image = self.walk_left[self.current_walk_down]
        elif self.right is True:
            self.image = pygame.transform.flip(self.walk_left[self.current_walk_left], True, False)

        # Positioning it
        self.rect = self.image.get_rect
        self.rect = [self.x, self.y]

    # Update function
    def update(self, speed):
        self.move(speed)
        self.rect1 = self.image.get_rect(center=(self.x, self.y))

    # Player animation and moving it
    def move(self, speed):
        # If self.up is true then show its animation and move it up
        if self.up is True:
            self.current_walk_up += speed
            if int(self.current_walk_up) >= len(self.walk_up):
                self.current_walk_up = 0

            self.y -= 2

            self.rect = self.image.get_rect
            self.rect = [self.x, self.y]

            self.image = self.walk_up[int(self.current_walk_up)]

        # If self.down is true then show its animation and move it down
        elif self.down is True:
            self.current_walk_down += speed
            if int(self.current_walk_down) >= len(self.walk_down):
                self.current_walk_down = 0

            self.y += 2

            self.rect = self.image.get_rect
            self.rect = [self.x, self.y]

            self.image = self.walk_down[int(self.current_walk_down)]

        # If self.left is true then show its animation and move it left
        elif self.left is True:
            self.current_walk_left += speed
            if int(self.current_walk_left) >= len(self.walk_left):
                self.current_walk_left = 0

            self.x -= 2

            self.rect = self.image.get_rect
            self.rect = [self.x, self.y]

            self.image = self.walk_left[int(self.current_walk_left)]

        # If self.right is true then show its animation and move it right
        elif self.right is True:
            self.current_walk_left += speed
            if int(self.current_walk_left) >= len(self.walk_left):
                self.current_walk_left = 0

            self.x += 2

            self.rect = self.image.get_rect
            self.rect = [self.x, self.y]

            self.image = pygame.transform.flip((self.walk_left[int(self.current_walk_left)]), True, False)
        # If none are true then reset the player
        else:
            self.image = self.walk_down[0]
            self.current_walk_down = 0
            self.current_walk_up = 0
            self.current_walk_left = 0


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, x1, y1):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load('Yellow1.png')
        self.image1 = pygame.transform.flip(pygame.image.load('Grey1.png'), True, False)
        self.rect = self.image.get_rect(center=(x, y))
        self.rect1 = self.image1.get_rect(center=(x1, y1))

    def update(self):
        window.blit(self.image, self.rect)
        window.blit(self.image1, self.rect1)

        self.rect.centerx -= self.speed
        self.rect1.centerx += self.speed

        self.collision()

    def collision(self):
        if self.rect1.colliderect(player.rect1):
            print("Boom")
        if self.rect.colliderect(player.rect1):
            print("Boom")

        if self.rect.centerx < -70 and self.rect1.centerx > 1040:
            self.kill()


# Draw function
def draw():
    window.blit(road2, (0, 60))


# Player Group
player = Player(500, 300)
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

car_group = pygame.sprite.Group()
car_event = pygame.USEREVENT

pygame.time.set_timer(car_event, 3000)

# Game loop

clock = pygame.time.Clock()
running = True
while running:

    # Getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == car_event:
            car = Car(1200, 150, 5, -100, 220)
            car_group.add(car)

        # Getting the keydown event to check for key presses
        if event.type == pygame.KEYDOWN:
            # Checking if the up arrow key is pressed
            if event.key == pygame.K_UP:
                # If pressed then player move up and show player up animation
                player.up = True
                player.down = False
                player.left = False
                player.right = False

            # Checking if the down aarrow key is pressed
            if event.key == pygame.K_DOWN:
                # If pressed than player move down and show player down animation
                player.down = True
                player.up = False
                player.left = False
                player.right = False

            # Checking if the left arrow key is pressed
            if event.key == pygame.K_LEFT:
                # If pressed then player move left and show player left animation
                player.left = True
                player.up = False
                player.down = False
                player.right = False

            # Checking if the right arrow key is pressed
            if event.key == pygame.K_RIGHT:
                # If pressed then player move right and show player right animation
                player.right = True
                player.up = False
                player.down = False
                player.left = False

        # Checking if the keys are not pressed anymore and reset it
        if event.type == pygame.KEYUP:
            # If the up key is not pressed then up animation should be false
            if event.key == pygame.K_UP:
                player.up = False

            # If the down key is not pressed then down animation should be false
            if event.key == pygame.K_DOWN:
                player.down = False

            # If the right key is not pressed then left animation should be false
            if event.key == pygame.K_LEFT:
                player.left = False

            # If the right key is not pressed then right animation should be false
            if event.key == pygame.K_RIGHT:
                player.right = False

    # background
    window.fill((0, 0, 0))
    # Calling the draw function
    draw()

    # Drawing the player and updating it
    player_group.draw(window)
    player_group.update(0.25)

    car_group.draw(window)
    car_group.update()

    # Frame rate and updating the window
    clock.tick(100)
    pygame.display.update()

