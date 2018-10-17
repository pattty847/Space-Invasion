import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def runGame():

    """ Initialize screen and pygame settings. """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion " + ai_settings.author + ai_settings.version)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        #Check every keystroke
        if stats.game_active:
            ship.update(screen)  # Updata the screen for
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        gf.check_events(ai_settings, screen, ship, bullets)
        for event in pygame.event.get():
            screen.fill(ai_settings.color)
            ship.blitme()
            pygame.display.flip()

runGame()