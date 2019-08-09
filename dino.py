import pygame
from time import sleep

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
                self.frame += 1
            self.timer += 1

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

class Fireball:
    def __init__(self, settings, screen, dino_rect):
        # Stores screen and fireball animation
        self.screen = screen
        fb1 = pygame.image.load('images/fireball/fireball_1.png').convert()
        fb2 = pygame.image.load('images/fireball/fireball_2.png').convert()
        fb3 = pygame.image.load('images/fireball/fireball_3.png').convert()
        fb4 = pygame.image.load('images/fireball/fireball_4.png').convert()
        fb5 = pygame.image.load('images/fireball/fireball_5.png').convert()
        fb6 = pygame.image.load('images/fireball/fireball_6.png').convert()

        # Scales fireballs to this size
        fb1 = pygame.transform.scale(fb1, (32, 32))
        fb2 = pygame.transform.scale(fb2, (32, 32))
        fb3 = pygame.transform.scale(fb3, (32, 32))
        fb4 = pygame.transform.scale(fb4, (32, 32))
        fb5 = pygame.transform.scale(fb5, (32, 32))
        fb6 = pygame.transform.scale(fb6, (32, 32))
        # Stores in array to loop through
        self.images = [fb1, fb2, fb3, fb4, fb5, fb6]

        #Sets position of first fire ball
        self.dino_rect = dino_rect
        self.rect = self.images[0].get_rect()

        # Sets speed of explosion
        self.speed = settings.cactus_speed
        self.frame = 0  # Loops through frames

        # Explosion for fireball
        self.explosion = Explosion(settings, screen)

    def shoot(self):
        # Draws current fireball (frame), moves down screen
        self.screen.blit(self.images[self.frame], self.rect)
        self.update()

    def update_frames(self):
            if self.frame is 5:
                self.frame = 0
            else:
                self.frame = self.frame + 1

    def update(self):
        self.rect.centerx = self.rect.centerx + self.speed

    def off_screen(self, screen_width):
        # Returns if fireball has gone off screen
        if self.rect.x > screen_width:
            return True
        else:
            return False

    def reset(self):
        # Resets fireball when offscreen
        self.frame = 0

    def EXPLODE(self, speed):
        if self.explosion.active:
            self.rect.centerx = self.rect.centerx - speed + 3
            self.explosion.blitme(self.screen, self.rect)

            self.explosion.update()
        else:
            self.reset()
            self.explosion.reset()

class Explosion:
    def __init__(self, settings, screen):

        # Stores screen and images
        exp1 = pygame.image.load('images/fireball_hit/fb_hit_1.png').convert()
        exp2 = pygame.image.load('images/fireball_hit/fb_hit_2.png').convert()
        exp3 = pygame.image.load('images/fireball_hit/fb_hit_3.png').convert()
        exp4 = pygame.image.load('images/fireball_hit/fb_hit_4.png').convert()
        exp5 = pygame.image.load('images/fireball_hit/fb_hit_5.png').convert()
        exp6 = pygame.image.load('images/fireball_hit/fb_hit_6.png').convert()
        exp7 = pygame.image.load('images/fireball_hit/fb_hit_7.png').convert()
        exp8 = pygame.image.load('images/fireball_hit/fb_hit_8.png').convert()
        exp9 = pygame.image.load('images/fireball_hit/fb_hit_9.png').convert()

        # Scales images to screen
        exp1 = pygame.transform.scale(exp1, (64, 64))
        exp2 = pygame.transform.scale(exp2, (64, 64))
        exp3 = pygame.transform.scale(exp3, (64, 64))
        exp4 = pygame.transform.scale(exp4, (64, 64))
        exp5 = pygame.transform.scale(exp5, (64, 64))
        exp6 = pygame.transform.scale(exp6, (64, 64))
        exp7 = pygame.transform.scale(exp7, (64, 64))
        exp8 = pygame.transform.scale(exp8, (64, 64))
        exp9 = pygame.transform.scale(exp9, (64, 64))
        # Stores all frames in array
        self.images = [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9]

        self.screen = screen
        self.set = settings
        self.active = False

        self.frame = 0
        self.switch = False
        self.flip = False

    def update(self):
        self.frame = self.frame + 1

    def reset(self):
        self.active = False
        self.frame = 0

        self.switch = False
        self.flip = False

        # Covers up blitted explosion
        pygame.draw.line(self.screen,((0, 0, 0)),(0, self.set.screen_height),
        (self.set.screen_width, self.set.screen_height), 50)

    def blitme(self, screen, rect):
        if self.frame >= 19:
            self.reset()
        elif self.active:
            # Each fireball image has same dimensions so rect will work for all
            screen.blit(self.images[self.frame % 9], rect)
