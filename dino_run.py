import pygame
from pygame.sprite import Group
import random
from time import sleep

from settings import Settings
import game_functions as gf

from background import *
from dino import Dino

def run_game():
    pygame.init()
    set = Settings()

    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Dino Run")

    # Creates background
    sun = Sun(set, screen)
    ct1 = City(set, screen, 1)
    ct2 = City(set, screen, 2)
        # Active game scoreboard
    sb = Scoreboard(set, screen)
        # High score shows when game paused
    high_score = Scoreboard(set, screen)
        # Playbutton - to start game
    play_button = Button(set, screen, "Play")

    # Creates game objects
    dino = Dino(set, screen)
    cacti = Group()
    dino.jump()    # Initialize jump for player

    while True:
        # Checks jump, fireball, dino/cacti collisions
        gf.check_events(set, play_button, dino, cacti)

        if set.play:
            # Updates city movement
            ct1.update()
            ct2.update()
            sb.prep_score(set)  # Preps scoreboard

        if set.play:
            # Checks for fireball collision or offscreen cacti
            gf.update_cacti(set, cacti, dino.fireball)
            dino.update(set)    # Updates dino, fireball, explosion
            gf.check_score(set, dino, cacti)

            if random.randint(0, 10) > 8:   # Need better spawning method
                gf.make_cactus(set, screen, cacti)
        else:
            high_score.prep_score(set, True)
            high_score.prep_score(set, True)
            high_score.show_score()

        gf.draw_background(set, ct1, ct2, sun, sb)
        gf.draw_screen(set, play_button, high_score, dino, cacti)

        sleep(.03)  # Gets around 34 frames a second

run_game()
