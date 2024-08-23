import pygame
import sys
from constants import *
from pygame.locals import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Object group assignment
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    # Player and environment start
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    updatable.add(player, asteroid_field)
    drawable.add(player)
    print(f"Number of asteroids: {len(asteroids)}")
    
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="#000000")
        
                
        for item in updatable:
            item.update(dt)
        
        for asteroid in asteroids:
            print(f"Checking collision: Player at {player.position} (radius {player.radius}), Asteroid at {asteroid.position} (radius {asteroid.radius})")
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
        
        for item in drawable:
            item.draw(screen)        
        
        
        pygame.display.flip()
        
        
    
if __name__ == "__main__":  
    main()