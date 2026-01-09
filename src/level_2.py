import os
import sys
import pygame
import random

from src.level import Level
from src.balloon import Balloon

class Level2(Level):
    def __init__(self):
        super().__init__()
        self._background = None
        
    def _setup(self):
        number = random.randint(3, 5)

        for n in range(number):
            balloon = Balloon()
            self._balloons.add(balloon)
            self._sprites.add(balloon)

    def check_win_condition(self):
        if not self._balloons:
            return True
        else:
            return False

if __name__ == "__main__":
    pygame.init()

    screen_width = int(os.getenv("GAME_WIDTH"))
    screen_height = int(os.getenv("GAME_HEIGHT"))
    screen = pygame.display.set_mode((screen_width, screen_height))

    fps = 60
    clock = pygame.time.Clock()

    level = Level2()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level.spawn_bullet()

        clock.tick(fps)
        level.update()
        level.draw(screen)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()