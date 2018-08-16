import pygame
from pygame.sprite import Group
import random
from time import sleep

from settings import Settings
import game_functions as gf

from background import Sun, City, Tower, Scoreboard
from button import Button
from dino import Dino

def run_game():
    pygame.init()
    set = Settings()

    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Dino Run")

    # Creates sun and the city
    sun = Sun(set, screen)
    ct1 = City(set, screen, 1)
    ct2 = City(set, screen, 2)
    # Creates play button and scoreboard
    play_button = Button(set, screen, "Play")
    sb = Scoreboard(set, screen)
    # Creates game objects
    diego = Dino(set, screen)
    cacti = Group()

    while True:
        gf.check_events(set, play_button, diego, cacti)

        if set.play:
            ct1.update()
            ct2.update()
            sb.prep_score(set)

        gf.update_cacti(set, cacti, diego.fireball)
        if set.play is True and random.randint(0, 20) > 7:
            gf.make_cactus(set, screen, cacti)   
        
        diego.update(set)

        sleep(.03)
        gf.check_score(set, diego, cacti)

        gf.update_screen(set, ct1, ct2, sun, sb, play_button, diego, cacti)

run_game()
