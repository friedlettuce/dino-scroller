import pygame
from fireball import Fireball

class Dino:
    def __init__(self, settings, screen):

        # Sets screen and dino image
        self.screen = screen

        # Frames for dino
        self.image_stand = pygame.image.load('images/dino_stand.png').convert()
        self.image_l1 = pygame.image.load('images/dino_l1.png').convert()
        self.image_l2 = pygame.image.load('images/dino_l2.png').convert()
        self.image_ma = pygame.image.load('images/dino_midair.png').convert()
        self.image_r1 = pygame.image.load('images/dino_r1.png').convert()
        self.image_r2 = pygame.image.load('images/dino_r2.png').convert()

        # Scales frames to draw
        self.image_stand = pygame.transform.scale(self.image_stand, (30, 34))
        self.image_l1 = pygame.transform.scale(self.image_l1, (30, 34))
        self.image_l2 = pygame.transform.scale(self.image_l2, (30, 34))
        self.image_ma = pygame.transform.scale(self.image_ma, (30, 34))
        self.image_r1 = pygame.transform.scale(self.image_r1, (30, 34))
        self.image_r2 = pygame.transform.scale(self.image_r2, (30, 34))
        # Stores frames in array
        self.images = [self.image_stand, self.image_l1, self.image_l2,
                       self.image_ma, self.image_r1, self.image_r2]

        # Sets rect for image and screen
        self.rect = self.image_stand.get_rect()
        screen_rect = screen.get_rect()

        # Sets position in screen
        self.rect.bottom = settings.ground
        self.rect.centerx = int(screen_rect.centerx / 2)

        self.frame = 0

        # Tracks jump
        self.isjump = False
        self.m = 8
        self.v = 2

        # fireball
        self.fireball = Fireball(settings, screen, self.rect)

    def jump(self):
        # Turns jump on, speed up cactus for jump
        self.isjump = True

    # Makes sure fireball rect is dino rect upon firing
    def set_fireball(self):
        self.fireball.rect.right = self.rect.right
        self.fireball.rect.centery = self.rect.centery

    def update(self, settings):
        ''' Runs, jumps, shoots and explodes fireball '''
        if settings.play:
            self.frame = self.frame + 1

        # Block updates jump
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
                self.rect.bottom = settings.ground
                self.isjump = False
                self.v = 8

        # Updates frames for fireball
        if settings.fireball:
            if not self.fireball.off_screen(settings.screen_width):
                self.fireball.update_frames()
                self.fireball.update()
            else:
                settings.fireball = False
                self.fireball.reset()

        # Checks to stop explosion
        elif self.fireball.explosion.active:
            self.fireball.EXPLODE(settings.cactus_speed)

            if not self.fireball.explosion.active:
                self.fireball.explosion.reset()
                self.fireball.reset()

    def blitme(self, set):
        # Rotates through and draws dino by frame
        if self.frame is 6:
            self.frame = 0

        dino_image = self.images[self.frame]
        self.screen.blit(dino_image, self.rect)

        if set.fireball and set.play:
            self.fireball.shoot()

        elif self.fireball.explosion.active and set.play:
            self.fireball.EXPLODE(set.cactus_speed)
