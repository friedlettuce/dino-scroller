import sys, pygame
from pygame.sprite import spritecollideany
from background import City
from cactus import Cactus

def check_events(set, play_button, diego, cacti):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    diego.jump(set)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                set.play = True

    if spritecollideany(diego, cacti):
        set.reset()
        cacti.empty()

def update_screen(set, ct1, ct2, twr, sun, sb, play_button, diego, cacti):
    # Draw ground and background
    ct1.blitme()
    ct2.blitme()
    sun.blitme()

    if set.play:
        sb.show_score()
    twr.blitme()
    # Draw character and update screen
    diego.blitme()
    if set.play:
        for cactus in cacti.sprites():
            cactus.draw()

    if not set.play:
        play_button.draw_button()

    pygame.display.flip()

def make_cactus(set, screen, cacti):
    if len(cacti) < set.cacti_allowed:
        new_cactus = Cactus(set, screen)
        cacti.add(new_cactus)

def update_cacti(set, cacti):
    cacti.update()

    for cactus in cacti.copy():
        if cactus.rect.x < 0:
            cacti.remove(cactus)

def check_score(set, diego, cacti):
    for cactus in cacti.copy():
        if cactus.rect.x < diego.rect.x and not cactus.scored:
              set.score = set.score + 1
              cactus.scored = True
