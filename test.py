import os
import sys
import pygame

from dotenv import load_dotenv
from level_1 import Level1
from level_2 import Level2

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
        self._level_choice = None
        self._current_level = None        

    def _select_level(self):
        print("Press 1 for Level 1, 2 for Level 2")
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self._level_choice = 1
        elif keys[pygame.K_2]:
            self._level_choice = 2

    def _initialise_level(self):
        if self._level_choice == 1:
            self._current_level = Level1
        elif self._level_choice == 2:
            self._current_level = Level2

    def game_loop(self):
        while self._running:
            self._handle_events()

            if not self._level_choice:
                self._select_level()
            else:
                self._initialise_level()
                self._current_level.update()
                self._current_level.draw(self._screen)
                pygame.display.flip()

            if self._current_level.check_win_condition():
                print(f"Level {self._level_choice} Complete!")
                self._running = False

            self._clock.tick(self._fps)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._current_level.spawn_bullet()

    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.game_loop()
    game.quit()