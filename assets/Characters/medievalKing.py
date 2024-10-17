import pygame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's Fight!")
SIZEX = 160
SIZEY = 111
SCALEX = 2.8
SCALEY = 3.3
OFFSET1 = [70, 50]
OFFSET2 = [61, 50]
DATA = [SIZEX, SIZEY, SCALEX, SCALEY, OFFSET1]
ANIMATION_STEPS = [8, 8, 2, 4, 4, 4, 4, 6]
#load spritesheets
sheet = pygame.image.load("assets/images/Medieval King Pack 2/Sprites/MedievalKing.png").convert_alpha()