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
        self.cactus_timer = 0

    def update(self):
        if self.cactus_timer is 7:
            new_pos = float(self.rect.centerx - self.speed)
            self.rect.centerx = new_pos
            self.cactus_timer = 0
        self.cactus_timer = self.cactus_timer + 1

    def draw(self):
        self.screen.blit(self.image, self.rect)
