import pygame
import random

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        radius = random.randint(15, 30)
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 400 - self.rect.width)
        self.rect.y = 600 + random.randint(20, 100)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()