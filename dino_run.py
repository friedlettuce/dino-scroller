import pygame
from pygame.sprite import Group
import random
from time import sleep

from settings import Settings
import game_functions as gf
from dino import Dino

def run_game():
    pygame.init()
    set = Settings()

    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Dino Run")

    diego = Dino(set, screen)
    cacti = Group()

    while True:
        if random.randint(0, 30) > 25:
            gf.make_cactus(set, screen, cacti)

        gf.check_events(set, diego)
        diego.update(set)
        gf.update_cacti(set, cacti)

        gf.update_screen(set, screen, diego, cacti)

run_game()
