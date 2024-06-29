import pygame

class Surfaces:
    def __init__(self):
        self.background_menu = pygame.image.load('Backgrounds/menu.jpg')
        self.backgrounds_game = [
            pygame.image.load('Backgrounds/bgame1.png'),
            pygame.image.load('Backgrounds/bgame2.png'),
            pygame.image.load('Backgrounds/bgame3.jpeg')
        ]
        self.backgrounds_loading = [
            pygame.image.load('Backgrounds/bloading1.jpeg'),
            pygame.image.load('Backgrounds/bloading2.png')
        ]

        self.backgrounds_gameover = [
            pygame.image.load('Backgrounds/gameover1.jpeg'),
            pygame.image.load('Backgrounds/gameover2.jpeg')
        ]

        self.backgrounds_win = [
            pygame.image.load('Backgrounds/win1.jpeg'),
            pygame.image.load('Backgrounds/win2.jpeg')
        ]
        
        self.loading_bar = pygame.image.load("Backgrounds/Loading Bar.png")

        self.dragonFruit = pygame.image.load('Sprites/DragonFruit.png').convert_alpha()
        self.BlueDragonSprites = pygame.image.load('Sprites/BlueDragonSprites.png').convert_alpha()
        self.RedDragonSprites = pygame.image.load('Sprites/RedDragonSprites.png').convert_alpha()

        self.blue_dragon_sprites = {
            'head': {
                'RIGHT': pygame.transform.rotate(self.BlueDragonSprites.subsurface((68, 94, 37, 32)), 0),
                'UP': pygame.transform.rotate(self.BlueDragonSprites.subsurface((68, 94, 37, 32)), 90),
                'LEFT': pygame.transform.rotate(self.BlueDragonSprites.subsurface((68, 94, 37, 32)), 180),
                'DOWN': pygame.transform.rotate(self.BlueDragonSprites.subsurface((68, 94, 37, 32)), 270)
            },
            'body': {
                'DOWN': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 61, 32, 32)), 0),
                'RIGHT': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 61, 32, 32)), 90),
                'UP': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 61, 32, 32)), 180),
                'LEFT': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 61, 32, 32)), 270)
            },
            'bodyC': {
                'C3': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 94, 32, 32)), 0),
                'C4': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 94, 32, 32)), 90),
                'C2': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 94, 32, 32)), 180),
                'C1': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 94, 32, 32)), 270)
            },
            'tail': {
                'DOWN': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 28, 32, 32)), 0),
                'RIGHT': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 28, 32, 32)), 90),
                'UP': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 28, 32, 32)), 180),
                'LEFT': pygame.transform.rotate(self.BlueDragonSprites.subsurface((35, 28, 32, 32)), 270)
            }
        }

        self.red_dragon_sprites = {
            'head': {
                'RIGHT': pygame.transform.rotate(self.RedDragonSprites.subsurface((68, 94, 37, 32)), 0),
                'UP': pygame.transform.rotate(self.RedDragonSprites.subsurface((68, 94, 37, 32)), 90),
                'LEFT': pygame.transform.rotate(self.RedDragonSprites.subsurface((68, 94, 37, 32)), 180),
                'DOWN': pygame.transform.rotate(self.RedDragonSprites.subsurface((68, 94, 37, 32)), 270)
            },
            'body': {
                'DOWN': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 61, 32, 32)), 0),
                'RIGHT': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 61, 32, 32)), 90),
                'UP': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 61, 32, 32)), 180),
                'LEFT': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 61, 32, 32)), 270)
            },
            'bodyC': {
                'C3': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 94, 32, 32)), 0),
                'C4': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 94, 32, 32)), 90),
                'C2': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 94, 32, 32)), 180),
                'C1': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 94, 32, 32)), 270)
            },
            'tail': {
                'DOWN': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 28, 32, 32)), 0),
                'RIGHT': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 28, 32, 32)), 90),
                'UP': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 28, 32, 32)), 180),
                'LEFT': pygame.transform.rotate(self.RedDragonSprites.subsurface((35, 28, 32, 32)), 270)
            }
        }

    def get_retangle_transparente(self,largura,altura,transparencia,cor):
        retangulo_transparente = pygame.Surface((largura, altura))
        retangulo_transparente.set_alpha(transparencia)
        retangulo_transparente.fill(cor)

        return retangulo_transparente
