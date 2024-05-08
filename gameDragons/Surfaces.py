import pygame

class Surfaces:
    def __init__(self):
        self.background1 = pygame.image.load('Backgrounds/1.jpg')
        self.background2 = pygame.image.load('Backgrounds/2.png')
        self.background3 = pygame.image.load('Backgrounds/3.png')
        self.background4 = pygame.image.load('Backgrounds/4.png')
        self.background5 = pygame.image.load('Backgrounds/5.png')

        self.dragonFruit = pygame.image.load('Sprites/DragonFruit.png').convert_alpha()
        self.dragonSprites = pygame.image.load('Sprites/DragonSprite.png').convert_alpha()

        self.headRIGHT = pygame.transform.rotate(self.dragonSprites.subsurface((68,94),(37,32)), 0)
        self.headUP = pygame.transform.rotate(self.dragonSprites.subsurface((68,94),(37,32)), 90)
        self.headLEFT = pygame.transform.rotate(self.dragonSprites.subsurface((68,94),(37,32)), 180)
        self.headDOWN = pygame.transform.rotate(self.dragonSprites.subsurface((68,94),(37,32)), 270)

        self.bodyDOWN = pygame.transform.rotate(self.dragonSprites.subsurface((35,61),(32,32)), 0)
        self.bodyRIGHT = pygame.transform.rotate(self.dragonSprites.subsurface((35,61),(32,32)), 90)
        self.bodyUP = pygame.transform.rotate(self.dragonSprites.subsurface((35,61),(32,32)), 180)
        self.bodyLEFT = pygame.transform.rotate(self.dragonSprites.subsurface((35,61),(32,32)), 270)

        self.bodyC3 = pygame.transform.rotate(self.dragonSprites.subsurface((35,94),(32,32)), 0)
        self.bodyC4 = pygame.transform.rotate(self.dragonSprites.subsurface((35,94),(32,32)), 90)
        self.bodyC2 = pygame.transform.rotate(self.dragonSprites.subsurface((35,94),(32,32)), 180)
        self.bodyC1 = pygame.transform.rotate(self.dragonSprites.subsurface((35,94),(32,32)), 270)

        self.tailDOWN = pygame.transform.rotate(self.dragonSprites.subsurface((35,28),(32,32)), 0)
        self.tailRIGHT = pygame.transform.rotate(self.dragonSprites.subsurface((35,28),(32,32)), 90)
        self.tailUP = pygame.transform.rotate(self.dragonSprites.subsurface((35,28),(32,32)), 180)
        self.tailLEFT = pygame.transform.rotate(self.dragonSprites.subsurface((35,28),(32,32)), 270)

    def get_retangle_transparente(self,largura,altura,transparencia,cor):
        retangulo_transparente = pygame.Surface((largura, altura))
        retangulo_transparente.set_alpha(transparencia)
        retangulo_transparente.fill(cor)

        return retangulo_transparente
