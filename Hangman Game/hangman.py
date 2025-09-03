# Imports
import pygame
import os
import math

# Initializing pygame
pygame.init()

# Setting up the window
Width, Height = 800, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Hello")

# Loading images
images = []
hangman_status = 6
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# Making the circles and their letters
radius = 20
gap = 15
letters = []
startx = round((Width - (radius * 2 + gap) * 13) / 2)
starty = 400
a = 65
for i in range(26):
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(a + i), True])

# Fonts
letter_font = pygame.font.SysFont('comicsans', 40)
word_font = pygame.font.SysFont('comicsans', 60)


word = "CLEARCODING"
guessed = []


# Draw function for drawing images and circles
def draw():
    window.fill((255, 255, 255))

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_font.render(display_word, 1, (0, 0, 0))
    window.blit(text, (320, 200))

    # Drawing the circles and letters
    for letter in letters:
        x, y, ltr, valid = letter
        if valid:
            pygame.draw.circle(window, (0, 0, 0), (x, y), radius, 3)
            letter_text = letter_font.render(ltr, 1, (0, 0, 0))
            window.blit(letter_text, (x - 10, y - 15))

    # Drawing the hangman images
    window.blit(images[hangman_status], (100, 150))


# Main Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Getting the mouse pos when button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, valid = letter
                if valid:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < radius:
                        letter[3] = False
                        guessed.append(ltr)

    # Calling the draw function
    draw()

    # Frame rate and updating the window
    clock.tick(60)
    pygame.display.update()
