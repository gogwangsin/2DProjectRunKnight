from pico2d import load_image, get_time
import global_var

# 용사 객체

class Knight:
    def __init__(self):
        self.init_knight_var()

    def update(self):

        if self.get_time_gap() > self.update_frame_time:
            self.knight_frame = (self.knight_frame + 1) % 3
            self.last_frame_update_time = get_time()

        self.knight_HP -= 0.25
        if self.knight_HP <= 0:
            print('용사 사망')
            global_var.running = False
            return

        # global_var.scroll_speed = 0


    def get_time_gap(self):
        return get_time() - self.last_frame_update_time

    def handle_event(self, event):
        pass

    def draw(self):
        self.knight_image.clip_draw(self.knight_frame * self.knight_width, self.knight_action * self.knight_height,
                                    self.knight_width, self.knight_height, self.knight_draw_x, self.knight_draw_y,
                                    self.knight_draw_width, self.knight_draw_height)


    def get_current_HP(self):
        return self.knight_HP


    def init_knight_var(self):
        self.knight_image = load_image("Object\\KnightSprite.png")

        self.knight_width = 146
        self.knight_height = 241  # 한개 사진 크기

        self.knight_draw_width = 146 * 1.1  # 원본 1.2배
        self.knight_draw_height = 241 * 1.1  # 사진 그릴 크기 [ 비율 조정 ]

        self.knight_draw_x, self.knight_draw_y = 250, 400

        self.knight_frame = 0
        self.knight_action = 0  # 0 걷기, 1 찌르기 2, 점프 공격
        self.knight_HP = 100

        self.last_frame_update_time = get_time()
        self.update_frame_time = 0.08  # 프레임 업데이트 시간 간격 : 0.8 -> 스크롤 속도에 영향 받음
