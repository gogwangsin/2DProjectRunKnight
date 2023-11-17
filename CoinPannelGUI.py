from pico2d import load_image, load_font


# 코인 패널 클래스


class CoinGUI:
    def __init__(self, knight):
        self.knight = knight
        self.pannel_image = load_image("UI\\menu_gold_level.png")
        self.coin_image = load_image('UI\\gold_ui.png')
        self.font = load_font('Jalnan.ttf', 25)

    def update(self):
        pass
    def draw(self):
        self.pannel_image.clip_draw(0, 0, 279, 163, 140, 745, 279 * 0.9, 163 * 0.9)
        self.coin_image.clip_draw(0, 0, 46, 49, 100, 740, 46 * 0.9, 49 * 0.9)
        self.font.draw(60, 700, '{:>5d}'.format(int(self.knight.Coin)), (230, 230, 230))
        pass



