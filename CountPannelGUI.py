from pico2d import load_image, load_font
# 코인 패널 클래스


class MonsterCountGUI:
    def __init__(self, knight):
        self.knight = knight
        self.count_image = load_image('UI\\count_korean.png')
        self.font = load_font('Jalnan.ttf', 20)

    def update(self):
        pass

    def draw(self):
        self.count_image.clip_draw(0, 0, 500, 300, 222, 740, 500 * 0.3, 300 * 0.3)
        self.font.draw(175, 720, '{:>5d}'.format(int(self.knight.Count)), (230, 230, 230))
