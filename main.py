import math
import random
import tkinter as tk
import pygame
from pygame import mixer
import time

# Intialize the pygame
pygame.init()

#Creating the first start up screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CLICK TO START")
font = pygame.font.Font(None, 50)

play_image = pygame.image.load("play.png").convert_alpha()
quit_image = pygame.image.load('quit.png').convert_alpha()
restart_image = pygame.image.load('restart.png').convert_alpha()

play_rect = play_image.get_rect()
play_rect.centerx = screen.get_rect().centerx - 100
play_rect.centery = screen.get_rect().centery

quit_rect = quit_image.get_rect()
quit_rect.centerx = screen.get_rect().centerx + 100
quit_rect.centery = screen.get_rect().centery

restart_rect = restart_image.get_rect()
restart_rect.centerx = screen.get_rect().centerx + 100
restart_rect.centery = screen.get_rect().centery


#caption and icon for the first screen
pygame.display.set_caption("Haggai's space fighter")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
background = pygame.image.load('bg3.png')
play_bn = pygame.image.load('play.png').convert_alpha()		
restart_bn = pygame.image.load('restart.png').convert_alpha()
quit_bn = pygame.image.load('quit.png').convert_alpha()

font1 = pygame.font.Font('freesansbold.ttf', 64)

# create the 2nd screen for the game
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('bg3.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Caption and Icon for the 2nd screen
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def start_game():
    # code to start the game goes here
    #loop for the first screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos=pygame.mouse.get_pos()
                if play_rect.collidepoint(mouse_pos):
                    running = False
                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Start the game here
                pass
        screen.blit(background, (0, 0))
        screen.blit(play_image, play_rect)
        screen.blit(quit_image, quit_rect)

        pygame.display.update()

root = tk.Tk()
root.title("Click to Start Game")

start_button = tk.Button(root, text="Start Game", command=start_game())
start_button.pack()

# def game_over_text():
#     # Clear the screen
#     screen.fill((255, 255, 255))

#     # Render the text "Game Over"
#     font = pygame.font.Font(None, 36)
#     text = font.render("Game Over", True, (0, 0, 0))
#     text_rect = text.get_rect()
#     text_rect.centerx = screen.get_rect().centerx
#     text_rect.centery = screen.get_rect().centery

#     # Blit the text onto the screen
#     screen.blit(text, text_rect)

#     # Update the screen
#     pygame.display.update()

def game_over():
    while True:
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        for i in range(3):
            text = font1.render('Game over', True, (255, 255, 255))
            screen.blit(text, (200, 250))
            time.sleep(1)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        break
        pygame.display.update()



# Player
playerImg = pygame.image.load('ufo.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 20

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(7)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 8
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

   #player change increment
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
                playerY=2000
            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()






    pygame.display.update()
