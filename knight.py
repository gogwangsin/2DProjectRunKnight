from pico2d import load_image


class Knight:
    def __init__(self):
        self.draw_x, self.draw_y = 300, 400
        self.frame = 0
        self.action = 0 # 0 걷기, 1 찌르기 2, 점프 공격

        self.image = load_image("Object\\KnightSprite.png")

        self.image_size_width = 146
        self.image_size_height = 241  # 한개 사진 크기

        self.draw_size_width = 146 * 1.2 # 원본 1.2배
        self.draw_size_height = 241 * 1.2 # 사진 그릴 크기 [ 비율 조정 ]
        pass

    def update(self):
        self.frame = (self.frame + 1) % 3
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * self.image_size_width, self.action * self.image_size_height,
                             self.image_size_width, self.image_size_height, self.draw_x, self.draw_y,
                             self.draw_size_width,self.draw_size_height)

        # self.image.clip_draw(0, 0, self.image_size_width, self.image_size_height,
                             # self.draw_x, self.draw_y, self.draw_size_width, self.draw_size_height)

        # 사진 픽셀 시작 위치 (왼쪽 하단 0,0) / 사진 크기 / 그릴 위치(사진 중앙이 pivot) // 그릴 크기 조정 1280, 720
        # 프레임 x 사진 한개 가로, 액션 x 사진 한개 세로 : 사진 픽셀 왼쪽 하단
        # 사진 가로 크기(한개), 사진 세로 크기(한개), 그릴 위치 임의로 300,400 [변수임]
        # 그릴 사진 크기[ 배수로 비율 늘림 ] 1.2배

