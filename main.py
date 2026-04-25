import pygame
import constants
import logger 
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() 
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0        
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroidField_1 = AsteroidField()  
  
    while True:
        logger.log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if obj.collides_with(player) == True:
                logger.log_event("player_hit")
                print("Game over")
                sys.exit()
        for ast in asteroids:
            for shot in shots:
                if ast.collides_with(shot) == True:
                    logger.log_event("asteroid_shot")
                    Asteroid.split(ast)
                    pygame.sprite.Sprite.kill(shot)
        pygame.display.flip()        
        dt = clock.tick(60)/1000
        

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
