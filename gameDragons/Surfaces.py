import pygame

class Surfaces:
    def __init__(self):
        self.bodyDragon = pygame.image.load('Sprites/SpriteBody.png').convert_alpha()
        self.headDragon = pygame.image.load('Sprites/SpriteHead.png').convert_alpha()
        self.tailDragon = pygame.image.load('Sprites/SpriteTail.png').convert_alpha()

        self.headDOWN = pygame.transform.rotate(self.headDragon.subsurface((0,0),(32,32)), 0)
        self.headRIGHT = pygame.transform.rotate(self.headDragon.subsurface((0,0),(32,32)), 90)
        self.headUP = pygame.transform.rotate(self.headDragon.subsurface((0,0),(32,32)), 180)
        self.headLEFT = pygame.transform.rotate(self.headDragon.subsurface((0,0),(32,32)), 270)

        self.bodyDOWN = pygame.transform.rotate(self.bodyDragon.subsurface((0,0),(32,32)), 0)
        self.bodyRIGHT = pygame.transform.rotate(self.bodyDragon.subsurface((0,0),(32,32)), 90)
        self.bodyUP = pygame.transform.rotate(self.bodyDragon.subsurface((0,0),(32,32)), 180)
        self.bodyLEFT = pygame.transform.rotate(self.bodyDragon.subsurface((0,0),(32,32)), 270)
        #self.bodyC1
        #self.bodyC2
        #self.bodyC3
        #self.bodyC4

        self.tailDOWN = pygame.transform.rotate(self.tailDragon.subsurface((0,0),(32,32)), 0)
        self.tailRIGHT = pygame.transform.rotate(self.tailDragon.subsurface((0,0),(32,32)), 90)
        self.tailUP = pygame.transform.rotate(self.tailDragon.subsurface((0,0),(32,32)), 180)
        self.tailLEFT = pygame.transform.rotate(self.tailDragon.subsurface((0,0),(32,32)), 270)

