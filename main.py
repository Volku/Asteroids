# TODO: Make these system comes true?
# - Add a scoring system
# - Implement multiple lives and respawning
# - Add an explosion effect for the asteroids
# - Add acceleration to the player movement
# - Make the objects wrap around the screen instead of disappearing
# - Add a background image
# - Create different weapon types
# - Make the asteroids lumpy instead of perfectly round
# - Make the ship have a triangular hit box instead of a circular one
# - Add a shield power-up
# - Add a speed power-up
# - Add bombs that can be dropped
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player1 = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_collisions(asteroid):
                    bullet.kill()
                    asteroid.split()
            if player1.check_collisions(asteroid):
                print("Game over!")
                return
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
