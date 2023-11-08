from pico2d import load_image, get_time
from sdl2 import SDL_KEYDOWN, SDLK_LEFT, SDL_KEYUP, SDLK_RIGHT

import game_framework
import global_var
import over_mode


# 용사 객체

def left_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_LEFT


def left_up(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYUP and event[1].key == SDLK_LEFT


def right_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_RIGHT


def right_up(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYUP and event[1].key == SDLK_RIGHT


def time_out(event):
    return event[0] == 'TIME_OUT'


# =========================================================
class Run:

    @staticmethod
    def entry(knight, event):
        # 키 flag : 한번 눌렀을 때 방향 정해짐
        if left_down(event):
            knight.Dir += 1
        elif right_down(event):
            knight.Dir -= 1
        elif left_up(event):
            knight.Dir -= 1
        elif right_up(event):
            knight.Dir += 1

        knight.action = 0  # 0 걷기, 1 찌르기 2, 점프 공격
        knight.last_frame_time = get_time()
        knight.update_frame_time = 0.085  # 프레임 업데이트 시간 간격 : 0.8 -> 스크롤 속도에 영향 받음 : 0.08

    @staticmethod
    def exit(knight, event):
        pass

    @staticmethod  # 함수를 그룹핑 하는 역할
    def do(knight):
        if get_time() - knight.last_frame_time > knight.update_frame_time:
            knight.frame = (knight.frame + 1) % 3
            knight.last_frame_time = get_time()

        if 700 >= knight.draw_y + knight.Dir * 6.5 >= 80:
            knight.draw_y += knight.Dir * 6.5

    @staticmethod
    def draw(knight):  # frame, action, 사진 가로,세로, x,y, 크기 비율
        knight.knight_image.clip_draw(knight.frame * knight.knight_width,
                                      knight.action * knight.knight_height,
                                      knight.knight_width, knight.knight_height,
                                      knight.draw_x, knight.draw_y,
                                      knight.knight_draw_width, knight.knight_draw_height)


# ==========================================================
class StateMachine:
    def __init__(self, knight):
        self.knight = knight
        self.cur_state = Run
        # 상태 전환 테이블
        self.transitions = {

            Run: {left_down: Run, left_up: Run, right_down: Run, right_up: Run}

        }
        pass

    def start(self):
        self.cur_state.entry(self.knight, ('START', 0))
        # entry action : event:( key == START, value == 0 )으로 전달

    def update(self):
        self.cur_state.do(self.knight)
        pass

    def draw(self):
        self.cur_state.draw(self.knight)
        pass

    def handle_event(self, event):
        # cur_state의 key,value값 하나씩 꺼내서 확인 [ex) left_down: Walk, left_up: Walk]
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(event):
                self.cur_state.exit(self.knight, event)
                self.cur_state = next_state
                self.cur_state.entry(self.knight, event)
                return True
        return False


# ==========================================================
class Knight:
    def __init__(self):
        self.init_knight_var()
        self.init_state_machine()

    def update(self):
        self.state_machine.update()
        self.update_hp()

        # global_var.scroll_speed 대쉬에 따라 속도 변화

    def draw(self):
        self.state_machine.draw()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))  # 입력 이벤트

    def init_knight_var(self):
        self.knight_image = load_image("Object\\KnightSprite.png")

        self.knight_width = 146
        self.knight_height = 241  # 한개 사진 크기

        self.knight_draw_width = 146 * 1.1  # 원본 1.2배
        self.knight_draw_height = 241 * 1.1  # 사진 그릴 크기 [ 비율 조정 ]

        self.draw_x, self.draw_y = 250, 400  # 250은 사실 고정이라고 생각해도 됨 물리좌표

        self.frame = 0
        self.HP = 100
        self.Dir = 0

    def init_state_machine(self):
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def get_current_hp(self):
        return self.HP

    def update_hp(self):
        self.HP -= 1.0 # 0.25
        if self.HP <= 0:
            self.Dir = 0
            # 스크롤 점점 줄여서 천천히 멈추게 관성 효과
            if global_var.scroll_speed > 0:
                # self.draw_x -= global_var.scroll_speed / 150
                global_var.scroll_speed -= global_var.scroll_speed / 150
            game_framework.push_mode(over_mode)

