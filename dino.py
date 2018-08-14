import pygame
from time import sleep

class Dino:
    def __init__(self, settings, screen):
        # Sets screen and dino image
        self.screen = screen
        self.image = pygame.image.load('images/blue_dino.png').convert()
        self.image = pygame.transform.scale(self.image, (40, 30))

        self.buffer = settings.buffer
        self.ground = settings.ground
        # Sets rect for image and screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Sets position in screen
        self.rect.bottom = settings.ground
        self.rect.centerx = int(self.screen_rect.centerx / 2)
        # Tracks movement of image
        self.isjump = 0
        self.m = 8
        self.v = 2
        # y = (x - 4.5)**2 + 20

    def jump(self, set):
        self.isjump = 1
        set.cactus_speed = set.cactus_speed * 500

    def update(self, settings):
        if self.isjump:

            if self.v and self.v > 0:
                F = ( 0.05 * self.m * (self.v*self.v) )
            else:
                F = -( 0.05 * self.m * (self.v*self.v) )

            # Change position/velocity
            self.rect.y = self.rect.y - F
            self.v = self.v - 1

             # If ground is reached, reset variables.
            if self.rect.bottom >= settings.ground:
                self.rect.bottom = self.ground
                self.isjump = 0
                self.v = 8
                settings.cactus_speed = settings.cactus_speed / 500

    def blitme(self):
        self.screen.blit(self.image, self.rect)
