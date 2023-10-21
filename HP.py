from pico2d import load_image
# HP 클래스


class HP:
    def __init__(self, knight):
        self.knight = knight

        self.hp_image = load_image("UI\\HP_bar.png")
        self.hp_template_image = load_image("UI\\HP_back_bar.png")

        self.image_size_width = 657
        self.image_size_height = 37  # 한개 사진 크기

        self.scale_factor = 1.0
        self.draw_size_width = 657 * 1.0  #
        self.draw_size_height = 37 * 1.0  # 사진 그릴 크기 [ 비율 조정 ]

        self.draw_x, self.draw_y = 640, 750 # 그릴 피봇 -> 스크린 크기 ( 1280, 800 )

    def update(self):
        # if self.scale_factor >= 0:
        if self.scale_factor >= 0:
            self.scale_factor -= 0.0005
        else:
            self.scale_factor = 1.0
        self.draw_size_width = 657 * self.scale_factor  #

        self.draw_x = 640 - (self.image_size_width - self.draw_size_width) / 2
        print('용사 체력 :', self.knight.get_hp()) # hp에 따라 길이 조절 -> scale_factor 수정
        pass

    def draw(self):
        # HP틀 크기 675, 84 [ 상수 -> 안변함 ]
        self.hp_template_image.clip_draw(0, 0, 675, 84, 640, 750, 675, 37 * 1.5)

        self.hp_image.clip_draw(0, 0, self.image_size_width, self.image_size_height,
                                self.draw_x, self.draw_y, self.draw_size_width, self.draw_size_height)



# 원래 self.draw_x는 사진을 그릴 위치를 가리키는데,
# 원래 크기와 새로운 크기 간의 차이를 반으로 나누어 오른쪽으로 이동한다.
# -> 줄어든 사진 크기의 절반 값을 원래의 draw_x에 +-한다.

# 결과적으로, 비율을 조정하고 오른쪽으로 이동시켜 가운데 정렬을 유지함으로써
# 원하는 비율로 축소된 사진을 그릴 수 있다.
# 이러한 방식으로 사진을 조정하면 화면 상에서 오른쪽으로만 줄어들게 된다.