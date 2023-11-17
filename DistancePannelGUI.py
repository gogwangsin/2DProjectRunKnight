from pico2d import load_image, load_font

import game_framework
import play_mode


# 이동거리 패널 클래스


class DistanceGUI:
    def __init__(self, knight):
        self.knight = knight
        self.pannel_image = load_image("UI\\menu_meter.png")
        self.meter_image = load_image('UI\\meter.png')
        self.font = load_font('Jalnan.ttf', 25)

    def update(self):
        pass
    def draw(self):
        self.pannel_image.clip_draw(0, 0, 323, 138, 1150, 745, 323, 138)
        self.meter_image.clip_draw(0, 0, 500, 300, 1120, 732, 500 * 0.45, 300 * 0.45)
        self.font.draw(1035, 700, '{:>5d}'.format(int(self.knight.Coin)), (126, 122, 113))
        # self.font.draw(1035, 700, '{:>5d}'.format(int(play_mode.scroll_pixel_per_second * game_framework.frame_time)),
        #                (126, 122, 113))

        pass



