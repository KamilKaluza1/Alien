import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez statek"""
    def __init__(self, ai_settings, screen, ship):
        """ Utworzenie obiektu pocisku w aktualnym położeniu statku """
        super(Bullet, self).__init__()
        self.screen = screen
        # Utworzenie prostokonta pocisku w punkcie (0,0) a nastepnie zdefiniowanie dla niego odpowiedniego położenia
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Położenie pocisku jest zdefinowane za pomocą wartości zmiennoprzecinkowej
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """ Poruszanie pociskiem po ekranie """
        # Uaktualnianie położenia pocisku
        self.y -= self.speed_factor
        # uaktualnienie położenia prostokąta pocisku
        self.rect.y = self.y

    def draw_bullet(self):
        """ Wyświetlanie pocisku na ekranie """
        pygame.draw.rect(self.screen, self.color, self.rect)