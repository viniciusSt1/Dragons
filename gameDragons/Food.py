import random

class Food:
    def __init__(self, coords):
        self.position = coords

    def spawn_food(self, display_size, snake_positions):
        while True:
            x = random.randrange(1, (display_size[0] // 32)) * 32
            y = random.randrange(1, (display_size[1] // 32)) * 32
            self.position = [x, y]

            # Check if food position overlaps with snake positions
            if self.position not in snake_positions:
                break

    def draw_food(self, display, surf):
        display.window.blit(surf.dragonFruit, self.position)

    def to_dict(self):
        return {
            'position': self.position
        }
