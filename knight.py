from pico2d import load_image, get_time
import global_var


# 용사 객체

class Walk:
    @staticmethod
    def entry(knight, event):
        print('Idle Entry Action')
        knight.frame = 0
        knight.action = 0  # 0 걷기, 1 찌르기 2, 점프 공격

        knight.last_frame_time = get_time()
        knight.update_frame_time = 0.065  # 프레임 업데이트 시간 간격 : 0.8 -> 스크롤 속도에 영향 받음 : 0.08

    @staticmethod  # 함수를 그룹핑 하는 역할
    def do(knight):
        print('Idle Doing')
        if get_time() - knight.last_frame_time > knight.update_frame_time:
            knight.frame = (knight.frame + 1) % 3
            knight.last_frame_time = get_time()

    @staticmethod
    def exit(knight, event):
        print('Idle Exit Action')
        pass

    @staticmethod
    def draw(knight):  # frame, action, 사진 가로,세로, x,y, 크기 비율
        knight.knight_image.clip_draw(knight.frame * knight.knight_width,
                                      knight.action * knight.knight_height,
                                      knight.knight_width, knight.knight_height,
                                      knight.knight_draw_x, knight.knight_draw_y,
                                      knight.knight_draw_width, knight.knight_draw_height)


# ==========================================================
class StateMachine:
    def __init__(self, knight):
        self.knight = knight
        self.cur_state = Walk
        pass

    def start(self):
        self.cur_state.entry(self.knight, ('START', 0))
        # entry action : key == START, event값 0으로 전달

    def update(self):
        self.cur_state.do(self.knight)
        pass

    def draw(self):
        self.cur_state.draw(self.knight)
        pass

    def handle_event(self):
        pass


# ==========================================================
class Knight:
    def __init__(self):
        self.init_knight_var()
        self.init_state_machine()

    def update(self):
        self.state_machine.update()

        self.knight_HP -= 0.25
        if self.knight_HP <= 0:
            print('용사 사망')
            # global_var.running = False
            self.knight_HP = 100
            return

        # global_var.scroll_speed = 0

    def draw(self):
        self.state_machine.draw()

    def handle_event(self, event):
        self.state_machine.handle_event()

    def init_knight_var(self):
        self.knight_image = load_image("Object\\KnightSprite.png")

        self.knight_width = 146
        self.knight_height = 241  # 한개 사진 크기

        self.knight_draw_width = 146 * 1.1  # 원본 1.2배
        self.knight_draw_height = 241 * 1.1  # 사진 그릴 크기 [ 비율 조정 ]

        self.knight_draw_x, self.knight_draw_y = 250, 400

        self.knight_HP = 100

    def init_state_machine(self):
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def get_current_HP(self):
        return self.knight_HP
