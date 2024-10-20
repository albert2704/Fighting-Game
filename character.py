import pygame
from pygame import mixer
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
mixer.init()
class Character():
    def __init__(self, name, sizeX, sizeY, scaleX, scaleY, offSet1, offSet2, animation_steps, sheet, sound):
        self.name = name
        self.SIZEX = sizeX
        self.SIZEY = sizeY
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.OFFSET1 = offSet1
        self.OFFSET2 = offSet2
        self.animation_steps = animation_steps
        self.sheet = sheet
        self.sound = sound
        
characters = {
    'knight': Character('knight', 96, 84, 5, 5, [40, 25], [40, 25], [7, 8, 5, 5, 6, 6, 4, 12], pygame.image.load("assets/images/Knight/Sprites/with_outline/Knight.png").convert_alpha(), pygame.mixer.Sound("assets/audio/sword.wav")),
    'martialHero': Character('martialHero', 126, 126, 4, 4, [65, 37], [43, 37], [10, 8, 3, 9, 7, 6, 3, 11], pygame.image.load("assets/images/Martial Hero 3/Sprite/martialHero.png").convert_alpha(), pygame.mixer.Sound("assets/audio/sword.wav")),
    'medievalKing': Character('medievalKing', 160, 111, 2.8, 3.3, [70, 50], [61, 50], [8, 8, 2, 4, 4, 4, 4, 6], pygame.image.load("assets/images/Medieval King Pack 2/Sprites/MedievalKing.png").convert_alpha(), pygame.mixer.Sound("assets/audio/sword.wav")),
    'medievalKnight': Character('medievalKnight', 184, 137, 2, 2, [65, 35], [75, 35], [6, 8, 2, 4, 4, 4, 3, 9], pygame.image.load("assets/images/Medieval Warrior Pack/MedievalKnight.png").convert_alpha(), pygame.mixer.Sound("assets/audio/sword.wav")),
    'warrior': Character('warrior', 162, 162, 4, 4, [72, 56], [68, 56], [10, 8, 3, 7, 7, 8, 3, 7], pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha(), pygame.mixer.Sound("assets/audio/sword.wav")),
    'huntress': Character('huntress', 150, 150, 4, 4, [65, 52], [65, 52], [8, 8, 2, 5, 5, 7, 3, 8], pygame.image.load("assets/images/Huntress/Sprites/Huntress.png").convert_alpha(), pygame.mixer.Sound("assets/audio/sword.wav"))
}