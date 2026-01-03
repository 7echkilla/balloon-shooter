import pygame

from gun import Gun
from bullet import Bullet
from balloon import Balloon

class Level:
    def __init__(self, level_number):
        self._level_number = level_number
        self._sprites = pygame.sprite.Group()
        self._background = None
        self._sprites = pygame.sprite.Group()
        self._bullets = pygame.sprite.Group()
        self._balloons = pygame.sprite.Group() 
        self._gun = Gun()
        self._sprites.add(self._gun)

    def setup(self):
        pass

    def update(self):
        # Update all sprites and logic specific to the level
        self._sprites.update()

    def draw(self, screen):
        # Draw everything related to this level
        screen.fill(self._background)
        self._sprites.draw(screen)
        
    def check_win_condition(self):
        # Check if the player has won the level (optional)
        return False  # Just a placeholder, add your win condition here
    
    def spawn_bullet(self):
        bullet = self._gun.shoot()
        self._sprites.add(bullet)
        self._bullets.add(bullet)
