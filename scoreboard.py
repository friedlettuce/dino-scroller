import pygame.font

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
