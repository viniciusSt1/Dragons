import pygame,sys

class Events:
    def __init__(self):
        pass

    def checker(self,dragon1, dragon2):   #dragon passado por referencia
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if dragon2 == None:
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        dragon1.change_direction('UP')
                    elif event.key == pygame.K_DOWN or event.key == ord('s'):
                        dragon1.change_direction('DOWN')
                    elif event.key == pygame.K_LEFT or event.key == ord('a'):
                        dragon1.change_direction('LEFT')
                    elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                        dragon1.change_direction('RIGHT')
                else:
                    if event.key == pygame.K_UP:
                        dragon2.change_direction('UP')
                    elif event.key == pygame.K_DOWN:
                        dragon2.change_direction('DOWN')
                    elif event.key == pygame.K_LEFT:
                        dragon2.change_direction('LEFT')
                    elif event.key == pygame.K_RIGHT:
                        dragon2.change_direction('RIGHT')
                    elif event.key == ord('w'):
                        dragon1.change_direction('UP')
                    elif event.key == ord('s'):
                        dragon1.change_direction('DOWN')
                    elif event.key == ord('a'):
                        dragon1.change_direction('LEFT')
                    elif event.key == ord('d'):
                        dragon1.change_direction('RIGHT')
                
                # Esc -> Create event to quit the game
                if event.key == ord('p'):
                    return 'pause'
        return None
    
    def gameStart(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    return 'start_1player'
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    return 'start_2player'
                elif event.key == pygame.K_s:
                    return 'load_save'
        return None
    
    def despause(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    if event.key == ord('p'):
                        return True
        return False