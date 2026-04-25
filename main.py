import pygame
import constants
from logger import log_state
from player import Player

def main():
    pygame.init() 
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0    
    player_1 = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        player_1.draw(screen)
        pygame.display.flip()
        if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick(60)/1000


        


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
