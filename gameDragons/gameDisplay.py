import pygame,time,sys
from . import *

class gameDisplay:
    def __init__(self,fps:int=10,fullScreen:bool=False,name:str="Dragons",disp_size=(1120,672)):
        self.fps=fps
        self.fullScreen=fullScreen
        self.name=name
        self.size = disp_size

        self._setup_display()

    def _setup_display(self):
        pygame.display.set_caption(self.name)

        self.window = pygame.display.set_mode(self.size)

        pygame.mouse.set_visible(False)
    
    def game_over(self, score):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.size[0]/2, self.size[1]/4)
        self.window.fill(black)
        self.window.blit(game_over_surface, game_over_rect)
        self.show_score(0, red, 'times', 20, score)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
    
    def show_score(self,choice, color, font, size, score):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (self.size[0]/10, 15)
        else:
            score_rect.midtop = (self.size[0]/2, self.size[1]/1.25)
        self.window.blit(score_surface, score_rect)
        # pygame.display.flip()

