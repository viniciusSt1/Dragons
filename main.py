import pygame
from gameDragons.Runner import Runner

pygame.init()

# Configurações do menu
menu_font = pygame.font.SysFont('Arial', 56)
menu_color = (33, 200, 156)
menu_text = menu_font.render("Pressione Enter para Jogar", False, menu_color)
menu_text_rect = menu_text.get_rect(center=(640, 360))

game_display = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
game_started = False

#Carregar a imagem de fundo
wallpaper = pygame.image.load("Backgrounds/1.jpg")


#Musica
pygame.mixer.music.load("SFX/ambience2.mp3")
pygame.mixer.music.play(-1)  # -1 produção em loop

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_started = True
                pygame.mixer.music.stop()
    game_display.blit(wallpaper, (0, 0))  # Preenche o fundo 

    if not game_started:
        game_display.blit(menu_text, menu_text_rect)
    else:
        game = Runner()  # Inicia o jogo

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
