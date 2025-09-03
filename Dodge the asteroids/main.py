# Imports
import pygame
import random

# Initializing pygame
pygame.init()

# Setting up the window
Width, Height = 1000, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Dodge the Meteors")


# Spaceship Class
class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        # Loading the spaceship image and giving it a position
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        # Health
        self.health = 5
        self.shield_surface = pygame.image.load('shield.png')

    def update(self):
        # Making the spaceship pos = your mouse pos
        self.rect.center = pygame.mouse.get_pos()
        # Boundary function
        self.boundary()
        # Health function
        self.display_health()

    # sets the boundary for our spaceship so that it does not go out of the screen
    def boundary(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= Width:
            self.rect.right = Width
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= Height:
            self.rect.bottom = Height

    # This function is displaying the spaceship health
    def display_health(self):
        for index, shield in enumerate(range(self.health)):
            window.blit(self.shield_surface, (index * 40, 10))


# Meteor Class
class Meteor(pygame.sprite.Sprite):
    def __init__(self, img, x_pos, y_pos, x_speed, y_speed):
        super().__init__()
        # Loading the image and giving it a position
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

        # Creating attributes for x and y speed parameters
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        # Moving the meteors by the x and y speed
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed

        # if the meteors go out of the screen then delete them so that our game does not lag
        if self.rect.centery >= 700:
            self.kill()


# Spaceship group
spaceship = SpaceShip('spaceship.png', 300, 300)
spaceship_group = pygame.sprite.GroupSingle(spaceship)

# Meteor Group
meteor_group = pygame.sprite.Group()
meteor_event = pygame.USEREVENT
pygame.time.set_timer(meteor_event, 200)

# Laser group
laser_group = pygame.sprite.Group()

# Global variables
score = 0
game_font = pygame.font.Font('LazenbyCompSmooth.ttf', 150)
score_font = pygame.font.Font('LazenbyCompSmooth.ttf', 50)
valid = True

# Game loop
clock = pygame.time.Clock()
running = True
while running:

    # Getting the mouse pos
    mouse = pygame.mouse.get_pos()

    # Getting events
    for event in pygame.event.get():
        # Quiting the game
        if event.type == pygame.QUIT:
            running = False
        # If meteor event is triggered then do this
        if event.type == meteor_event:
            # Image
            path = random.choice(('Meteor1.png', 'Meteor2.png', 'Meteor3.png'))
            # X position for meteor
            random_x_pos = random.randrange(0, 1000)
            # y position for meteor
            random_y_pos = random.randrange(-500, -50)
            # X speed for meteor
            random_x_speed = random.randrange(-1, 1)
            # Y speed for meteor
            random_y_speed = random.randrange(4, 10)
            # Calling the meteor class
            meteor = Meteor(path, random_x_pos, random_y_pos, random_x_speed, random_y_speed)
            # Adding the meteor class to the meteor group
            meteor_group.add(meteor)
        # keydown in events to check for key presses
        if event.type == pygame.KEYDOWN:
            # Checking if the space key is pressed
            if event.key == pygame.K_SPACE:
                # If pressed then it will call the laser class and add it to the laser group
                new_laser = Laser('Laser.png', mouse, 15)
                laser_group.add(new_laser)
            # Checking if r key is pressed
            if event.key == pygame.K_r and spaceship_group.sprite.health < 1:
                # If pressed than restart the game
                # Empty the groups
                laser_group.empty()
                meteor_group.empty()
                # Health becomes 5
                spaceship_group.sprite.health = 5
                # Score becomes 0
                score = 0

    # Background color
    window.fill((42, 41, 56))

    # If health is more than 0 than it will display everything
    if spaceship_group.sprite.health > 0:

        # Drawing lasers and updating them
        laser_group.draw(window)
        laser_group.update()

        # Drawing spaceship and updating it
        spaceship_group.draw(window)
        spaceship_group.update()

        # Drawing meteors and updating it
        meteor_group.draw(window)
        meteor_group.update()

        # Creating the score and then displaying on the screen
        score_text = score_font.render(f'Score: {score}', False, (255, 255, 255))
        window.blit(score_text, (700, 10))

    # But if not more than 0 than it will display game over
    else:
        # Displaying game over
        game_text = game_font.render('Game Over', False, (255, 255, 255))
        game_pos = game_text.get_rect(center=(500, 300))
        window.blit(game_text, game_pos)

        # Displaying the score
        score_text = score_font.render(f'Score: {score}', False, (255, 255, 255))
        window.blit(score_text, (700, 10))

    # If it is valid collision will work and if not then it won't work
    if valid:

        # Collision between spaceship and meteors
        if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
            # If there is collision then minus 1 from health
            spaceship_group.sprite.health -= 1

        # Collision between laser and meteors
        for laser in laser_group:
            if pygame.sprite.spritecollide(laser, meteor_group, True):
                # If there is collision then increase score by 1
                score += 1

    # Frame rate and updating the screen
    clock.tick(60)
    pygame.display.update()
