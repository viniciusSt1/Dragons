import pygame, random
from gameDragons import *
from gameDragons.Sounds import Sounds
from gameDragons.Dragon import Dragon
from gameDragons.gameDisplay import gameDisplay
from gameDragons.Food import Food
from gameDragons.Events import Events

class Runner:
    def __init__(self):
        self.som = Sounds()
        self.display = gameDisplay()
        self.dragon = Dragon()
        self.food = Food([random.randrange(1, (self.display.size[0]//10)) * 10, random.randrange(1, (self.display.size[1]//10)) * 10])
        self.events = Events()

        self.score=0

        self.fps_controller = pygame.time.Clock()

        self.run()

    def run(self):
        self.som.ambienceMusic1.play(-1)
        
        while True:
            self.events.checker(self.dragon)    #verifica os eventos vindos do teclado

            self.display.window.fill(black)     #pinta a tela de preto

            if(self.dragon.update(self.display.size)):  #atualiza estado/posição do dragao, return true = morreu
                self.som.ambienceMusic1.stop()
                self.som.gameover1.play()
                self.display.game_over(self.score)

            # Verificando se o dragao comeu a comida
            if self.dragon.eat(self.food.position):
                self.som.eat.play()
                self.food.spawm_food(self.display.size)    #respawnando a comida
                self.score+=1
            
            # setando os blocos do dragao na tela
            for pos in self.dragon.body:
                pygame.draw.rect(self.display.window, green, pygame.Rect(pos[0], pos[1], 10, 10))
            
            # setando a comida na tela
            pygame.draw.rect(self.display.window, white, pygame.Rect(self.food.position[0], self.food.position[1], 10, 10))

            self.display.show_score(1, white, 'consolas', 20, self.score)   # mostrando score na tela

            pygame.display.update()             # atualizando (desenhando) a tela com tudo setado
            
            self.fps_controller.tick(difficulty)
    

    