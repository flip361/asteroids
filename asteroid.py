import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, surface):
        pygame.draw.circle(
            surface,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            2
        )
    
    def update(self, dt):
        # Update x & y positions using velocity and dt
        movement = self.velocity * dt
        self.position.x += movement.x
        self.position.y += movement.y

    def split(self):
        print(f"Splitting asteroid with radius: {self.radius}")
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("Asteroid too small to split")
            self.kill()
            return
        
        random_angle = random.uniform(20, 50)
        new_vel1 = self.velocity.rotate(random_angle)
        new_vel2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # creating new asteeroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # setting their velocities higher than parent velocity
        asteroid1.velocity = new_vel1 * 1.2
        asteroid2.velocity = new_vel2 * 1.2

        # add them to the game's asteroid group
        self.groups()[0].add(asteroid1)
        self.groups()[0].add(asteroid2)
        
        self.kill()