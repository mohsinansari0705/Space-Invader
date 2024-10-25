import pygame as pg
import random

# Initialize the pygame
pg.init()

# Create a screen
dimentions = (800, 600) # Width & Height(X, Y axis)
screen = pg.display.set_mode(dimentions)
backgroundImg = pg.image.load("background.png") # Load the background image


# Title & Icon
pg.display.set_caption("Space Invader :Devox_Network")
icon = pg.image.load("GameLogo.png")
pg.display.set_icon(icon)

# Player
playerImg = pg.image.load("player.png")
playerX = 368 # Initial coordinates of the spaceship
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pg.image.load("enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 236)
enemyX_change = 2.5
enemyY_change = 32

# Bullet
bulletImg = pg.image.load("bullet.png")
bulletX = 0
bulletY = playerY
bulletY_change = 10
bulletState = "ready"

# Player randering Function
def player(x, y):
    screen.blit(playerImg, (x, y))
    
# Enemy randering Function
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Bullet firing & randering Function
def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x+24, y-5))

# Game Loop
running = True
while running:
    screen.fill((23, 23, 23)) # Background color
    screen.blit(backgroundImg, (0, 0)) # Background image

    # Checking for the Events in the game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Changing the player moment depending upon the key pressed
        if event.type == pg.KEYDOWN:
            if event.key==pg.K_LEFT or event.key==pg.K_a:
                playerX_change = -4
            if event.key==pg.K_RIGHT or event.key==pg.K_d:
                playerX_change = 4
            if event.key==pg.K_UP or event.key==pg.K_w:
                playerY_change = -4
            if event.key==pg.K_DOWN or event.key==pg.K_s:
                playerY_change = 4
            if event.key == pg.K_LCTRL:
                playerX = 368
                playerY = 480
            if event.key == pg.K_SPACE:
                fire_bullet(playerX, playerY)

        if event.type == pg.KEYUP:
            if event.key==pg.K_LEFT or event.key==pg.K_a or event.key==pg.K_RIGHT or event.key==pg.K_d:
                playerX_change = 0
            if event.key==pg.K_UP or event.key==pg.K_w or event.key==pg.K_DOWN or event.key==pg.K_s:
                playerY_change = 0
            if event.key == pg.K_LCTRL:
                playerX = 368
                playerY = 480

    # Boundaries of the player
    if playerX < -16: # Left Boundary
        playerX = -16
    elif playerX > 752: # Right Boundary
        playerX = 752
    elif playerY > 536: # Bottom Boundary
        playerY = 536
    elif playerY < 400: # Top Boundary
        playerY = 400

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)

    # Movement of the enemey
    if enemyX <= 0:
        enemyX_change = 2.5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2.5
        enemyY += enemyY_change

    enemyX += enemyX_change
    enemy(enemyX, enemyY)

    # Bullet movement
    if bulletState == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change
    
    pg.display.update()