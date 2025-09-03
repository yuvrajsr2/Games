import pygame
import random

pygame.init()

Width, Height = 1000, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Hi")

ball = pygame.Rect(Width / 2 - 15, Height / 2 - 15, 30, 30)
player = pygame.Rect(5, Height / 2 - 70, 15, 140)
opponent = pygame.Rect(980, Height / 2 - 70, 15, 140)

ball_speed_x = 12 * random.choice((1, -1))
ball_speed_y = 12 * random.choice((1, -1))
player_speed = 0
opponent_speed = 0

player_score = 0
opponent_score = 0
score_font = pygame.font.Font('freesansbold.ttf', 50)

score_time = True


def draw():
    window.fill((0, 0, 0))

    pygame.draw.ellipse(window, (255, 255, 255), ball)
    pygame.draw.rect(window, (255, 255, 255), player)
    pygame.draw.rect(window, (255, 255, 255), opponent)
    pygame.draw.aaline(window, (255, 255, 255), (Width / 2, 0), (Width / 2, Height))

    player_text = score_font.render(f"Player 1 : {player_score}", True, (255, 255, 255))
    window.blit(player_text, (100, 20))

    opponent_text = score_font.render(f"Player 2 : {opponent_score}", True, (255, 255, 255))
    window.blit(opponent_text, (600, 20))


def ball_move():
    global ball_speed_y, ball_speed_x, opponent_score, player_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    elif ball.right >= Width:
        player_score += 1
        score_time = pygame.time.get_ticks()

    elif ball.top <= 0:
        ball_speed_y *= -1

    elif ball.bottom >= Height:
        ball_speed_y *= -1


def collision():
    global ball_speed_x

    if ball.colliderect(player):
        ball_speed_x *= -1
    elif ball.colliderect(opponent):
        ball_speed_x *= -1


def move_player():
    player.y += player_speed
    opponent.y += opponent_speed

    if player.top <= 0:
        player.top = 0
    elif player.bottom >= Height:
        player.bottom = Height

    if opponent.top <= 0:
        opponent.top = 0
    elif opponent.bottom >= Height:
        opponent.bottom = Height


def ball_restart():
    global ball_speed_y, ball_speed_x, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (Width / 2, Height / 2)

    if current_time - score_time < 700:
        number_three = score_font.render("3", False, (255, 255, 255))
        window.blit(number_three, (Width/2 - 10, Height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = score_font.render("2", False, (255, 255, 255))
        window.blit(number_two, (Width/2 - 10, Height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = score_font.render("1", False, (255, 255, 255))
        window.blit(number_one, (Width/2 - 10, Height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_x = 12 * random.choice((1, -1))
        ball_speed_y = 12 * random.choice((1, -1))
        score_time = None




clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 10

            if event.key == pygame.K_s:
                player_speed += 10

            if event.key == pygame.K_UP:
                opponent_speed -= 10

            if event.key == pygame.K_DOWN:
                opponent_speed += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 10

            if event.key == pygame.K_s:
                player_speed -= 10

            if event.key == pygame.K_UP:
                opponent_speed += 10

            if event.key == pygame.K_DOWN:
                opponent_speed -= 10



    move_player()
    draw()
    ball_move()
    collision()

    if score_time:
        ball_restart()

    clock.tick(60)
    pygame.display.update()
