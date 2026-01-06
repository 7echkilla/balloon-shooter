import os
import sys
import pygame

from bullet import Bullet

from dotenv import load_dotenv
load_dotenv("config.env")

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        screen_width = int(os.getenv("GAME_WIDTH"))
        screen_height = int(os.getenv("GAME_HEIGHT"))
        self._speed = int(os.getenv("GUN_SPEED"))

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "assets", "cannon.png")
        sound_path = os.path.join(base_path, "assets", "silencer.mp3")

        width = screen_width // 10
        height = screen_height // 5

        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (width, height))
        self._sound = pygame.mixer.Sound(sound_path)

        self.rect = self.image.get_rect()
        self.rect.left = screen_width // 20
        self.rect.centery = screen_height // 2

        self._vertical_minimum = 0
        self._vertical_maximum = screen_height

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

    screen_width = int(os.getenv("GAME_WIDTH"))
    screen_height = int(os.getenv("GAME_HEIGHT"))
    screen = pygame.display.set_mode((screen_width, screen_height))

    fps = 60
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    gun = Gun()
    sprites.add(gun)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = gun.shoot()
                    sprites.add(bullet)
                    bullets.add(bullet)

        clock.tick(fps)
        gun.update(pygame.key.get_pressed())
        bullets.update()

        screen.fill((255, 255, 255))
        sprites.draw(screen)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()