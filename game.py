import os
import pygame

from dotenv import load_dotenv
from gun import Gun
from balloon import Balloon


load_dotenv("config.env")

class Game:
    def __init__(self):
        pygame.init()

        self._width = int(os.getenv("GAME_WIDTH"))
        self._height = int(os.getenv("GAME_HEIGHT"))
        self._fps = int(os.getenv("GAME_FPS"))

        self._screen = pygame.display.set_mode((self._width, self._height))
        self._clock = pygame.time.Clock()
        self._running = True

        self._sprites = pygame.sprite.Group()
        self._bullets = pygame.sprite.Group()
        self._balloon = Balloon()
        self._gun = Gun()

    def run(self):
        while self._running:
            self._clock.tick(self._fps)


if __name__ == "__main__":
    game = Game()
    game.run()