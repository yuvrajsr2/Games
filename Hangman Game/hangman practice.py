import pygame

pygame.init()

Width, Height = 800, 500
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Hangman")

images = []
hangman_status = 6
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

radius = 20
gap = 15
startx = round((Width - (radius * 2 + gap) * 13) / 2)
starty = 400
letters = []
a = 65
for i in range(26):
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(a + i)])

letter_font = pygame.font.Font('freesansbold.ttf', 25)


def draw():
    window.fill((255, 255, 255))

    for letter in letters:
        x, y, ltr = letter
        pygame.draw.circle(window, (0, 0, 0), (x, y), radius, 3)
        text = letter_font.render(ltr, True, (255, 69, 0))
        window.blit(text, (x - 10, y - 10))

    window.blit(images[hangman_status], (130, 100))


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()

    clock.tick(60)
    pygame.display.update()
