from pico2d import load_image, load_font


# screen_width = 1280, height = 800
class ResultPannel:
    def __init__(self):
        self.menu = load_image("UI\\gold_meter_bar.png")  # self.menu.draw(400, 300)
        self.result_bar = load_image('UI\\result_bar.png')  # result_bar 431 x 165
        self.restart_button = load_image('UI\\regame_button.png')  # restart_button 243 x 87
        self.coin = load_image('UI\\gold_ui.png')  # coin 81 x 81
        self.result = load_image('UI\\result.png')  # 500 x 300
        self.distance = load_image('UI\\distance.png')  # 500 x 300
        self.gold = load_image('UI\\gold.png')  # 500 x 300
        self.restart = load_image('UI\\restart.png')  # 500 x 300
        self.screen_width = 1280
        self.screen_height = 800
        self.font = load_font('Jalnan.ttf', 35)
        self.color = 225

    def draw(self):
        self.draw_result_menu()
        self.draw_main_menu()
        self.draw_restart_menu()

    def update(self):
        pass

    def draw_main_menu(self):
        self.menu.clip_draw(0, 0, 667, 426, self.screen_width // 2, self.screen_height // 2, 667, 426)
        self.distance.clip_draw(0, 0, 500, 300, self.screen_width // 2 + 13, self.screen_height // 2 + 95,
                            500 * 0.55, 300 * 0.55)
        self.gold.clip_draw(0, 0, 500, 300, self.screen_width // 2 + 13, self.screen_height // 2 - 55,
                            500 * 0.55, 300 * 0.55)
        self.coin.clip_draw(0, 0, 46, 49, self.screen_width // 2 - 70, self.screen_height // 2 - 100, 46, 49)


    def draw_result_menu(self):
        self.result_bar.clip_draw(0, 0, 431, 165, self.screen_width // 2, self.screen_height - 73, 431, 165)
        self.result.clip_draw(0, 0, 500, 300, self.screen_width // 2 + 22, self.screen_height - 125, 500 * 1, 300 * 1)

    def draw_restart_menu(self):
        self.restart_button.clip_draw(0, 0, 243, 87, self.screen_width // 2, 135, 243 * 1.1, 87 * 1.1)
        self.restart.clip_draw(0, 0, 500, 300, self.screen_width // 2 + 13, self.screen_height // 2 - 285,
                               500 * 0.65, 300 * 0.65)

