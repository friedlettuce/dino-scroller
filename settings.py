class Settings:
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 356
        self.bg_color = 227, 154, 171
        self.play = False

        self.ground = self.screen_height - 20

        self.cactus_speed = 7
        self.cacti_allowed = 3
        self.score = 0

        self.rotation = 0
        self.switch = 0
        self.frame = 0

        self.fireball = False
        self.gain_fb = False
        self.explode = False

    def reset(self):
        self.play = False
        self.score = 0
        self.rotation = 0
        self.switch = 0
        self.frame = 0
