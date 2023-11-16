from pico2d import load_image, load_font


# HP 클래스


class HP:
    def __init__(self, knight):
        self.knight = knight
        self.init_hp_var()
        self.font = load_font('Jalnan.ttf', 30)

    def update(self):
        self.scale_factor = self.knight.get_current_hp() / 100  # 현재체력 / 최대체력 -> 비율
        self.HP_draw_width = 657 * self.scale_factor  # 그릴 길이 x 체력비율 매핑
        self.HP_draw_x = 640 - (self.HP_width - self.HP_draw_width) / 2
        # print('용사 체력 :', self.knight.get_current_HP())  # hp에 따라 길이 조절 -> scale_factor 수정\

    def draw(self):
        # HP 템플릿 크기 675, 84 [ 상수 -> 안변함 ]
        self.HP_template_image.clip_draw(0, 0, 675, 84, 640, 750, 675, 37 * 1.5)

        self.HP_image.clip_draw(0, 0, self.HP_width, self.HP_height,
                                self.HP_draw_x, self.HP_draw_y, self.HP_draw_width, self.HP_draw_height)

        self.font.draw(320, 748, 'HP', (230, 230, 230))
        self.font.draw(830, 748, '{:3d}'.format(int(self.knight.get_current_hp())), (230, 230, 230))
        self.font.draw(880, 748, '/100', (230, 230, 230))

    def init_hp_var(self):
        self.HP_image = load_image("UI\\HP_bar.png")
        self.HP_template_image = load_image("UI\\HP_back_bar.png")

        self.HP_width = 657
        self.HP_height = 37  # 한개 사진 크기

        self.scale_factor = 1.0
        self.HP_draw_width = 657 * 1.0  #
        self.HP_draw_height = 37 * 1.0  # 사진 그릴 크기 [ 비율 조정 ]

        self.HP_draw_x, self.HP_draw_y = 640, 750  # 그릴 피봇 -> 스크린 크기 ( 1280, 800 )
