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
        self._font = pygame.font.SysFont(None, 48)        

    def _draw_menu(self):
        self._screen.fill((0, 0, 0))
        coefficient = self._height // 3 # (3) -> number of lines to render

        title = self._font.render("Select Level", True, (255, 255, 255))
        level1 = self._font.render("Press 1 => Level 1", True, (255, 255, 255))
        level2 = self._font.render("Press 2 => Level 2", True, (255, 255, 255))

        self._screen.blit(title, (self._width // 2 - title.get_width() // 2, coefficient // 2 - title.get_height()))
        self._screen.blit(level1, (self._width // 2 - level1.get_width() // 2, 3 * coefficient // 2 - level1.get_height()))
        self._screen.blit(level2, (self._width // 2 - level2.get_width() // 2, 5 * coefficient // 2 - level2.get_height()))

    def game_loop(self):
        while self._running:
            self._handle_events()

            if self._level is None:
                self._draw_menu()

            else:
                self._level.update()
                self._level.draw(self._screen)

                if self._level.check_win_condition():
                    print(f"Level Complete!")
                    self._level = None

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