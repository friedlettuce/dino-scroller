import pygame
from pygame.sprite import Sprite
from time import sleep

class Cactus(Sprite):
    def __init__(self, set, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images\cactus.png')

        self.ground = set.ground
        self.speed = set.cactus_speed

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.bottom = self.ground
        self.rect.x = set.screen_width

    def update(self):
        cx = float(self.rect.centerx)
        cx = cx - self.speed

        self.rect.centerx = cx

    def draw(self):
        self.screen.blit(self.image, self.rect)
