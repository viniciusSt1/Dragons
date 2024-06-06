import pygame, random
from gameDragons import *
from gameDragons.Sounds import Sounds
from gameDragons.Dragon import Dragon
from gameDragons.gameDisplay import gameDisplay
from gameDragons.Food import Food
from gameDragons.Events import Events
from gameDragons.Surfaces import Surfaces
from gameDragons.Dao import Dao

class Runner:
    def __init__(self):
        self.som = Sounds()
        self.display = gameDisplay()
        self.dragon = Dragon()
        self.food = Food([random.randrange(1, (self.display.size[0]//grid_tam)) * grid_tam, random.randrange(1, (self.display.size[1]//grid_tam)) * grid_tam])
        self.events = Events()
        self.surf = Surfaces()
        self.dao = Dao()

        self.score=0

        self.fps_controller = pygame.time.Clock()

        self.inicio()
    
    def inicio(self):
        action = self.display.tela_inicial(self.surf,self.som,self.events)
        
        self.run() if action == 'start_game' else self.load_data()
    
    def load_data(self):
        self.dao.getDados(self.dragon, self.food)
        
        self.run()

    def run(self):
        self.som.ambienceMusic1.play(-1)
        
        while True:
            action = self.events.checker(self.dragon)    #verifica os eventos vindos do teclado
            if action == 'save':
                self.dao.saveDados(self.dragon, self.food)
                break

            self.display.set_background(self.surf)     #pinta a tela de preto

            # Verificando se o dragao comeu a comida
            if self.dragon.eat(self.food.position):
                self.som.eat.play()
                self.food.spawm_food(self.display.size)    #respawnando a comida
                self.score+=1

            if self.dragon.update(self.display.size):  #atualiza estado/posição do dragao, return true = morreu
                self.som.ambienceMusic1.stop()
                self.som.gameover1.play()
                self.display.game_over(self.score)

            # setando os blocos do dragao na tela
            self.dragon.draw_dragon(self.display,self.surf)

            # setando a comida na tela
            self.food.draw_food(self.display,self.surf)
            
            self.display.show_score(1, white, 'consolas', 20, self.score)   # mostrando score na tela

            pygame.display.update()             # atualizando (desenhando) a tela com tudo setado

            self.fps_controller.tick(difficulty)
    

    