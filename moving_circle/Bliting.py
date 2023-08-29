import pygame
import os

pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")
CEN = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pic.png')), (screen_width, screen_height))

running = True
trial_font = pygame.font.SysFont("comicsans", 70)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill((0, 255, 0))
    screen.blit(CEN, (0, 0))
    trial = trial_font.render("CEN to the WORLD", 1, (255, 0, 0))
    screen.blit(trial, (20, 10))
    pygame.display.update()

pygame.quit()