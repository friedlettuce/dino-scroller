import sys, pygame
from cactus import Cactus

def check_events(set, diego):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    diego.jump(set)

def update_screen(set, screen, diego, cacti):
    # Draw ground and background
    screen.fill(set.bg_color)
    pygame.draw.line(screen, (0,0,0),
            (0, set.ground), (set.screen_width, set.ground), 2)
    # Draw character and update screen
    diego.blitme()
    for cactus in cacti.sprites():
        cactus.draw()

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
