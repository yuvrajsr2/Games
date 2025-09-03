# Imports
import pygame
import random

# Initializing pygame
pygame.init()

# Setting up the window
Width, Height = 800, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Rock paper scissors")

# Fonts
heading_font = pygame.font.Font('freesansbold.ttf', 78)
question_font = pygame.font.Font('freesansbold.ttf', 40)

# Global variables
player_choice = None
computer_choice = random.choice(("p", "r", "s"))
valid = True
winner = None

# Loading paper image and transforming it
paper_img = pygame.image.load('paper.png').convert()
paper_img = pygame.transform.scale(paper_img, (230, 200))

# Loading rock image and transforming it
rock_img = pygame.image.load('rock.png').convert()
rock_img = pygame.transform.scale(rock_img, (230, 200))

# Loading scissors image and transforming it
scissors_img = pygame.image.load('scissors.png').convert()
scissors_img = pygame.transform.scale(scissors_img, (230, 200))


# Displaying text on the screen
def display_text():
    # Displaying the heading
    heading_text = heading_font.render("Rock Paper Scissors", True, (255, 255, 255))
    heading_rect = heading_text.get_rect(center=(400, 100))
    window.blit(heading_text, heading_rect)

    # Displaying the choose word
    question_text = question_font.render("Choose ", True, (255, 255, 255))
    question_rect = heading_text.get_rect(center=(700, 300))
    window.blit(question_text, question_rect)


# Displaying the images on the screen
def display_img():
    window.blit(paper_img, (10, 350))

    window.blit(rock_img, (280, 350))

    window.blit(scissors_img, (550, 350))


# Checking for winner
def check_winner():
    global winner

    if computer_choice == player_choice:
        winner = "Tie"
    elif computer_choice == "p" and player_choice == "r":
        winner = "You lost"
    elif computer_choice == "p" and player_choice == "s":
        winner = "You won"
    elif computer_choice == "r" and player_choice == "p":
        winner = "You won"
    elif computer_choice == "r" and player_choice == "s":
        winner = "You lost"
    elif computer_choice == "s" and player_choice == "p":
        winner = "You lost"
    elif computer_choice == "s" and player_choice == "r":
        winner = "You won"


# When the rock paper scissors button is pressed then display this
def end_screen():
    # Displaying the computer choice after button is pressed
    if computer_choice == "p":
        window.blit(paper_img, (60, 200))
    elif computer_choice == "r":
        window.blit(rock_img, (60, 200))
    elif computer_choice == "s":
        window.blit(scissors_img, (60, 200))

    # Displaying the player choice after button is pressed
    if player_choice == "p":
        window.blit(paper_img, (500, 200))
    elif player_choice == "r":
        window.blit(rock_img, (500, 200))
    elif player_choice == "s":
        window.blit(scissors_img, (500, 200))

    # Displaying the button for playing again
    pygame.draw.rect(window, (0, 0, 255), (270, 50, 250, 50))
    button_text = question_font.render(f"Play Again", True, (255, 255, 255))
    window.blit(button_text, (285, 53))

    # Displaying the text of who won
    end_screen_text = heading_font.render(f"{winner}", True, (255, 255, 255))
    end_screen_rect = end_screen_text.get_rect(center=(400, 500))
    window.blit(end_screen_text, end_screen_rect)

    # Displaying computer in front of its choice
    computer_text = question_font.render("Computer", True, (255, 255, 255))
    window.blit(computer_text, (65, 160))

    # Displaying player in front of its choice
    player_text = question_font.render("Player", True, (255, 255, 255))
    window.blit(player_text, (550, 160))


# Main game loop
clock = pygame.time.Clock()
running = True
while running:

    # Getting the mouse pos for checking for buttons
    mouse = pygame.mouse.get_pos()

    # getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checking if mouse button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:

            # if mouse buttons is clicked and it is valid check if the mouse pos is between these values
            if valid:
                # If between these values then valid is False
                if 10 <= mouse[0] <= 240 and 350 <= mouse[1] <= 550:
                    player_choice = "p"
                    valid = False

                if 280 <= mouse[0] <= 510 and 350 <= mouse[1] <= 550:
                    player_choice = "r"
                    valid = False

                if 550 <= mouse[0] <= 780 and 350 <= mouse[1] <= 550:
                    player_choice = "s"
                    valid = False

            # If valid becomes false then make a button for play again
            if valid is False:
                # If this happens then valid becomes true again and computer selects again and the player too
                if 270 <= mouse[0] <= 520 and 50 <= mouse[1] <= 100:
                    valid = True
                    computer_choice = random.choice(("p", "r", "s"))

    # Background
    window.fill((250, 68, 0))

    # Displaying this if it valid
    if valid:
        # Calling the display text and image functions
        display_text()
        display_img()


    # If it is not valid then display end screen
    else:
        # Calling the end screen function
        end_screen()

    # Calling checking for winner function
    check_winner()

    # Setting frame rate and updating the window
    clock.tick(60)
    pygame.display.update()
