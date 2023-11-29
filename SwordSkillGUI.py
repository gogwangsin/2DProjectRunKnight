from pico2d import load_image


class SwordGUI:
    def __init__(self, knight):
        self.knight = knight
        self.image = load_image("UI\\sword3_skill_button.png")
        self.draw_x, self.draw_y = 920, 105  # 그릴 피봇 -> 스크린 크기 ( 1280, 800 )

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.knight.sword_mode * 121, 0, 121, 117, self.draw_x, self.draw_y, 121, 117)
