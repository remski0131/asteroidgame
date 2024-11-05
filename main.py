import os
import pygame
from constants import *

def main():
    # Initialize pygame first
    pygame.init()
    
    # Then set the display mode
    pygame.display.init()
    
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((0, 0, 0))
        pygame.display.flip()
    
    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main()