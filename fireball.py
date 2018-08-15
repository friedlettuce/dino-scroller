import pygame

class Fireball:
    def __init__(self, screen, dino_rect):
        self.screen = screen
        fb1 = pygame.image.load('images/fireball/fireball_1.png').convert()
        fb2 = pygame.image.load('images/fireball/fireball_2.png').convert()
        fb3 = pygame.image.load('images/fireball/fireball_3.png').convert()
        fb4 = pygame.image.load('images/fireball/fireball_4.png').convert()
        fb5 = pygame.image.load('images/fireball/fireball_5.png').convert()
        fb6 = pygame.image.load('images/fireball/fireball_6.png').convert()

        fb1 = pygame.transform.scale(fb1, (32, 32))
        fb2 = pygame.transform.scale(fb2, (32, 32))
        fb3 = pygame.transform.scale(fb3, (32, 32))
        fb4 = pygame.transform.scale(fb4, (32, 32))
        fb5 = pygame.transform.scale(fb5, (32, 32))
        fb6 = pygame.transform.scale(fb6, (32, 32))

        self.images = [fb1, fb2, fb3, fb4, fb5, fb6]

        self.dino_rect = dino_rect
        self.rect = self.images[0].get_rect()
        self.rect.right = dino_rect.right
        self.rect.centery = dino_rect.centery - 3

    def shoot(self, frame):
        self.screen.blit(self.images[frame], self.rect)
        self.rect.centerx = self.rect.centerx + 5

    def off_screen(self, screen_width):
        if self.rect.x > screen_width:
            return True
        else:
            return False

    def reset(self):
        self.rect.right = self.dino_rect.right
        self.rect.centery = self.dino_rect.centery - 3

'''
class Explosion:
    def __init__(self, set, screen):
        print("Hello")
'''
