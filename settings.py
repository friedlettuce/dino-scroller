class Settings:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 300
        self.bg_color = 255, 255, 255

        self.ground = y = self.screen_height - 20
        self.buffer = .03

        self.cactus_speed = .00003
        self.cacti_allowed = 2
