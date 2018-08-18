import pygame
from fireball import Fireball

class Dino:
    def __init__(self, settings, screen):

        # Sets screen and dino image
        self.screen = screen

        # Frames for dino
        frame1 = pygame.image.load('images/dino/dino1.png').convert()
        frame2 = pygame.image.load('images/dino/dino2.png').convert()
        frame3 = pygame.image.load('images/dino/dino3.png').convert()
        frame4 = pygame.image.load('images/dino/dino4.png').convert()
        frame5 = pygame.image.load('images/dino/dino5.png').convert()
        frame6 = pygame.image.load('images/dino/dino6.png').convert()
        frame7 = pygame.image.load('images/dino/dino7.png').convert()

        # Scales frames to draw
        frame1 = pygame.transform.scale(frame1, (30, 34))
        frame2 = pygame.transform.scale(frame2, (30, 34))
        frame3 = pygame.transform.scale(frame3, (30, 34))
        frame4 = pygame.transform.scale(frame4, (30, 34))
        frame5 = pygame.transform.scale(frame5, (30, 34))
        frame6 = pygame.transform.scale(frame6, (30, 34))
        frame7 = pygame.transform.scale(frame7, (30, 34))
        # Stores frames in array
        self.images = [frame1, frame2, frame3, frame4, frame5, frame6, frame7]

        # Sets rect for image and screen
        self.rect = frame1.get_rect()
        screen_rect = screen.get_rect()

        # Sets position in screen
        self.rect.bottom = settings.ground
        self.rect.centerx = int(screen_rect.centerx / 2)

        self.frame = 0
        self.timer = 0

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
            # Times the frames to draw
            if self.timer == 21:
                self.timer = 0
                self.frame = self.frame + 1
            elif self.timer % 3 == 0:
                self.frame = self.frame + 1
            self.timer = self.timer + 1

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
        if self.frame is 7:
            self.frame = 1  # Restarts frame loop

        dino_image = self.images[self.frame]
        self.screen.blit(dino_image, self.rect)

        if set.fireball and set.play:
            self.fireball.shoot()

        elif self.fireball.explosion.active and set.play:
            self.fireball.EXPLODE(set.cactus_speed)
