import pygame
import random
import math

# Initialize the pygame
pygame.init()

# create the screen (x(left to right WIDTH), y(top do down HEIGHT))
screen = pygame.display.set_mode((800, 600))

# Background picture
background = pygame.image.load('background.jpeg')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('skull.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('pumpkin.png')
playerX = 370
playerY = 480
playerX_change = 0

score = 0


def player(x, y):
    # Draw player method (image (surface) and position)
    screen.blit(playerImg, (x, y))


# Enemy

enemyImg = pygame.image.load('bat.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(10, 50)
enemyX_change = 0.2
enemyY_change = 40
enemyYChange = 0


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet

# Ready state - You cant see bullet on the screen
# Fire - bullet is moving

bulletImg = pygame.image.load('candy.png')
bulletX = 0
bulletY = 480
bullet_state = "ready"
bulletY_change = 0.5

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Game Loop
running = True
while running:

    # Background in RGB (RED, GREEN, BLUE)
    screen.fill((128, 64, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change -= 0.3
            if event.key == pygame.K_d:
                playerX_change += 0.3

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    # enemy movement




    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX = 0
        enemyX_change = 0.2
        enemyY += 40

    elif enemyX >= 736:
        enemyX = 736
        enemyX_change = -0.2
        enemyY += 40

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        score_value += 1
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 736)
        enemyY = random.randint(10, 50)

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Calling player (always after fill method)
    player(playerX, playerY)
    show_score(textX, textY)
    enemy(enemyX, enemyY)
    pygame.display.update()
