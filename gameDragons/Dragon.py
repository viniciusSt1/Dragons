class Dragon:
    def __init__(self,coordsInicio=[100,50], bodyDragon=[[100, 50], [90, 50], [80, 50]], directionInicio="RIGHT"):
        #body block = 10px x 10px
        self.body = bodyDragon
        self.position = coordsInicio
        self.direction = directionInicio

    def change_direction(self,direction:str):
        #Verificando direção atual para mudar somente em casos válidos
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def move(self):
        if self.direction == 'UP':
            self.position[1] -= 10  #posição y
        if self.direction == 'DOWN':
            self.position[1] += 10  #posição y
        if self.direction == 'LEFT':
            self.position[0] -= 10  #posição x
        if self.direction == 'RIGHT':
            self.position[0] += 10 #posição x
    
    def eat(self,foodPosition):
        if self.position[0] == foodPosition[0] and self.position[1] == foodPosition[1]:
            return True
        else:
            self.body.pop()
            return False
    
    def update(self,display_size):
        self.move()
        self.body.insert(0, list(self.position))

        # Game Over conditions

        # Getting out of bounds
        if self.position[0] < 0 or self.position[0] > display_size[0]-10:
            return True
        if self.position[1] < 0 or self.position[1] > display_size[1]-10:
            return True

        # Touching the snake body
        for block in self.body[1:]:
            if self.position[0] == block[0] and self.position[1] == block[1]:
                return True
            
        return False    #tudo ok