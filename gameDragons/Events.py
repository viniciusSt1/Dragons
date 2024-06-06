import pygame,sys

class Events:
    def __init__(self):
        pass

    def checker(self,dragon):   #dragon passado por referencia
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    dragon.change_direction('UP')
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    dragon.change_direction('DOWN')
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    dragon.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    dragon.change_direction('RIGHT')
                # Esc -> Create event to quit the game
                elif event.key == ord('p'):
                    return 'save'
        return None
    
    def gameStart(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 'start_game'
                elif event.key == pygame.K_s:
                    return 'load_save'
        return None