class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry"""

    def __init__(self):
        """ Inicjalizacja danych statystycznych gry """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku

        self.ship_limit = 3
        # Ustawienia dotyczące pocisków
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        # Easy zmiana szybkości gry
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Inicjalizacja ustawień, które ulegają zmianie w trakcie gry """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # Wartość fleet_direction wynosząca 1 oznacza w prawo natomiast -1 w lewo
        self.fleet_direction = 1
        # Punktacja
        self.alien_points = 50
        self.score_scale = 1.5

    def increase_speed(self):
        """ Zmiana ustawień dotyczących szybkości gry i liczby przyznawanych punktów. """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)




