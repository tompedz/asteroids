import pygame
from constants import *
from pygame.locals import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="#000000")
        pygame.display.flip()
    
if __name__ == "__main__":
    main()