# GUI 클래스
from pico2d import load_image


class HP:
    def __init__(self, knight_hp):
        self.hp_bar = knight_hp
        # print('용사 체력 :', self.hp_bar)

        self.image = load_image("UI\\HP_bar.png")

        self.image_size_width = 657
        self.image_size_height = 37  # 한개 사진 크기

        self.draw_size_width = 657 * 1.0  #
        self.draw_size_height = 37 * 1.3  # 사진 그릴 크기 [ 비율 조정 ]

        self.draw_x, self.draw_y = 640, 750 # 그릴 피봇 -> 스크린 크기 ( 1280, 800 )

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, self.image_size_width, self.image_size_height,
                             self.draw_x, self.draw_y, self.draw_size_width, self.draw_size_height)
        pass


class GUI:
    def __init__(self, knight):
        GUI.HP = HP(knight.get_hp())
        pass

    def update(self):
        pass


    def draw(self):
        GUI.HP.draw()
        pass