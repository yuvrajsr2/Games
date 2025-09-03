# Import
import pygame

# Initialize
pygame.init()

# Window
Width, Height = 1000, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Pong")

# Game Characters
player1 = pygame.Rect(5, Height / 2 - 70, 15, 140)
player2 = pygame.Rect(980, Height / 2 - 70, 15, 140)
ball = pygame.Rect(Width / 2 - 15, Height / 2, 30, 30)

# Speed variables
ball_vel_x = 10
ball_vel_y = 10

player1_vel = 0
player2_vel = 0

player1_score = 0
player2_score = 0

# Font variables
score_font = pygame.font.SysFont('comicsans', 50)
button_font = pygame.font.SysFont('comicsans', 80)
game_over_font = pygame.font.SysFont('comicsans', 100)

# Color variable
white = (255, 255, 255)

# Global variables
valid = False
button_valid = True

# Button variables
button_x = 430
button_y = 250
button_width = 150
button_height = 50


# Displaying stuff on the window
def display():
    pygame.draw.rect(window, white, player1)
    pygame.draw.rect(window, white, player2)
    pygame.draw.ellipse(window, white, ball)


# Displaying the font and ending the game
def display_font():
    global valid, button_valid

    player1_text = score_font.render(f"Player1 : {player1_score}", True, white)
    window.blit(player1_text, (150, 20))

    player2_text = score_font.render(f"Player2 : {player2_score}", True, white)
    window.blit(player2_text, (650, 20))

    if player1_score >= 10:
        valid = False
        button_valid = True

        winner_text = game_over_font.render("Player 1  Won", True, white)
        window.blit(winner_text, (330, 400))

    if player2_score >= 10:
        valid = False
        button_valid = True

        winner_text = game_over_font.render("Player 2  Won", True, white)
        window.blit(winner_text, (330, 400))


# Moving the ball
def ball_movement():
    global ball_vel_x, ball_vel_y, player2_score, player1_score

    ball.x += ball_vel_x
    ball.y += ball_vel_y

    if ball.top <= 0:
        ball_vel_y *= -1
    if ball.bottom >= Height:
        ball_vel_y *= -1

    if ball.left <= 0:
        ball_vel_x *= -1
        player2_score += 1

    if ball.right >= Width:
        ball_vel_x *= -1
        player1_score += 1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_vel_x *= -1


# Moving the paddles
def move_player():
    player1.y += player1_vel
    player2.y += player2_vel

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= Height:
        player1.bottom = Height

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= Height:
        player2.bottom = Height


# main Game Loop
clock = pygame.time.Clock()
fps = 60
running = True
while running:

    # Getting the mouse pos for checking if it is in the button width and height
    mouse_pos = pygame.mouse.get_pos()

    # events
    for event in pygame.event.get():
        # Quit event, checking if the quit button is pressed
        if event.type == pygame.QUIT:
            running = False

        # Checking if when the mouse is pressed the mouse pos inside the width and height of the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_valid:
                if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                    print("pressed")
                    valid = True
                    button_valid = False
                    player1_score = 0
                    player2_score = 0


        # Keydown event checking for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player1_vel += 9
            if event.key == pygame.K_w:
                player1_vel -= 9

            if event.key == pygame.K_DOWN:
                player2_vel += 9
            if event.key == pygame.K_UP:
                player2_vel -= 9

        # KeyUp event,  checking if any keys are pressed or not
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player1_vel -= 9
            if event.key == pygame.K_w:
                player1_vel += 9

            if event.key == pygame.K_DOWN:
                player2_vel -= 9
            if event.key == pygame.K_UP:
                player2_vel += 9

    # background
    window.fill((0, 0, 0))

    # If valid is true
    if valid:
        # Calling the functions
        display()
        ball_movement()
        move_player()

    # Calling the display font function
    display_font()
    # Displaying a line between the window
    pygame.draw.aaline(window, white, (Width / 2, 0), (Width / 2, Height))

    # If button valid is true display the button
    if button_valid:
        pygame.draw.rect(window, white, (button_x, button_y, button_width, button_height))
        button_text = button_font.render("Start", True, (0, 0, 0))
        window.blit(button_text, (button_x + 5, button_y + 2))

    # Fps, controls how fast our game is
    clock.tick(fps)

    # Updating the screen
    pygame.display.update()