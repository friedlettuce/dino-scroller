import pygame
from pygame.sprite import Sprite

class Cactus(Sprite):
    ''' Creates cactus object '''

    def __init__(self, set, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images\cactus.png').convert()

        self.speed = set.cactus_speed
        self.scored = False     # Makes sure cactus isn't scored more than once

        # Cactus spawns on ground at right of screen
        self.rect = self.image.get_rect()
        self.rect.bottom = set.ground
        self.rect.x = set.screen_width

    def update(self):
        self.rect.x = self.rect.x - self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
