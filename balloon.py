import os
import sys
import pygame
import random

from dotenv import load_dotenv
load_dotenv("config.env")

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        screen_width = int(os.getenv("GAME_WIDTH"))
        screen_height = int(os.getenv("GAME_HEIGHT"))
        self._speed = int(os.getenv("BALLOON_SPEED"))
        diameter = screen_width // 10
        self._horizontal_minimum = screen_width // 2 + diameter // 2
        self._horizontal_maximum = screen_width - diameter // 2
        self._vertical_minimum = 0 + diameter // 2
        self._vertical_maximum = screen_height - diameter // 2

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "assets", "balloon.png")
        sound_path = os.path.join(base_path, "assets", "grenade.mp3")
        
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (diameter, diameter))
        self.rect = self.image.get_rect()
        self._sound = pygame.mixer.Sound(sound_path)

        self.rect.centerx = random.randint(self._horizontal_minimum , self._horizontal_maximum)
        self.rect.centery = random.randint(self._vertical_minimum, self._vertical_maximum)
        self._set_direction()

    def _set_direction(self):
        self._speed_x = random.randint(-self._speed, self._speed)
        self._speed_y = random.randint(-self._speed, self._speed)
        self._frames_counter = random.randint(60, 120)

    def update(self):
        self.rect.centerx += self._speed_x
        self.rect.centery += self._speed_y
        self._frames_counter -= 1

        if (
            self._frames_counter <= 0
            # Redirect on bounds
            or self.rect.left <= self._horizontal_minimum
            or self.rect.left >= self._horizontal_maximum
            or self.rect.top <= self._vertical_minimum
            or self.rect.bottom >= self._vertical_maximum
        ):
            self._set_direction()

        # Clamp bounds
        self.rect.centerx = max(self._horizontal_minimum, min(self.rect.centerx, self._horizontal_maximum))
        self.rect.centery = max(self._vertical_minimum, min(self.rect.centery, self._vertical_maximum))

    def collision(self):
        self._sound.play()
        self.kill()

if __name__ == "__main__":
    pygame.init()

    screen_width = int(os.getenv("GAME_WIDTH"))
    screen_height = int(os.getenv("GAME_HEIGHT"))
    screen = pygame.display.set_mode((screen_width, screen_height))

    fps = 60
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    balloon = Balloon()
    sprites.add(balloon)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(fps)
        sprites.update()
        screen.fill((255, 255, 255))
        sprites.draw(screen)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()