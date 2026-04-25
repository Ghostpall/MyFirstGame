import circleshape
import constants
import pygame
import logger
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius == constants.ASTEROID_MIN_RADIUS:
            return
        else:
            logger.log_event("asteroid_split")
            random.uniform(20,50)
            vector_1 = self.velocity.rotate(0)
            vector_2 = self.velocity.rotate(180)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = vector_1 * 1.2
            asteroid_2.velocity = vector_2 * 1.2