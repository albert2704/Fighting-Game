import pygame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's Fight!")
SIZEX = 184
SIZEY = 137
SCALEX = 2
SCALEY = 2
OFFSET1 = [65, 35]
OFFSET2 = [75, 35]
DATA = [SIZEX, SIZEY, SCALEX, SCALEY, OFFSET2]
ANIMATION_STEPS = [6, 8, 2, 4, 4, 4, 3, 9]
#load spritesheets
sheet = pygame.image.load("assets/images/Medieval Warrior Pack/MedievalKnight.png").convert_alpha()