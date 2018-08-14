import pygame
from pygame.sprite import Sprite

class City(Sprite):
    def __init__(self, set, screen, num):
        super().__init__()
        self.screen = screen
        self.screen_width = set.screen_width
        self.image = pygame.image.load('images\city.jpg').convert()

        self.num = num
        self.speed = int(set.cactus_speed / 4)
        self.rect = self.image.get_rect()

        if num is 1:
            self.rect.x = 0
        elif num is 2:
            self.rect.x = self.screen_width

        self.boundary = self.rect.x - self.screen_width
        self.rect.bottom = set.ground

    def update(self):
        self.rect.x = self.rect.x - self.speed

        if self.rect.x <= self.boundary:
            self.reset()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def reset(self):
        if self.num is 1:
            self.rect.x = 0
        elif self.num is 2:
            self.rect.x = self.screen_width
