import os
import sys
import pygame

from dotenv import load_dotenv
from src.level_1 import Level1
from src.level_2 import Level2

load_dotenv("config.env")

class Game:
    def __init__(self):
        pygame.init()

        # Load game parameters
        self._width = int(os.getenv("GAME_WIDTH"))
        self._height = int(os.getenv("GAME_HEIGHT"))
        self._fps = int(os.getenv("GAME_FPS"))

        self._screen = pygame.display.set_mode((self._width, self._height))
        self._clock = pygame.time.Clock()
        self._running = True
        self._level = None        

    def _select_level(self):
        print("Press 1 for Level 1, 2 for Level 2")

    def game_loop(self):
        self._select_level()

        while self._running:
            self._handle_events()

            if self._level:
                self._level.update()
                self._level.draw(self._screen)

                if self._level.check_win_condition():
                    print(f"Level Complete!")
                    # self._running = False
                    self._level = None
                    self._select_level()

            pygame.display.flip()
            self._clock.tick(self._fps)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if event.type == pygame.KEYDOWN:
                if self._level is None:
                    if event.key == pygame.K_1:
                        self._level = Level1()
                    if event.key == pygame.K_2:
                        self._level = Level2()
                else:
                    if event.key == pygame.K_SPACE:
                        self._level.spawn_bullet()

    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.game_loop()
    game.quit()