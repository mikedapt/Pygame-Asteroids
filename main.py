import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable

    Shot.containers = (shot, updatable, drawable)

    field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while 1 > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        screen.fill((0,0,0))
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
        
        for unit in asteroids:
            for s in shot:
                if s.collision(unit):
                   unit.split()
                   s.kill()
            if player.collision(unit):
               print("Game Over!")
               sys.exit()

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
