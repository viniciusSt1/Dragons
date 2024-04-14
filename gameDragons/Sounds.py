import pygame

class Sounds:
    def __init__(self):
        self.ambienceMusic1 = pygame.mixer.Sound("SFX/ambience1.mp3")
        self.ambienceMusic2 = pygame.mixer.Sound("SFX/ambience2.mp3")
        self.ambienceMusic3 = pygame.mixer.Sound("SFX/ambience3.mp3")
        self.ambienceMusic4 = pygame.mixer.Sound("SFX/ambience4.mp3")
        self.eat = pygame.mixer.Sound("SFX/eat.mp3")
        self.gameover1 = pygame.mixer.Sound("SFX/gameover1.mp3")
        self.gameover2 = pygame.mixer.Sound("SFX/gameover2.mp3")


