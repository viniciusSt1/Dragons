import pygame, time, sys, threading

class gameDisplay:
    def __init__(self, fps:int=10, fullScreen:bool=False, name:str="Dragons", disp_size=(1120, 672)):
        self.fps = fps
        self.fullScreen = fullScreen
        self.name = name
        self.size = disp_size
        self.menu_font = pygame.font.SysFont('Tahoma', 40)
        self.loading_font = pygame.font.SysFont("Roboto", 100)
        self.clock = pygame.time.Clock()

        self._setup_display()

    def _setup_display(self):
        pygame.display.set_caption(self.name)
        self.window = pygame.display.set_mode(self.size, pygame.DOUBLEBUF)
        self.window.set_alpha(None)
        pygame.mouse.set_visible(False)

    def tela_inicial(self, surf, song, events):
        song.ambienceMusic2.play(-1)
        altura_button = 90
        largura_button = 420

        menu_text_newgame = self.menu_font.render("Enter - Novo Jogo", True, "white")
        menu_text_save = self.menu_font.render("S - Último save", True, "white")

        menu_text_newgame_rect = menu_text_newgame.get_rect(center=(self.size[0]//2, self.size[1]//2-60))
        menu_text_save_rect = menu_text_save.get_rect(center=(self.size[0]//2, self.size[1]//2+60))

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
                self.tela_carregamento(surf)
                return buttonclick
            self.clock.tick(60)

    def tela_carregamento(self,surf):
        WORK = 10000000
        LOADING_BG_RECT = surf.loading_bg.get_rect(center=(self.size[0]//2, self.size[1]//2))
        loading_bar_rect = surf.loading_bar.get_rect(midleft=(self.size[0]//2, self.size[1]//2))
        loading_finished = False
        loading_progress = 0

        def doWork():
            nonlocal loading_finished, loading_progress
            for i in range(WORK):
                math_equation = 523687 / 789456 * 89456
                loading_progress = i 
            loading_finished = True

        threading.Thread(target=doWork).start()

        while not loading_finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill("#0d0e2e")
            loading_bar_width = loading_progress / WORK * 720
            loading_bar_scaled = pygame.transform.scale(surf.loading_bar, (int(loading_bar_width), 150))
            loading_bar_rect = loading_bar_scaled.get_rect(midleft=(280, 360))
            self.window.blit(surf.loading_bg, LOADING_BG_RECT)
            self.window.blit(loading_bar_scaled, loading_bar_rect)
            pygame.display.update()
            self.clock.tick(60)

        finished = self.loading_font.render("Done!", True, "white")
        finished_rect = finished.get_rect(center=(self.size[0]//2, self.size[1]//2))
        self.window.blit(finished, finished_rect)
        pygame.display.update()
        time.sleep(1)

    def game_paused(self,surf):
        background_cover = surf.get_retangle_transparente(self.size[0], self.size[1], 200, (0,0,0))
        self.window.blit(background_cover, (0, 0))

        text = self.menu_font.render("Jogo Pausado", True, "white")
        text_rect = text.get_rect(center=(self.size[0]//2, self.size[1]//2))
        self.window.blit(text, text_rect)

        pygame.display.update()

    def game_over(self, score, inicio):
        game_over_surface = self.menu_font.render('YOU DIED', True, (255, 0, 0))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.size[0]/2, self.size[1]/4)
        self.window.fill((0, 0, 0))
        self.window.blit(game_over_surface, game_over_rect)
        self.show_score(0, (255, 0, 0), 'times', 20, score)
        pygame.display.flip()
        time.sleep(3)
        inicio()

    def show_score(self, choice, color, font, size, score):
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
