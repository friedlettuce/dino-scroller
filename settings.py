class Settings:
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 356
        self.ground = self.screen_height - 20
        self.bg_color = 227, 154, 171   # Playbutton

        self.play = False
        # Cacti
        self.cactus_speed = 7
        self.cacti_allowed = 3
        self.score = 0
        # Dino
        self.rotation = 0
        self.switch = 0
        self.frame = 0
        # Fireball
        self.fireball = False
        self.gain_fb = False
        self.explode = False
        self.fireball_speed = 10
