import pygame
from circleshape import CircleShape

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