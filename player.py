import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
    # Call the parent constructor
    # Set the rotation attribute
    # in the player class
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt, forward = True):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        if not forward:
            direction = -direction
        self.position += direction * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            # Rotate left: pass a negative delta time
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right: pass a positive delta time
            self.rotate(dt)
        if keys[pygame.K_w]:
            #Move forward: pass a positive delta time
            self.move(dt, forward = True)
        if keys[pygame.K_s]:
            #Move backwards: pass a negative delta time
            self.move(dt, forward = False)
        if keys[pygame.K_SPACE]:
            #Shoot with spacebar
            self.shoot()
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            2
        )

    def shoot(self):
        if self.shoot_timer <= 0:
            new_shot = Shot(self.position.x, self.position.y)
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED
            new_shot.velocity = velocity
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            return new_shot
        else: # Can't shoot yet, return none or handle case as needed
            return None
