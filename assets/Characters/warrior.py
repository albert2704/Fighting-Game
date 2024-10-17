import pygame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's Fight!")
SIZEX = 162
SIZEY = 162
SCALEX = 4
SCALEY = 4
OFFSET1 = [72, 56]
OFFSET2 = [68, 56]
DATA = [SIZEX, SIZEY, SCALEX, SCALEY, OFFSET1]
ANIMATION_STEPS = [10, 8, 3, 7, 7, 8, 3, 7]
#load spritesheets
sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()