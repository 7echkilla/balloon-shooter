import os
import pygame

from bullet import Bullet

class Gun(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        self._width = screen_width // 10
        self._height = screen_height // 10

        self._vertical_minimum = 0
        self._vertical_maximum = screen_height

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "assets", "cannon.png")
        sound_path = os.path.join(base_path, "assets", "silencer.mp3")

        # self._image_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "assets", "cannon.png")
        # self._sound_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "assets", "silencer.mp3")
        self.image = pygame.transform.scale(pygame.image.load(self._image_path).convert_alpha(), (self._width, self._height))
        self._sound = pygame.mixer.Sound(self.sound_path)

        self.rect = self.image.get_rect()
        self.rect.left = screen_width // 20
        self.rect.centery = screen_height // 2

        self._speed = 6

    def update(self, keys):
        if keys[pygame.K_w] and self._rect.top > self._vertical_minimum:
            self._rect.y -= self._speed
        if keys[pygame.K_s] and self._rect.bottom < self._vertical_maximum:
            self._rect.y += self._speed

    def shoot(self):
        self._sound.play()
        bullet = Bullet(self._rect.right, self._rect.centery)
        return bullet
    
if __name__ == "__main__":
    pygame.init()
    gun = Gun(900, 500)