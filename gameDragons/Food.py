import random

class Food:
    def __init__(self,coords):
        self.position = coords

    def spawm_food(self,display_size):
        self.position = [random.randrange(1, (display_size[0]//10)) * 10, random.randrange(1, (display_size[1]//10)) * 10]