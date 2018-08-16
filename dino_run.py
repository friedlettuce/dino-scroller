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

    # Creates background
    sun = Sun(set, screen)
    ct1 = City(set, screen, 1)
    ct2 = City(set, screen, 2)
    sb = Scoreboard(set, screen)
        # Playbutton - to start game
    play_button = Button(set, screen, "Play")
    
    # Creates game objects
    diego = Dino(set, screen)
    cacti = Group()

    while True:
        # Checks jump, fireball, dino/cacti collisions
        gf.check_events(set, play_button, diego, cacti)

        if set.play:
            # Updates city movement
            ct1.update()
            ct2.update()
            sb.prep_score(set)
    
        gf.update_cacti(set, cacti, diego.fireball)
        diego.update(set)
        
        if set.play is True:
            gf.make_cactus(set, screen, cacti)   
        
        # Updates dino/fireball/explosion

        gf.check_score(set, diego, cacti)

        gf.draw_background(set, ct1, ct2, sun, sb)
        gf.draw_screen(set, play_button, diego, cacti)

run_game()
