# ----- Start of the Program ----- RPG Game -------


# Importing pygame
import pygame
import random

# Initializing pygame
pygame.init()

# Game window
Width, Height = 1000, 550
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Rpg, battle!")

current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90

# load images
# background image
background_img = pygame.image.load('Background/background.png').convert_alpha()
background_img = pygame.transform.scale(background_img, (1000, 400))

# panel image
panel_img = pygame.image.load('Icons/panel.png').convert_alpha()
panel_img = pygame.transform.scale(panel_img, (1000, 150))

sword_img = pygame.image.load('Icons/sword.png').convert_alpha()

font = pygame.font.Font('freesansbold.ttf', 30)

red = (255, 0, 0)
green = (0, 255, 0)


# Fighter class for displaying the player and enemies
class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        # loading multiple images for animating the characters
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0 -  idle , 1 - Attack, 2 - Hurt, 3 - dead
        self.update_time = pygame.time.get_ticks()
        # For loop for loading multiple images and appending it to the list

        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'{self.name}/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'{self.name}/Attack/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(center=(x, y))

    def attack(self, target):
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage

        if target.hp < 1:
            target.hp = 0
            target.alive = False

        self.action = 1
        self.frame_index = 0

    # This method updates the frame index which animates the character
    def update(self):
        animation_cooldown = 100

        self.frame_index += 0.2

        if int(self.frame_index) >= len(self.animation_list[self.action]):
            self.idle()

        self.image = self.animation_list[self.action][int(self.frame_index)]

    def idle(self):
        self.action = 0
        self.frame_index = 0

    # Draw method for drawing them on the window
    def draw(self):
        window.blit(self.image, self.rect)


class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(window, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(window, green, (self.x, self.y, 150 * ratio, 20))


# Calling the fighter function
knight = Fighter(200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(750, 270, 'Bandit', 20, 6, 1)
bandit2 = Fighter(900, 270, 'Bandit', 20, 6, 1)

# Making a list and appending the enemies to it
bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)


knight_health_bar = HealthBar(100, 450, knight.hp, knight.max_hp)

bandit1_health_bar = HealthBar(650, 440, bandit1.hp, bandit1.max_hp)

bandit2_health_bar = HealthBar(650, 500, bandit2.hp, bandit2.max_hp)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))


# Display function for displaying things
def display():
    global action_cooldown
    global current_fighter

    # Displaying the background img
    window.blit(background_img, (0, 0))

    # Displaying the panel img
    window.blit(panel_img, (0, 400))


    knight_health_bar.draw(knight.hp)

    bandit1_health_bar.draw(bandit1.hp)

    bandit2_health_bar.draw(bandit2.hp)

    draw_text(f'{knight.name} HP : {knight.hp}', font, red, 100, 410)

    for count, i in enumerate(bandit_list):
        draw_text(f'{i.name} HP : {i.hp}', font, red, 650, 410 + count * 60)

    # Calling the draw method from the Fighter class
    knight.update()
    knight.draw()

    # making for loop to display all the enemies on the screen
    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    if knight.alive == True:
        if current_fighter == 1:
            action_cooldown += 1

            if action_cooldown >= action_wait_time:
                knight.attack(bandit1)
                current_fighter += 1
                action_cooldown = 0

    for count, bandit in enumerate(bandit_list):
        if current_fighter == 2 + count:
            if bandit.alive:
                action_cooldown += 1

                if action_cooldown >= action_wait_time:
                    bandit.attack(knight)
                    current_fighter += 1
                    action_cooldown = 0

            else:
                current_fighter += 1


    if current_fighter > total_fighters:
        current_fighter = 1


# Game Loop
clock = pygame.time.Clock()
running = True
while running:
    # Getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background color
    window.fill((0, 0, 0))

    # Calling the display function
    display()

    # Setting frame rate and updating the window
    clock.tick(60)
    pygame.display.update()


# ------- End of the Program ------- Rpg Game complete ----------
