from pico2d import load_image
# 왕성 길


class KingDom:
    def __init__(self, screen_width, screen_height, scroll_speed):
        self.image = load_image("BackGround\\road_background.png")

        self.image_size_width = 1280
        self.image_size_height = 574  # 사진 원본 크기

        self.draw_size_width = 1280
        self.draw_size_height = 720  # 사진 그릴 크기

        self.screen_width = screen_width
        self.screen_height = screen_height  # 화면 스크린 크기

        self.draw_x = self.screen_width // 2  # 사진 그릴 위치 (x,y)
        self.draw_y = self.screen_height // 2 - 45  # 사진 비율 조정으로 인한 y 조절

        self.speed = scroll_speed

    def draw(self):
        self.image.clip_draw(0, 0, self.image_size_width, self.image_size_height,
                             self.draw_x, self.draw_y, self.draw_size_width, self.draw_size_height)

        self.image.clip_draw(0, 0, self.image_size_width, self.image_size_height,
                             self.draw_x + self.image_size_width, self.draw_y,
                             self.draw_size_width, self.draw_size_height)

        self.image.clip_draw(0, 0, self.image_size_width, self.image_size_height,
                             self.draw_x + self.image_size_width + self.image_size_width, self.draw_y,
                             self.draw_size_width, self.draw_size_height)

        # 사진 픽셀 시작 위치 (왼쪽 하단 0,0) / 사진 크기 / 그릴 위치(사진 중앙이 pivot) // 그릴 크기 조정 1280, 720
        # (0,0, 1280, 574, drawX,drawY, 1280, 720)

    def update(self):
        self.draw_x -= self.speed
        if self.draw_x < -self.image_size_width:
            self.draw_x = 0


        pass

