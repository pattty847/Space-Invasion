from random import randint


class Settings():
    """Where we will change/update new settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 700
        self.color = (5, 20, 33)
        self.ship_speed_fac = float(10)
        self.version = "v1.0"
        self.author = "By. Pat "

        #Normal Bullet settings
        self.norm_bullet_speed = 50
        self.norm_bullet_width = 5
        self.norm_bullet_height = 20
        self.norm_bullet_color = 226, 0, 0
        self.norm_bullet_allowed = 5

        #Missel settings
        self.missel_speed = 15
        self.missel_width = 6
        self.missel_height = 20
        self.missel_color = 50, 60, 70
        self.missel_speed = 40

        #Alien settings
        self.fleet_speed_factor = 5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
        self.ships_allowed = 3
