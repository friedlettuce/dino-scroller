import pygame
from time import sleep

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
