import pygame
from pygame.sprite import Sprite

class Cactus(Sprite):
    ''' Creates cactus object '''

    def __init__(self, set, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images\cactus.png').convert()

        # Cactus spawns on ground at right of screen
        self.speed = set.cactus_speed 
        self.scored = False
        self.rect = self.image.get_rect()

        self.rect.bottom = set.ground
        self.rect.x = set.screen_width

    def update(self):
        new_pos = self.rect.x - self.speed
        self.rect.x = new_pos

    def draw(self):
        self.screen.blit(self.image, self.rect)
