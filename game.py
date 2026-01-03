import os
import pygame
import random

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
        self._balloons = pygame.sprite.Group() 
        self._gun = Gun()
        self._sprites.add(self._gun)

        self._score = 0
        self._level = 1

    def spawn_balloon(self):
        balloon = Balloon()
        self._sprites.add(balloon)
        self._balloons.add(balloon)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = self._gun.shoot()
                    self._sprites.add(bullet)
                    self._bullets.add(bullet)
    
    def update(self):
        keys = pygame.key.get_pressed()
        self._gun.update(keys)
        self._bullets.update()
        self._balloons.update()

        collision = pygame.sprite.groupcollide(self._balloons, self._bullets, True, True)
        if collision:
            self._score += len(collision)

        if random.random() < 0.02:
            self.spawn_balloon()

    def draw(self):
        self._screen.fill((255, 255, 255))
        self._sprites.draw(self._screen)

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self._score}", True, (0, 0, 0))
        self._screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def run(self):
        while self._running:
            self._clock.tick(self._fps)
            self.events()
            self.update()
            self.draw()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()