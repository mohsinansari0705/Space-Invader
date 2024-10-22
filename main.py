import pygame as pg

# Initialize the pygame
pg.init()

# Create a screen
dimentions = (800, 600) # Width & Height
screen = pg.display.set_mode(dimentions)


# Title & Icon
pg.display.set_caption("Space Invader :Devox_Network")
icon = pg.image.load("GameLogo.png")
pg.display.set_icon(icon)

# Player
playerImg = pg.image.load("player.png")
playerX = 368
playerY = 480

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
    screen.fill((23, 23, 23))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    player(playerX, playerY)
    
    pg.display.update()