import pygame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's Fight!")
SIZEX = 126
SIZEY = 126
SCALEX = 4
SCALEY = 4
OFFSET1 = [65, 37]
OFFSET2 = [43, 37]
DATA = [SIZEX, SIZEY, SCALEX, SCALEY, OFFSET1]
ANIMATION_STEPS = [10, 8, 3, 9, 7, 6, 3, 11]
#load spritesheets
sheet = pygame.image.load("assets/images/Martial Hero 3/Sprite/martialHero.png").convert_alpha()