#  -------- Start of the Program ---------

# Import
import pygame
import random

# Initialize pygame so that we have no errors
pygame.init()

# Set up the screen


# game variables
current_fighter = 1
total_fighter = 3
action_cooldown = 0
action_wait_time = 90

Width, Height = 1000, 550
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("HI")

# Loading background image
bgImg = pygame.image.load('Background/background.png')
bgImg = pygame.transform.scale(bgImg, (1000, 400))

# Loading the panel img
panelImg = pygame.image.load('Icons/panel.png')
panelImg = pygame.transform.scale(panelImg, (1000, 150))

font = pygame.font.Font('freesansbold.ttf', 35)
bandit_font = pygame.font.Font('freesansbold.ttf', 25)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)


# PLayer class for handling the player
class Player:
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.potions = potions
        self.start_potions = potions
        self.alive = True

        # Animating the player
        self.animation_list = []
        self.frame_index = 0
        self.action = 0

        # Loading multiple images using a for loop
        temp_list = []
        for i in range(8):
            self.image = pygame.image.load(f'{self.name}/Idle/{i}.png ')
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
            temp_list.append(self.image)

        self.animation_list.append(temp_list)

        temp_list = []
        for i in range(8):
            self.image = pygame.image.load(f'{self.name}/Attack/{i}.png ')
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
            temp_list.append(self.image)

        self.animation_list.append(temp_list)

        self.img = self.animation_list[self.action][self.frame_index]
        self.rect = self.img.get_rect(center=(x, y))

    # Update method to increase the frame index so that our animation works
    def update(self):

        self.frame_index += 0.2

        if int(self.frame_index) >= len(self.animation_list[self.action]):
            self.idle()

        self.img = self.animation_list[self.action][int(self.frame_index)]


    def attack(self, target):
        rand = random.randint(-4, 4)
        damage = self.strength + rand
        target.hp -= damage
        self.action = 1
        self.frame_index = 0

    def idle(self):
        self.frame_index = 0
        self.action = 0

    # Display function for displaying the player on the screen
    def display(self):
        window.blit(self.img, self.rect)


class Healthbar:
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        self.ratio = self.hp / self.max_hp
        pygame.draw.rect(window, red, (self.x, self.y, 180, 20))
        pygame.draw.rect(window, green, (self.x, self.y, 180 * self.ratio, 20))


# Calling the Player function in var player
player = Player(200, 260, 'Knight', 30, 10, 3)

# Creating a list and appending the bandit instances to it
bandit_list = []
bandit1 = Player(600, 270, 'Bandit', 15, 5, 1)
bandit2 = Player(800, 270, 'Bandit', 15, 5, 1)
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = Healthbar(100, 460, player.hp, player.max_hp)
bandit1_health_bar = Healthbar(600, 440, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = Healthbar(600, 500, bandit2.hp, bandit2.max_hp)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))


# Display function to display things on the screen
def display():
    # Drawing the background image
    window.blit(bgImg, (0, 0))

    # Drawing the panel img
    window.blit(panelImg, (0, 400))

    knight_health_bar.draw(player.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)

    draw_text(f'{player.name} HP: {player.hp}', font, white, 100, 420)

    for count, i in enumerate(bandit_list):
        draw_text(f'{i.name} HP: {i.hp}', bandit_font, white, 600, 410 + count * 60)

    # Calling the player display and update function
    player.update()
    player.display()

    # Using a for loop to draw multiple bandits
    for bandit in bandit_list:
        bandit.update()
        bandit.display()


#  -------- Game Loop -----------

# Making a frame rate
clock = pygame.time.Clock()
# This var will determine if the game loop is running or not
running = True
while running:
    # getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calling the display function
    display()

    if player.alive == True:
        if current_fighter == 1:
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                player.attack(bandit1)
                current_fighter += 1
                action_cooldown = 0

    for count, bandit in enumerate(bandit_list):
        if current_fighter == 2 + count:
            if bandit.alive == True:
                action_cooldown += 1


    # Frame rate and updating the screen
    clock.tick(60)
    pygame.display.update()


# --------- End of the Program --------

