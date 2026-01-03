import os
import pygame
import random

from dotenv import load_dotenv
load_dotenv("config.env")

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        screen_width = int(os.getenv("GAME_WIDTH"))
        screen_height = int(os.getenv("GAME_HEIGHT"))
        diameter = screen_width // 10

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "assets", "balloon.png")
        
        self._horizontal_minimum = screen_width // 2 + diameter // 2
        self._horizontal_maximum = screen_width - diameter // 2
        self._vertical_minimum = 0 + diameter // 2
        self._vertical_maximum = screen_height - diameter // 2

        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (diameter, diameter))
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(self._horizontal_minimum , self._horizontal_maximum)
        self.rect.centery = random.randint(self._vertical_minimum, self._vertical_maximum)

        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()