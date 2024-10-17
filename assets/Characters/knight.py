import pygame
SIZEX = 96
SIZEY = 84
SCALEX = 5
SCALEY = 5
OFFSET1 = [40, 25]
OFFSET2 = [40, 25]
DATA = [SIZEX, SIZEY, SCALEX, SCALEY, OFFSET2]
ANIMATION_STEPS = [7, 8, 5, 5, 6, 6, 4, 12]
#load spritesheets
sheet = pygame.image.load("assets/images/Knight/Sprites/with_outline/Knight.png").convert_alpha()