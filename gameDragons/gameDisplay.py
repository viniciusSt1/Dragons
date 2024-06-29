import pygame, time, sys, threading, random
import pygame_gui

class gameDisplay:
    def __init__(self, fps:int=10, fullScreen:bool=False, name:str="Dragons", disp_size=(1120, 672)):
        self.fps = fps
        self.fullScreen = fullScreen
        self.name = name
        self.size = disp_size
        self.menu_font = pygame.font.SysFont('Tahoma', 40)
        self.dragon_font = pygame.font.SysFont("Roboto", 80)
        self.loading_font = pygame.font.SysFont("Roboto", 30)
        self.clock = pygame.time.Clock()

        self._setup_display()

    def _setup_display(self):
        pygame.display.set_caption(self.name)
        self.window = pygame.display.set_mode(self.size, pygame.DOUBLEBUF)
        self.window.set_alpha(None)
        #pygame.mouse.set_visible(False)

    def tela_inicial(self, surf, song, events):
        # Inicializa o gerenciador de interface do usuário
        manager = pygame_gui.UIManager(self.size, 'theme.json')

        song.ambienceMusic2.play(-1)
        altura_button = 75
        largura_button = 390

        # Define as posições dos botões
        pos_1player = ((self.size[0] - largura_button) // 2, (self.size[1] - altura_button) // 2 - 100)
        pos_2player = ((self.size[0] - largura_button) // 2, (self.size[1] - altura_button) // 2)
        pos_save = ((self.size[0] - largura_button) // 2, (self.size[1] - altura_button) // 2 + 100)

        # Cria os botões usando pygame_gui
        button_1player = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(pos_1player, (largura_button, altura_button)),
            text='Single Player',
            manager=manager,
            object_id="#button"
        )
        button_2player = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(pos_2player, (largura_button, altura_button)),
            text='Multiplayer',
            manager=manager,
            object_id="#button"
        )
        button_save = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(pos_save, (largura_button, altura_button)),
            text='Último save',
            manager=manager,
            object_id="#button"
        )

        while True:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Passa os eventos para o gerenciador de interface do usuário
                manager.process_events(event)

                # Verifica se algum botão foi clicado
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_1player:
                        song.ambienceMusic2.stop()
                        self.tela_carregamento(surf)
                        return 'start_1player'
                    elif event.ui_element == button_2player:
                        song.ambienceMusic2.stop()
                        self.tela_carregamento(surf)
                        return 'start_2player'
                    elif event.ui_element == button_save:
                        song.ambienceMusic2.stop()
                        self.tela_carregamento(surf)
                        return 'load_save'

            #Redesenha background
            self.set_background(surf, 1)

            # Atualiza o gerenciador de interface do usuário
            manager.update(time_delta)

            # Desenha os botões
            manager.draw_ui(self.window)

            pygame.display.flip()

    def tela_carregamento(self,surf):
        WORK = 1000
        loading_bar_rect = surf.loading_bar.get_rect(midleft=(self.size[0]//2, self.size[1]//2))
        loading_finished = False
        loading_progress = 0
        backnum = random.choice([5,6])

        def doWork():
            nonlocal loading_finished, loading_progress
            for i in range(WORK):
                loading_progress = i 
                self.clock.tick(350)
            loading_finished = True

        threading.Thread(target=doWork).start()

        while not loading_finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.set_background(surf,backnum)
            loading_bar_width = loading_progress
            loading_bar_scaled = pygame.transform.scale(surf.loading_bar, (int(loading_bar_width), 20))
            loading_bar_rect = loading_bar_scaled.get_rect(midleft=(self.size[0]//2 - loading_bar_width/2, self.size[1] - 50))
            self.window.blit(loading_bar_scaled, loading_bar_rect)
            pygame.display.update()
            self.clock.tick(60)

        finished = self.loading_font.render("Feito!", True, "white")
        finished_rect = finished.get_rect(center=(self.size[0]//2, self.size[1] - 20))
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

    def game_over(self, surf, score, inicio, ganhador):
        # Inicializa o gerenciador de interface do usuário
        manager = pygame_gui.UIManager(self.size, 'theme.json')
        altura_button = 70
        largura_button = 380

        # Define a posição do botões
        posbutton = ((self.size[0] - largura_button) // 2, self.size[1] - 120)

        buttonback = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(posbutton, (largura_button, altura_button)),
            text='Voltar ao menu',
            manager=manager,
            object_id="#button"
        )

        if ganhador == 'any':
            backgnum = random.choice([7,8])
            self.set_background(surf,backgnum)
            if backgnum == 8:
                game_over_text = self.menu_font.render('Infelizmente você morreu, Tente Novamente', True, (255, 255, 255))
                game_over_rect = surf.get_retangle_transparente(self.size[0], 100, 200, (0, 0, 0))

                self.window.blit(game_over_rect, (0, (self.size[1] - 100) // 2))

                text_rect = game_over_text.get_rect()
                text_rect.center = (self.size[0] // 2, (self.size[1] - 100) // 2 + 90 // 2) 

                self.window.blit(game_over_text, text_rect)
        elif ganhador == 'Empate':
            self.set_background(surf,8)
            text_draw = self.menu_font.render('Obtivemos um Empate na partida!', True, (255, 255, 255))
            draw_rect = surf.get_retangle_transparente(self.size[0], 100, 200, (0, 0, 0))

            self.window.blit(draw_rect, (0, (self.size[1] - 100) // 2))

            text_rect = text_draw.get_rect()
            text_rect.center = (self.size[0] // 2, (self.size[1] - 100) // 2 + 90 // 2) 

            self.window.blit(text_draw, text_rect)

        else:
            if ganhador == 'Dragão Azul':
                self.set_background(surf,9)
            else:
                self.set_background(surf,10)
            
            text_win = self.menu_font.render(f'{ganhador} venceu a partida!', True, (255, 255, 255))
            win_rect = surf.get_retangle_transparente(self.size[0], 100, 200, (0, 0, 0))

            self.window.blit(win_rect, (0, (self.size[1] - 100) // 2))

            text_rect = text_win.get_rect()
            text_rect.center = (self.size[0] // 2, (self.size[1] - 100) // 2 + 90 // 2) 

            self.window.blit(text_win, text_rect)

        while True:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Passa os eventos para o gerenciador de interface do usuário
                manager.process_events(event)

                # Verifica se algum botão foi clicado
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == buttonback:
                        inicio()


            # Atualiza o gerenciador de interface do usuário
            manager.update(time_delta)

            # Desenha os botões
            manager.draw_ui(self.window)

            pygame.display.flip()

    def show_score(self, choice, color, font, size, score):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (self.size[0]/12, 20)
        else:
            score_rect.midtop = (self.size[0]/2, self.size[1]/1.25)
        self.window.blit(score_surface, score_rect)
        # pygame.display.flip()

    def set_background(self, surf, num):
        match(num):
            case 1: self.window.blit(surf.background_menu, (0,0))
            case 2: self.window.blit(surf.backgrounds_game[0], (0,0))
            case 3: self.window.blit(surf.backgrounds_game[1], (0,0))
            case 4: self.window.blit(surf.backgrounds_game[2], (0,0))
            case 5: self.window.blit(surf.backgrounds_loading[0], (0,0))
            case 6: self.window.blit(surf.backgrounds_loading[1], (0,0))
            case 7: self.window.blit(surf.backgrounds_gameover[0], (0,0))
            case 8: self.window.blit(surf.backgrounds_gameover[1], (0,0))
            case 9: self.window.blit(surf.backgrounds_win[0], (0,0))
            case 10: self.window.blit(surf.backgrounds_win[1], (0,0))
        
