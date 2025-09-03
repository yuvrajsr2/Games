# Imports
import pygame
import random


# Initializing pygame
pygame.init()

# Setting up the Window
Width, Height = 700, 600
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Flappy Bird")

# Background image
bgImg = pygame.image.load('background-night.png').convert()
bgImg = pygame.transform.scale(bgImg, (Width, Height))

# Floor Image
floorImg = pygame.image.load('base.png')
floorImg = pygame.transform.scale(floorImg, (700, 100))
floor_x_pos = 0

# Bird and its variables
bird_down = pygame.image.load('yellowbird-downflap.png').convert()
bird_mid = pygame.image.load('yellowbird-midflap.png').convert()
bird_up = pygame.image.load('yellowbird-upflap.png').convert()
bird_frames = [bird_down, bird_mid, bird_up]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_pos = bird_surface.get_rect(center=(200, 100))
BirdFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BirdFLAP, 100)

# Pipe image
pipeImg = pygame.image.load('pipe-green.png')
PIPE_EVENT = pygame.USEREVENT
pipe_list = []
pygame.time.set_timer(PIPE_EVENT, 1200)
pipe_height = [250, 300, 350, 400, 450]

# Global variables
gravity = 0.25
bird_movement = 0
valid = False
valid1 = False
can_score = True
score = 0
high_score = 0
score_font = pygame.font.Font('freesansbold.ttf', 30)
game_font = pygame.font.Font('freesansbold.ttf', 60)


# Drawing the floor
def floor():
    global floor_x_pos

    window.blit(floorImg, (floor_x_pos, 500))
    window.blit(floorImg, (floor_x_pos + 576, 500))

    if floor_x_pos <= -576:
        floor_x_pos = 0


# Creating the pipe
def create_pipe():

    height = random.choice(pipe_height)
    bottom_pipe = pipeImg.get_rect(midtop=(900, height))
    top_pipe = pipeImg.get_rect(midbottom=(900, height - 200))

    return bottom_pipe, top_pipe


# Moving the pipe to the left
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


# Drawing the pipe on the screen
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 400:
            window.blit(pipeImg, pipe)
        else:
            pipeImg_flip = pygame.transform.flip(pipeImg, False, True)
            window.blit(pipeImg_flip, pipe)


# Collision between bird and pipes and sky and floor
def collision(pipes):
    global valid, valid1

    # Collision between bird and pipes
    for pipe in pipes:
        if bird_pos.colliderect(pipe):
            valid = False
            valid1 = True

    if bird_pos.top <= 0 or bird_pos.bottom >= 500:
        valid = False
        valid1 = True


# Rotating the bird when it goes up and down
def rotate_bird(bird):
    bird_rotated = pygame.transform.rotate(bird, -bird_movement * 3)
    return bird_rotated


# Animation the bird by moving its flaps
def bird_animation():
    new_bird = bird_frames[bird_index]
    new_pos = new_bird.get_rect(center=(200, bird_pos.centery))
    return new_bird, new_pos


# Displaying the score and setting a high score
def display_score():
    global high_score

    score_text = score_font.render(f'Score: {score}', True, (255, 255, 255))
    window.blit(score_text, (30, 20))

    high_score_text = score_font.render(f'High Score: {high_score}', True, (255, 255, 255))
    window.blit(high_score_text, (300, 20))

    if score > high_score:
        high_score = score


# Increasing the score when bird crosses pipe without touching it
def increase_score():
    global score, can_score

    if pipe_list:
        for pipe in pipe_list:
            if bird_pos.centerx == pipe.centerx and can_score:
                score += 1
                can_score = False
            if bird_pos.centerx != pipe.centerx:
                can_score = True


# Game Loop
clock = pygame.time.Clock()
running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If space key is down then bird goes up
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6
            # If r key is pressed than restart the game and only do that if the there is any collision
            if event.key == pygame.K_SPACE and valid == False:
                valid = True
                valid1 = False
                score = 0
                pipe_list.clear()
                bird_movement = 0
                bird_pos.center = (200, 100)
        # Drawing pipes when this is triggered
        if event.type == PIPE_EVENT:
            pipe_list.extend(create_pipe())

        if event.type == BirdFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_pos = bird_animation()

    # Game Logic
    window.blit(bgImg, (0, 0))

    if valid:
        collision(pipe_list)

        # Calling the pipe functions
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)

        # Moving the bird and also drawing it on the screen
        rotated_bird = rotate_bird(bird_surface)
        bird_movement += gravity
        bird_pos.centery += bird_movement
        window.blit(rotated_bird, bird_pos)

        increase_score()

    if valid1 is True:
        game_over = game_font.render('Game Over', True, (255, 255, 255))
        game_over_rect = game_over.get_rect(center=(350, 300))
        window.blit(game_over, game_over_rect)

    # Calling the displaying score and increase score function
    display_score()

    # Calling the floor function and also moving it
    floor_x_pos -= 5
    floor()

    # Frame rate
    clock.tick(120)

    # Updating the screen
    pygame.display.update()
