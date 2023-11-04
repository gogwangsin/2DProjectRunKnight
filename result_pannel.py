from pico2d import load_image

class ResultPannel:
    def __init__(self):
        self.menu = load_image("UI\\gold_meter_bar.png")

    def draw(self):
        self.menu.draw(400, 300)

    def update(self):
        pass