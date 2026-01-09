import os
import pygame

from dotenv import load_dotenv
load_dotenv("config.env")

class Bullet(pygame.sprite.Sprite):
    def __init__(self, left, y):
        super().__init__()
        
        screen_width = int(os.getenv("GAME_WIDTH"))
        screen_height = int(os.getenv("GAME_HEIGHT"))
        self._speed = int(os.getenv("BULLET_SPEED"))

        asset_path = os.path.join(os.path.dirname(__file__), "..", "assets")
        sound_path = os.path.join(asset_path, "impact.mp3")

        width = screen_width // 100
        height = screen_height // 100
        black = (0, 0, 0)

        self.image = pygame.Surface((width, height))
        self.image.fill(black)
        self.rect = self.image.get_rect(center=(left, y))
        self._sound = pygame.mixer.Sound(sound_path)
        self._horizontal_maximum = screen_width

    def update(self):
        self.rect.centerx += self._speed
        if self.rect.left >= self._horizontal_maximum:
            self._sound.play()
            self.kill()

    def collision(self):
        self.kill()