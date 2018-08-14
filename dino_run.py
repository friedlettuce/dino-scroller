import pygame
from pygame.sprite import Group
import random
from time import sleep

from settings import Settings
import game_functions as gf
from sun import Sun
from city import City
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

    # Creates play button
    play_button = Button(set, screen, "Play")

    # Creates game objects
    diego = Dino(set, screen)
    cacti = Group()

    while True:
        if random.randint(0, 30) > 21:
            gf.make_cactus(set, screen, cacti)

        gf.check_events(set, play_button, diego, cacti)

        if set.play:
            ct1.update()
            ct2.update()
        diego.update(set)
        gf.update_cacti(set, cacti)
        sleep(set.buffer)

        gf.update_screen(set, ct1, ct2, sun, play_button, diego, cacti)

run_game()
