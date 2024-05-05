import random

class Food:
    def __init__(self,coords):
        self.position = coords

    def spawm_food(self,display_size):
        self.position = [random.randrange(1, (display_size[0]//32)) * 32, random.randrange(1, (display_size[1]//32)) * 32]
    
    def draw_food(self,display,surf):
        display.window.blit(surf.dragonFruit, self.position)