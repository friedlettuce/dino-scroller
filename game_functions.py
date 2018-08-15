import sys, pygame
from pygame.sprite import spritecollideany
from background import City
from cactus import Cactus

def check_events(set, play_button, diego, cacti):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                set.reset()
                cacti.empty()
            elif event.key == pygame.K_SPACE:
                diego.jump(set)
            elif event.key == pygame.K_f and set.gain_fb:
                set.fireball = True
                set.gain_fb = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                set.play = True

    if spritecollideany(diego, cacti):
        set.reset()
        cacti.empty()

    if set.score % 10 == 0:
        set.gain_fb = True

def update_screen(set, ct1, ct2, twr, sun, sb, play_button, diego, cacti):
    # Draw ground and background
    ct1.blitme()
    ct2.blitme()
    sun.blitme()

    if set.play:
        sb.show_score()
    twr.blitme()
    # Draw character and update screen
    if set.play:
        for cactus in cacti.sprites():
            cactus.draw()

        set.switch = set.switch + 1

        if set.switch == 3:
            if set.rotation == 5:
                set.rotation = 1
            else:
                set.rotation = set.rotation + 1
            set.switch = 0
    diego.blitme(set)

    if not set.play:
        play_button.draw_button()

    pygame.display.flip()

def make_cactus(set, screen, cacti):
    if len(cacti) < set.cacti_allowed:
        new_cactus = Cactus(set, screen)
        cacti.add(new_cactus)

    print(str(len(cacti)))

def update_cacti(set, cacti, fireball):
    cacti.update()

    for cactus in cacti.copy():
        if cactus.rect.x < 0:
            cacti.remove(cactus)
        if fireball.rect.collidepoint(cactus.rect.left, cactus.rect.centery) and set.fireball:
            cacti.remove(cactus)
            set.fireball = False
            fireball.reset()

def check_score(set, diego, cacti):
    for cactus in cacti.copy():
        if cactus.rect.x < diego.rect.x and not cactus.scored:
              set.score = set.score + 1
              cactus.scored = True
