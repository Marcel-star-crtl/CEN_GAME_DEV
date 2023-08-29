import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movements")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


FPS = 60
VEL = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100, 100

PLAYER_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'ufo.png'))
PLAYER_SPACESHIP = pygame.transform.scale(PLAYER_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'bg3.png')), (WIDTH, HEIGHT))


def draw_window( yellow):
    WIN.blit(SPACE, (0, 0))

    WIN.blit(PLAYER_SPACESHIP, (yellow.x, yellow.y))

    pygame.display.update()


def player_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < WIDTH:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL



def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, yellow)

        draw_window(yellow)

    main()

if __name__ == "__main__":
    main()
