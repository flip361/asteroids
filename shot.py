import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
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

    def is_off_screen(self):
        return (self.position.x < 0 or
                self.position.x > SCREEN_WIDTH or
                self.position.y < 0 or
                self.position.y > SCREEN_HEIGHT
                )