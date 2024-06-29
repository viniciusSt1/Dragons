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
        self.dragon1 = Dragon()
        self.dragon2 = None
        self.food = Food(None)
        self.events = Events()
        self.surf = Surfaces()
        self.dao = Dao()
        self.multiplayer = True
        self.backnum = random.choice([2,3,4])

        self.score=0

        self.fps_controller = pygame.time.Clock()

        self.inicio()
    
    def inicio(self):
        action = self.display.tela_inicial(self.surf,self.som, self.events)

        if action == 'load_save':
            self.load_data()
        else:
            self.dragon1 = Dragon(coordsInicio=[96,32], bodyDragon=[[96, 32], [64, 32], [32, 32]], directionInicio="RIGHT", direction_blocks=['RIGHT','RIGHT','RIGHT'], color='blue')
            self.food = Food([random.randrange(1, (self.display.size[0]//grid_tam)) * grid_tam, random.randrange(1, (self.display.size[1]//grid_tam)) * grid_tam])
            
            if action == 'start_1player':
                self.multiplayer = False
                self.dragon2 = None
            else:
                self.dragon2 = Dragon(coordsInicio=[960,608], bodyDragon=[[960,608], [960,608], [960,608]], directionInicio='LEFT', direction_blocks=['LEFT','LEFT','LEFT'], color='red')
                self.multiplayer = True

            self.run() 

    def load_data(self):
        self.dao.getDados(self.dragon1, self.food)
        self.dragon2 = None
        self.multiplayer = False

        self.run()

    def run(self):
        self.som.ambienceMusic1.play(-1)
        self.backnum = random.choice([2,3,4])
        
        while True:
            action = self.events.checker(self.dragon1,self.dragon2)        #verifica os eventos vindos do teclado

            if action == 'pause':
                if not self.multiplayer:
                    self.dao.saveDados(self.dragon1, self.food)

                self.display.game_paused(self.surf)
                waiting=True
                while waiting:
                    if self.events.despause():
                        waiting = False

            self.display.set_background(self.surf,self.backnum)     #Desenha o background

            # Verificando se o dragao comeu a comida
            if self.dragon1.eat(self.food.position):
                self.som.eat.play()
                self.food.spawm_food(self.display.size)    #respawnando a comida
                self.score+=1
            
            if self.dragon2 != None and self.dragon2.eat(self.food.position):
                self.som.eat.play()
                self.food.spawm_food(self.display.size)    #respawnando a comida
                self.score+=1

            if self.dragon1.update(self.display.size, self.dragon2):  #atualiza estado/posição do dragao, return true = morreu
                self.som.ambienceMusic1.stop()
                self.som.gameover1.play()
                if(self.dragon2 != None):
                    msg = 'Dragão Vermelho' if self.dragon1.position != self.dragon2.position else 'Empate'
                    self.display.game_over(self.surf,self.score, self.inicio, ganhador = msg)
                else:
                    self.display.game_over(self.surf,self.score, self.inicio, ganhador = 'any')

            if self.dragon2 != None and self.dragon2.update(self.display.size, self.dragon1):  #atualiza estado/posição do dragao, return true = morreu
                self.som.ambienceMusic1.stop()
                self.som.gameover1.play()
                msg = 'Dragão Azul' if self.dragon1.position != self.dragon2.position else 'Empate'
                self.display.game_over(self.surf, self.score, self.inicio, ganhador = msg)

            # setando os blocos do dragao na tela
            self.dragon1.draw_dragon(self.display,self.surf)

            if(self.dragon2 != None):
                self.dragon2.draw_dragon(self.display,self.surf)

            # setando a comida na tela
            self.food.draw_food(self.display,self.surf)
            
            if self.dragon2 == None:
                self.display.show_score(1, black, 'consolas', 20, self.score)   # mostrando score na tela

            pygame.display.update()             # atualizando (desenhando) a tela com tudo setado

            self.fps_controller.tick(difficulty)
    

    