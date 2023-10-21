from pico2d import load_image
# HP 클래스

class HP:
    def __init__(self, knight):
        self.knight = knight

        self.hp_image = load_image("UI\\HP_bar.png")
        self.hp_bar_image = load_image("UI\\HP_back_bar.png")

        self.image_size_width = 657
        self.image_size_height = 37  # 한개 사진 크기

        self.draw_size_width = 657 * 1.0  #
        self.draw_size_height = 37 * 1.0  # 사진 그릴 크기 [ 비율 조정 ]

        self.draw_x, self.draw_y = 640, 750 # 그릴 피봇 -> 스크린 크기 ( 1280, 800 )

    def update(self):
        print('용사 체력 :', self.knight.get_hp()) # hp에 따라 길이 조절
        pass

    def draw(self):
        self.hp_bar_image.clip_draw(0, 0, 675, 84,
                                self.draw_x, self.draw_y, 675, 37*1.5)

        self.hp_image.clip_draw(0, 0, self.image_size_width, self.image_size_height,
                                self.draw_x, self.draw_y, self.draw_size_width, self.draw_size_height)

