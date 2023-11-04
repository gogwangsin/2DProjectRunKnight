from pico2d import load_image

# screen_width = 1280, height = 800
class ResultPannel:
    def __init__(self):
        self.menu = load_image("UI\\gold_meter_bar.png")
        self.screen_width = 1280
        self.screen_height = 800

    def draw(self):
        # self.menu.draw(400, 300)
        self.menu.clip_draw(0, 0, 667, 426, self.screen_width // 2, self.screen_height // 2, 667, 426)

    def update(self):
        pass