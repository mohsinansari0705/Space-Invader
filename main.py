import pygame as pg
import random
import math

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

# Enemies list
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
    enemyImg.append(pg.image.load("enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 236))
    enemyX_change.append(2.5)
    enemyY_change.append(32)

# Bullet
bulletImg = pg.image.load("bullet.png")
bulletX = 0
bulletY = 0
bulletY_change = 10
bulletState = "ready"

# Score of the player
score_value = 0
font = pg.font.Font('font_Consolas.ttf', 16)
textX = 10 # Coordinates of the text on the screen
textY = 10

# Function for rendering the score on the screen
def show_score(x, y):
    score = font.render("Score : "+str(score_value), True, (233, 233, 233))
    screen.blit(score, (x, y))

# Player randering Function
def player(x, y):
    screen.blit(playerImg, (x, y))
    
# Enemy randering Function
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Bullet firing & randering Function
def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x+24, y-5))

# Checking the collision of bullet & the enemey
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX), 2) + math.pow((enemyY-bulletY), 2))

    # Check if distance is within collision threshold=40
    if distance<=40:
        return True
    else:
        return False

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
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX, playerY)

        if event.type == pg.KEYUP:
            if event.key==pg.K_LEFT or event.key==pg.K_a or event.key==pg.K_RIGHT or event.key==pg.K_d:
                playerX_change = 0
            if event.key==pg.K_UP or event.key==pg.K_w or event.key==pg.K_DOWN or event.key==pg.K_s:
                playerY_change = 0
            if event.key == pg.K_LCTRL:
                playerX = 368
                playerY = 480

    # Randering the score on the screen
    show_score(textX, textY)

    # Limit the boundaries of the player
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

    # Movement of the enemies
    for i in range(number_of_enemies):
        if enemyX[i] <= 0:
            enemyX_change[i] = 2.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2.5
            enemyY[i] += enemyY_change[i]

        enemyX[i] += enemyX_change[i]
        enemy(enemyX[i], enemyY[i], i)

        # Collision detection
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            score_value += 1
            bulletX = playerX
            bulletY = playerY
            bulletState = "ready"
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(0, 236)

    # Bullet movement
    if bulletState == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"
    
    pg.display.update()