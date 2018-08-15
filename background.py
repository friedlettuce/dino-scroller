import pygame
from pygame.sprite import Sprite
import pygame.font

class Sun:
    def __init__(self, set, screen):
        self.screen = screen
        self.image = pygame.image.load('images\\sun.jpg').convert()

        self.rect = self.image.get_rect()
        screen_rect = self.screen.get_rect()

        self.rect.x = screen_rect.left + 20
        self.rect.top = screen_rect.top + 10

    def blitme(self):
        self.screen.blit(self.image, self.rect)

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

    def update(self, twr):
        self.rect.x = self.rect.x - self.speed
        twr.rect.x = twr.rect.x - int(self.speed / 2)

        if self.rect.x <= self.boundary:
            self.reset(twr)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def reset(self, twr):
        if self.num is 1:
            self.rect.x = 0
            twr.rect.x = 0
        elif self.num is 2:
            self.rect.x = self.screen_width
            twr.rect.x = self.screen_width

class Tower:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images\\tower.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = 715
        self.rect.bottom = 65

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Scoreboard:
    def __init__(self, set, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.set = set

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

    def prep_score(self, set):
        score = str(set.score)
        self.score_img = self.font.render(score, True, self.text_color,
                    self.set.bg_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
