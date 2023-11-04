from pico2d import load_image
import global_var

# 왕성 길


class KingDom:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height  # 화면 스크린 크기

        self.init_back_sky_var()
        self.init_back_column_var()
        self.init_kingdom_road_var()

    def draw(self):
        self.draw_back_sky_image()
        self.draw_back_column_image()
        self.draw_kingdom_road_image()

    def update(self):
        self.update_back_sky()
        self.update_back_column()
        self.update_kingdom_road()

    def init_kingdom_road_var(self):
        self.road_image = load_image("BackGround\\road_background.png")

        self.road_width = 1280
        self.road_height = 574  # 사진 원본 크기

        self.road_draw_width = 1280
        self.road_draw_height = 720  # 사진 그릴 크기

        self.road_draw_x = self.screen_width // 2  # 사진 그릴 위치 (x,y)
        self.road_draw_y = self.screen_height // 2 - 45  # 사진 비율 조정으로 인한 y 조절

    def draw_kingdom_road_image(self):
        # 왕성 사진 1 -> [ O ][ ][ ]
        self.road_image.clip_draw(0, 0, self.road_width, self.road_height,
                                  self.road_draw_x, self.road_draw_y,
                                  self.road_draw_width, self.road_draw_height)

        # 왕성 사진 2 -> [ ][ O ][ ]
        self.road_image.clip_draw(0, 0, self.road_width, self.road_height,
                                  self.road_draw_x + self.road_width, self.road_draw_y,
                                  self.road_draw_width, self.road_draw_height)

        # 왕성 사진 3 -> [ ][ ][ O ]
        self.road_image.clip_draw(0, 0, self.road_width, self.road_height,
                                  self.road_draw_x + self.road_width * 2, self.road_draw_y,
                                  self.road_draw_width, self.road_draw_height)

        # 사진 픽셀 시작 위치 (왼쪽 하단 0,0) / 사진 크기 / 그릴 위치(사진 중앙이 pivot) // 그릴 크기 조정 1280, 720
        # (0,0, 1280, 574, drawX,drawY, 1280, 720)

    def update_kingdom_road(self):
        self.road_draw_x -= global_var.scroll_speed
        if self.road_draw_x < -self.road_width:
            self.road_draw_x = 0

    def init_back_sky_var(self):
        self.sky_image = load_image("BackGround\\sky_background.png")

        self.sky_width = 1280
        self.sky_height = 376  # 사진 원본 크기

        self.sky_draw_width = 1280
        self.sky_draw_height = 376  # 사진 그릴 크기

        self.sky_draw_x = self.screen_width // 2  # 사진 그릴 위치 (x,y)
        self.sky_draw_y = self.screen_height // 2 + 280  # 사진 비율 조정으로 인한 y 조절

    def draw_back_sky_image(self):
        self.sky_image.clip_draw(0, 0, self.sky_width, self.sky_height,
                                 self.sky_draw_x, self.sky_draw_y,
                                 self.sky_draw_width, self.sky_draw_height)

        # 뒷 배경 사진 2 -> [ ][ O ][ ]
        self.sky_image.clip_draw(0, 0, self.sky_width, self.sky_height,
                                 self.sky_draw_x + self.sky_width, self.sky_draw_y,
                                 self.sky_draw_width, self.sky_draw_height)

        # 뒷 배경 사진 3 -> [ ][ ][ O ]
        self.sky_image.clip_draw(0, 0, self.sky_width, self.sky_height,
                                 self.sky_draw_x + self.sky_width * 2, self.sky_draw_y,
                                 self.sky_draw_width, self.sky_draw_height)

    def update_back_sky(self):
        self.sky_draw_x -= global_var.scroll_speed * 0.60   # 하늘 레이어 속도 조정 변경 가능
        if self.sky_draw_x < -self.sky_width:
            self.sky_draw_x = 0

    def init_back_column_var(self):
        self.column_image = load_image("BackGround\\column_background.png")

        self.column_width = 970
        self.column_height = 234  # 사진 원본 크기

        self.column_draw_width = 970
        self.column_draw_height = 234  # 사진 그릴 크기

        self.column_draw_x = self.screen_width // 2  # 사진 그릴 위치 (x,y)
        self.column_draw_y = self.screen_height // 2 + 330  # 사진 비율 조정으로 인한 y 조절

    def draw_back_column_image(self):
        # 기둥 사진 1 -> [ O ][ ]
        self.column_image.clip_draw(0, 0, self.column_width, self.column_height,
                                    self.column_draw_x, self.column_draw_y,
                                    self.column_draw_width, self.column_draw_height)

        # 기둥 사진 2 -> self.column_width * 1.5 == 그냥 원본은 기둥이 끝에 있어서 간격이 좁아서 거리를 두고 사이클을 돌도록 함
        self.column_image.clip_draw(0, 0, self.column_width, self.column_height,
                                    self.column_draw_x + self.column_width * 1.5, self.column_draw_y,
                                    self.column_draw_width, self.column_draw_height)

        self.column_image.clip_draw(0, 0, self.column_width, self.column_height,
                                    self.column_draw_x + self.column_width * 3.0, self.column_draw_y,
                                    self.column_draw_width, self.column_draw_height)

    def update_back_column(self):
        self.column_draw_x -= global_var.scroll_speed
        if self.column_draw_x < -self.column_width * 1.5:
            self.column_draw_x = 0
