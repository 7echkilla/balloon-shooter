import os
import pygame

from bullet import Bullet

class Gun(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        width = screen_width // 10
        height = screen_height // 10

        self._vertical_minimum = 0
        self._vertical_maximum = screen_height

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "assets", "cannon.png")
        sound_path = os.path.join(base_path, "assets", "silencer.mp3")

        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (width, height))
        self._sound = pygame.mixer.Sound(sound_path)

        self.rect = self.image.get_rect()
        self.rect.left = screen_width // 20
        self.rect.centery = screen_height // 2

        self._speed = 6

    def update(self, keys):
        if keys[pygame.K_w] and self.rect.top > self._vertical_minimum:
            self.rect.y -= self._speed
        if keys[pygame.K_s] and self.rect.bottom < self._vertical_maximum:
            self.rect.y += self._speed

    def shoot(self):
        self._sound.play()
        bullet = Bullet(self.rect.right, self.rect.centery)
        return bullet
    
if __name__ == "__main__":
    pygame.init()
    gun = Gun(900, 500)