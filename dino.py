import pygame
from time import sleep

class Dino:
    def __init__(self, settings, screen):
        # Sets screen and dino image
        self.screen = screen
        # Animation images for dino
        self.image_stand = pygame.image.load('images/dino_stand.png').convert()
        self.image_l1 = pygame.image.load('images/dino_l1.png').convert()
        self.image_l2 = pygame.image.load('images/dino_l2.png').convert()
        self.image_ma = pygame.image.load('images/dino_midair.png').convert()
        self.image_r1 = pygame.image.load('images/dino_r1.png').convert()
        self.image_r2 = pygame.image.load('images/dino_r2.png').convert()
        # Scale and Track image to draw
        self.image_stand = pygame.transform.scale(self.image_stand, (30, 34))
        self.image_l1 = pygame.transform.scale(self.image_l1, (30, 34))
        self.image_l2 = pygame.transform.scale(self.image_l2, (30, 34))
        self.image_ma = pygame.transform.scale(self.image_ma, (30, 34))
        self.image_r1 = pygame.transform.scale(self.image_r1, (30, 34))
        self.image_r2 = pygame.transform.scale(self.image_r2, (30, 34))

        self.images = [self.image_stand, self.image_l1, self.image_l2,
                       self.image_ma, self.image_r1, self.image_r2]

        self.buffer = settings.buffer
        self.ground = settings.ground
        # Sets rect for image and screen
        self.rect = self.image_stand.get_rect()
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



    def blitme(self, set):
        image = self.images[set.rotation]
        self.screen.blit(image, self.rect)

    def set_background(self, rotation, city_image):
        print("Setting background")
