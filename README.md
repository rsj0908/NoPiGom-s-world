# NoPiGom-s-world
# Create pygame

import pygame, sys

def moving():
    global y_change, x_change, x, y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            y_change = y_change + 30
        if event.key == pygame.K_UP:
            y_change = y_change - 30
        if event.key == pygame.K_LEFT:
            x_change = x_change - 30
        if event.key == pygame.K_RIGHT:
            x_change = x_change + 30
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
            event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0
            y_change = 0

    x += x_change
    y += y_change


def can_t_out():
    global x,y
    if x < 0:
        x = 0
    elif x > 462:
        x = 462
    elif y < 0:
        y = 0
    elif y > 462:
        y = 462

def ene_reflect():
    global x_ene_change, y_ene_change, x_ene, y_ene
    if x_ene < 0:
        x_ene_change = -x_ene_change
    elif x_ene > 462:
        x_ene_change = -x_ene_change
    elif y_ene < 0:
        y_ene_change = -y_ene_change
    elif y_ene > 462:
        y_ene_change = -y_ene_change

    x_ene += x_ene_change
    y_ene += y_ene_change




White = (255,255,255)
wid = 512
hei = 512
pygame.init()
display = pygame.display.set_mode((wid,hei))
pygame.display.set_caption("game")
whale = pygame.image.load('whale.png')
whale_ene = pygame.image.load('whale.png')
whale = pygame.transform.scale(whale,(50,50))
whale_ene = pygame.transform.scale(whale_ene,(50,50))
whale_ene2 = pygame.image.load('whale.png')
whale_ene2 = pygame.transform.scale(whale_ene2,(50,50))
y_change = 0
x_change = 0
x = wid * 0.05
y = hei * 0.5
x_ene = 0
y_ene = 30
x_ene_change = 0.05
y_ene_change = 0.05

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        moving()
        can_t_out()

    ene_reflect()
    pygame.display.update()
    display.fill(White)
    display.blit(whale,(x,y))
    display.blit(whale_ene,(x_ene,y_ene))

