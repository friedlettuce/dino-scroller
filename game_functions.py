import sys, pygame
from pygame.sprite import spritecollideany
from background import City
from cactus import Cactus

def check_events(settings, play_button, dino, cacti):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                reset(settings, dino)
                cacti.empty()

            elif event.key == pygame.K_SPACE:
                if not settings.play:
                    settings.play = True
                else:
                    dino.jump()

            # Shoots fireball if 1 is available
            elif event.key == pygame.K_f and settings.fireball_count > 0:
                dino.set_fireball()
                settings.fireball = True
                settings.fireball_count = settings.fireball_count - 1

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                dino.frame = 1 # Makes dino not stand
                settings.play = True

    # Resets game if collide
    if spritecollideany(dino, cacti):
        reset(settings, dino)
        cacti.empty()

    # Every 10 scored gives 1 fireball
    if settings.score % 10 == 0 and settings.score > 9:
        settings.fireball_count = settings.fireball_count + 1

def draw_background(set, ct1, ct2, sun, sb):
    # Draw ground and background
    ct1.blitme()
    ct2.blitme()
    sun.blitme()

    if set.play:
        sb.show_score()
    ct1.tower.blitme()
    ct2.tower.blitme()


def draw_screen(set, play_button, high_score, dino, cacti):
    # Draw cacti and animates dino
    if set.play:
        for cactus in cacti.sprites():
            cactus.draw()

        set.switch = set.switch + 1

        if set.switch == 5:
            if set.rotation == 5:
                set.rotation = 1
            else:
                set.rotation = set.rotation + 1
            set.switch = 0
    else:
        play_button.draw_button()

    # Draws dino with animation, blits fireball
    dino.blitme(set)

    if not set.play:
        high_score.show_score()
    pygame.display.update()

def make_cactus(set, screen, cacti):

    # Makes new cacti when less than 3 on screen
    limit = len(cacti)

    if limit < set.cacti_allowed:
        new_cactus = Cactus(set, screen)
        cacti.add(new_cactus)

def update_cacti(set, cacti, fireball):
    for cactus in cacti:
        cactus.update()

    # If offscreen or collides with fireball, removes, or turns fireball off and explodes
    for cactus in cacti:
        if cactus.rect.x < 0:
            cacti.remove(cactus)

        elif fireball.rect.collidepoint(
                cactus.rect.left, cactus.rect.centery) and set.fireball:
            cacti.remove(cactus)
            fireball.explosion.active = True
            set.fireball = False

def check_score(set, dino, cacti):
    # Adds to score each cactus jumped
    for cactus in cacti.copy():
        if cactus.rect.x < dino.rect.x and not cactus.scored:
              set.score = set.score + 1
              cactus.scored = True

def reset(set, dino):
    # Pauses game, resets score
    set.play = False

    if set.score > set.high_score:
        set.high_score = set.score
    set.score = 0
    # So fireball can't be shot when restarting
    set.fireball = False
    set.fireball_count = 0
    set.gain_fb = False
    # Tracks frames for dino, can I just control inside of dino?
    set.rotation = 0
    set.switch = 0
    set.frame = 0
    # Makes dino stand
    dino.frame = 0
    dino.timer = 0
