# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import time
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(
        x = SCREEN_WIDTH / 2,
        y = SCREEN_HEIGHT / 2
    )
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_shot = player.shoot()
                    if new_shot is not None: # Only add the shot  if its not none
                        shots.add(new_shot)
        
        bullet_hit_leeway = 5

        for shot in shots.copy():
            for asteroid in asteroids.copy():
                if asteroid.position.distance_to(shot.position) <= asteroid.radius + shot.radius + bullet_hit_leeway:
                    shot.kill()  # Remove the bullet
                    asteroid.split()  # Remove the asteroid
                    shots.remove(shot)
                    asteroids.remove(asteroid)
                    break
        
        # Handle continuous key presses
        keys = pygame.key.get_pressed()

        screen.fill((0, 0, 0))
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
        for object in updatable:
            object.update(dt)
        
        for object in asteroids:
            if object.collisions(player):
                print("Game Over")
                # Exit the program here
                sys.exit()
        
        for shot in shots.copy():
            if shot.is_off_screen():
                shots.remove(shot)
        
        


if __name__ == "__main__":
    main()