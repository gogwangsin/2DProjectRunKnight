from pico2d import load_image

# screen_width = 1280, height = 800
class ResultPannel:
    def __init__(self):
        self.menu = load_image("UI\\gold_meter_bar.png")   # self.menu.draw(400, 300)
        self.result_bar = load_image('UI\\result_bar.png') # result_bar 431 x 165
        self.regame_button = load_image('UI\\regame_button.png') # regame_button 243 x 87
        self.coin = load_image('UI\\coin.png') # coin 81 x 81
        self.screen_width = 1280
        self.screen_height = 800

    def draw(self):
        self.menu.clip_draw(0, 0, 667, 426, self.screen_width // 2, self.screen_height // 2, 667, 426)
        self.result_bar.clip_draw(0, 0, 431, 165, self.screen_width // 2, self.screen_height - 73, 431, 165)
        self.regame_button.clip_draw(0, 0, 243, 87, self.screen_width // 2, 135, 243 * 1.1, 87 * 1.1)

    def update(self):
        pass