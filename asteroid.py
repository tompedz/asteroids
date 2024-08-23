import pygame
import random
from circleshape import *
from constants import *
from main import *
from player import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.random_angle = random.uniform(20, 50)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)
        
          
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        v1 = self.velocity.rotate(self.random_angle)
        v2 = self.velocity.rotate(-self.random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        n1 = Asteroid(self.position.x, self.position.y, new_radius)
        n2 = Asteroid(self.position.x, self.position.y, new_radius)

        n1.velocity = v1 * 1.2
        n2.velocity = v2 * 1.2