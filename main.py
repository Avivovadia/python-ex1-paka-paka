from Player import Player
import pygame

pygame.init()

screen = pygame.display.set_mode((1300, 670))
pygame.display.set_caption("GAME")
monkeyX = 200
monkeyY = 200

monkeyimg = pygame.image.load("Images/animal.png")
font = pygame.font.SysFont('candara', 80)
text = font.render("Ready to Start?", True, (0, 0, 0))
running = True

print(screen.get_size())
monkeyX_change=0
monkeyY_change=0
monkey_speed=0.5

def monkey(x, y):
    screen.blit(monkeyimg, (x, y))


while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        #closing the game
        if event.type == pygame.QUIT:
            running = False
        #movement mechanics
        if event.type==pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
               monkeyY_change = monkey_speed
             if event.key == pygame.K_UP:
               monkeyY_change = -monkey_speed
             if event.key == pygame.K_RIGHT:
               monkeyX_change = monkey_speed
             if event.key == pygame.K_LEFT:
               monkeyX_change = -monkey_speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                monkeyX_change=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                monkeyY_change=0

    monkeyX+=monkeyX_change
    monkeyY+=monkeyY_change
    if monkeyX>screen.get_size()[0]-32:
        monkeyX=screen.get_size()[0]-32
    if monkeyY > screen.get_size()[1]-32:
        monkeyY = screen.get_size()[1]-32
    if monkeyX<0:
        monkeyX=0
    if monkeyY<0:
        monkeyY=0
    screen.blit(text, (400, 200))
    monkey(monkeyX, monkeyY)

    pygame.display.update()
