import pygame

class Sun:
    def __init__(self, set, screen):
        self.screen = screen
        self.image = pygame.image.load('images\\sun.jpg').convert()

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = int(set.screen_width / 6)
        self.rect.centery = 40

    def blitme(self):
        self.screen.blit(self.image, self.rect)
