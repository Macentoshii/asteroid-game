from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

import random
import pygame


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface=surface, color='white', center=self.position, radius=self.radius, width=LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        
        angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(angle)
        velocity_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(velocity_1[0], velocity_1[1], new_radius)
        asteroid_1.velocity = velocity_1 * 1.2
        asteroid_2 = Asteroid(velocity_2[0], velocity_2[1], new_radius)
        asteroid_2.velocity = velocity_2 * 1.2
        