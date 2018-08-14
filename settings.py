class Settings:
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 356
        self.bg_color = 255, 255, 255
        self.play = False

        self.ground = y = self.screen_height - 20
        self.buffer = .03

        self.cactus_speed = 10
        self.cacti_allowed = 2
        self.cacti_survived = 0

    def reset(self):
        self.play = False
        self.cactus_speed = 10
        self.cacti_survived = 0
