import pygame
from gameDragons import red

class Dragon:
    def __init__(self,coordsInicio=[96,32], bodyDragon=[[96, 32], [64, 32], [32, 32]], directionInicio="RIGHT", direction_blocks=['RIGHT','RIGHT','RIGHT']):
        #body block = 32px x 32px -> grid layout
        
        self.body = bodyDragon
        self.position = coordsInicio
        self.direction = directionInicio    #RIGHT, UP, LEFT, DOWN
        self.last_direction = self.direction    #ultima direção que o dragao andou
        self.direction_blocks = direction_blocks    #: RIGHT, UP, LEFT, DOWN, c1, c2, c3, c4 
        self.eatState = False

    def change_direction(self,direction:str):
        #Verificando direção atual para mudar somente em casos válidos
        #Atualizando o valor de direction_blocks do pescoço para fazer a curva
        if direction == 'UP' and self.last_direction != 'DOWN' and self.last_direction != 'UP':
            self.direction = 'UP'

            if(self.last_direction == 'RIGHT'):     #adiciona a direção de uma curva
                self.direction_blocks[0] = 'c4'
            elif(self.last_direction == 'LEFT'):
                self.direction_blocks[0] = 'c3'
                
        elif direction == 'DOWN' and self.last_direction != 'UP' and self.last_direction != 'DOWN':
            self.direction = 'DOWN'
            
            if(self.last_direction == 'RIGHT'):     #adiciona a direção de uma curva
                self.direction_blocks[0] = 'c2'
            elif(self.last_direction == 'LEFT'):
                self.direction_blocks[0] = 'c1'

        elif direction == 'LEFT' and self.last_direction != 'RIGHT' and self.last_direction != 'LEFT':
            self.direction = 'LEFT'
            
            if(self.last_direction == 'UP'):        #adiciona a direção de uma curva
                self.direction_blocks[0] = 'c2'
            elif(self.last_direction == 'DOWN'):
                self.direction_blocks[0] = 'c4'

        elif direction == 'RIGHT' and self.last_direction != 'LEFT' and self.last_direction != 'RIGHT':
            self.direction = 'RIGHT'
            
            if(self.last_direction == 'UP'):        #adiciona a direção de uma curva
                self.direction_blocks[0] = 'c1'
            elif(self.last_direction == 'DOWN'):
                self.direction_blocks[0] = 'c3'

    def move(self):
        if self.direction == 'UP':
            self.position[1] -= 32  #posição y
        if self.direction == 'DOWN':
            self.position[1] += 32  #posição y
        if self.direction == 'LEFT':
            self.position[0] -= 32  #posição x
        if self.direction == 'RIGHT':
            self.position[0] += 32 #posição x

        self.last_direction = self.direction
    
    def eat(self,foodPosition):
        if self.position == foodPosition:
            self.direction_blocks.insert(0,self.direction)      #adiciona mais uma direção de um bloco (cabeça)
            self.eatState = True
        else:
            self.eatState = False
            self.body.pop()

        return self.eatState
    
    def update(self,display_size):
        self.move()
        self.body.insert(0, list(self.position))
        
        if(not self.eatState):
            for index in range(len(self.direction_blocks)-1,-1,-1):     #atualizando a direção dos blocos
                #if(index == len(self.direction_blocks)):
                #    if(self.direction_blocks[index] == 'c1' or self.direction_blocks[index] == 'c2' or self.direction_blocks[index] == 'c3' or self.direction_blocks[index] == 'c4'):
                #        self.direction_blocks[index] = self.direction_blocks[index-2]
                #else:
                self.direction_blocks[index] = self.direction_blocks[index-1]

        self.direction_blocks[0] = self.direction                   #atualizando a direção da cabeça
        #print(self.direction_blocks)
        
        # Game Over conditions

        # Getting out of bounds
        if self.position[0] < 0 or self.position[0] > display_size[0]-32:
            print("Para fora da tela")
            return True
        if self.position[1] < 0 or self.position[1] > display_size[1]-32:
            print("Para fora da tela")
            return True


        # Touching the snake body
        for block in self.body[1:]:
            if self.position == block:
                print("Tocou no seu corpo")
                return True
            
        return False    #tudo ok
    
    def draw_dragon(self, display,surf):
        for index, pos in enumerate(self.body): #desenhando bloco a bloco de acordo com suas direções
            if index == 0:
                match self.direction_blocks[0]:
                    case 'DOWN': display.window.blit(surf.headDOWN, pos)
                    case 'RIGHT': display.window.blit(surf.headRIGHT, pos)
                    case 'UP': display.window.blit(surf.headUP, pos)
                    case 'LEFT': display.window.blit(surf.headLEFT, pos)
            elif index < len(self.body)-1:
                match self.direction_blocks[index]:
                    case 'DOWN': display.window.blit(surf.bodyDOWN, pos)
                    case 'RIGHT': display.window.blit(surf.bodyRIGHT, pos)
                    case 'UP': display.window.blit(surf.bodyUP, pos)
                    case 'LEFT': display.window.blit(surf.bodyLEFT, pos)
                    case 'c1': display.window.blit(surf.bodyC1, pos)
                    case 'c2': display.window.blit(surf.bodyC2, pos)
                    case 'c3': display.window.blit(surf.bodyC3, pos)
                    case 'c4': display.window.blit(surf.bodyC4, pos)
            else:
                match self.direction_blocks[index]:    #tail
                    case 'DOWN': display.window.blit(surf.tailDOWN,pos)
                    case 'RIGHT': display.window.blit(surf.tailRIGHT,pos)
                    case 'UP': display.window.blit(surf.tailUP,pos)
                    case 'LEFT': display.window.blit(surf.tailLEFT,pos)