from pico2d import load_image


# 왕성 길


class KingDom:
    def __init__(self, screen_width, screen_height):
        self.image = load_image("BackGround\\road_background.png")

        self.screen_width = screen_width
        self.screen_height = screen_height # 화면 스크린 좌표 저장

        self.draw_x = self.screen_width // 2 # 사진 그릴 위치 (x,y)
        self.draw_y = self.screen_height // 2 - 45

    def draw(self):
        # self.image.draw(self.x, self.y)
        self.image.clip_draw(0, 0, self.screen_width, self.screen_height, self.draw_x, self.draw_y, 1280, 720)
        # self.image.clip_draw(0, 0, self.screen_width, self.screen_height, self.screen_width // 2, self.screen_height // 2 - 45, 1280, 720)

        # 사진 그릴 중심 (왼쪽 하단 0,0) / 사진 크기 / 그릴위치(사진중앙이 pivot) // 그릴 크기 조정 1280, 720

        # 사진 왼쪽아래(x), 사진(y), 그릴크기(x), 그릴(y), 실제x, y
        # clip_draw(frame * 100, 0, 100, 100, x, 130, 200, 200)

    def update(self):
        pass

