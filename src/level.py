import os
import sys
import pygame

from src.gun import Gun
from src.bullet import Bullet
from src.balloon import Balloon
# from abc import ABC, abstractmethod

class Level():
    def __init__(self):
        self._background = None

        self._sprites = pygame.sprite.Group()
        self._bullets = pygame.sprite.Group()
        self._balloons = pygame.sprite.Group() 

        self._gun = Gun()
        self._sprites.add(self._gun)

        self._setup()

    def _setup(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        self._gun.update(keys)
        self._bullets.update()
        self._balloons.update()

        collision = pygame.sprite.groupcollide(self._balloons, self._bullets, True, True)
        
        for balloon, bullets in collision.items():
            balloon.collision()
            for bullet in bullets:
                bullet.collision()

    def draw(self, screen):
        white = (255, 255, 255)
        screen.fill(white)
        self._sprites.draw(screen)
        
    def check_win_condition(self):
        pass
        
    def spawn_bullet(self):
        bullet = self._gun.shoot()
        self._sprites.add(bullet)
        self._bullets.add(bullet)

if __name__ == "__main__":
    pygame.init()

    screen_width = int(os.getenv("GAME_WIDTH"))
    screen_height = int(os.getenv("GAME_HEIGHT"))
    screen = pygame.display.set_mode((screen_width, screen_height))

    fps = 60
    clock = pygame.time.Clock()

    level = Level()

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
