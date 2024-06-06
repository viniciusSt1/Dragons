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

        self.window = pygame.display.set_mode(self.size, pygame.DOUBLEBUF)
        self.window.set_alpha(None)

        pygame.mouse.set_visible(False)
    
    def tela_inicial(self, surf, song , events):
        song.ambienceMusic2.play(-1)

        clock = pygame.time.Clock()
        altura_button = 90
        largura_button = 420
        
        menu_font = pygame.font.SysFont('Tahoma', 40)
        menu_color = (255, 255, 255)
        menu_text_newgame = menu_font.render("Enter - Novo Jogo", True, menu_color)
        menu_text_save = menu_font.render("S - Último save", True, menu_color)

        menu_text_newgame_rect = menu_text_newgame.get_rect(center=(self.size[0]//2,self.size[1]//2-60))
        menu_text_save_rect = menu_text_save.get_rect(center=(self.size[0]//2,self.size[1]//2+60))

        self.window.blit(surf.background1, (0,0))

        retangulo = surf.get_retangle_transparente(largura_button, altura_button, 200, (0,0,0))  
    
        self.window.blit(retangulo, ((self.size[0]-largura_button)//2, (self.size[1]-altura_button)//2 - 60))   
        self.window.blit(menu_text_newgame, menu_text_newgame_rect)

        self.window.blit(retangulo, ((self.size[0]-largura_button)//2, (self.size[1]-altura_button)//2 + 60))
        self.window.blit(menu_text_save, menu_text_save_rect)
            
        pygame.display.flip()

        while True:
            buttonclick = events.gameStart()
            if buttonclick == 'start_game' or buttonclick == 'load_save':
                song.ambienceMusic2.stop()
                return buttonclick

            clock.tick(60)
        
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

    def set_background(self, surf):
        self.window.blit(surf.background3, (0,0))
