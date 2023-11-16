from pico2d import load_image, get_time
from sdl2 import SDL_KEYDOWN, SDLK_LEFT, SDL_KEYUP, SDLK_RIGHT
import game_framework
import over_mode
import play_mode


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

    @staticmethod
    def exit(knight, event):
        pass

    @staticmethod  # 함수를 그룹핑 하는 역할
    def do(knight):
        knight.frame = (knight.frame + knight.frames_per_action * knight.action_per_time * game_framework.frame_time) % 3
        if 700 >= knight.draw_y + knight.Dir * knight.walk_speed_pixel_per_second * game_framework.frame_time >= 80:
            knight.draw_y += knight.Dir * knight.walk_speed_pixel_per_second * game_framework.frame_time

        if knight.HP <= 30:
            knight.warning_frame = (knight.warning_frame + knight.warning_frames_per_action *
                                    knight.warning_action_per_time * game_framework.frame_time) % 10
            knight.sweat_frame = (knight.sweat_frame + knight.sweat_frames_per_action *
                                  knight.sweat_action_per_time * game_framework.frame_time) % 3

    @staticmethod
    def draw(knight):  # frame, action, 사진 가로,세로, x,y, 크기 비율
        knight.knight_image.clip_draw(int(knight.frame) * knight.knight_width,
                                      knight.action * knight.knight_height,
                                      knight.knight_width, knight.knight_height,
                                      knight.draw_x, knight.draw_y,
                                      knight.knight_draw_width, knight.knight_draw_height)
        if knight.HP <= 30:
            knight.warning_image.clip_draw(int(knight.warning_frame) * 105, 0, 105, 25,
                                           knight.draw_x - 20, knight.draw_y + 80, 105 * 0.95, 25 * 0.95)
            knight.sweat_image.clip_draw(int(knight.sweat_frame) * 66, 0, 66, 60,
                                         knight.draw_x - 80, knight.draw_y + 55, 66 * 0.8, 60 * 0.8)


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
        self.init_warnning_var()
        self.init_sweat_var()
        self.init_state_machine()

    def update(self):
        self.state_machine.update()
        self.update_hp()

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
        self.time_per_action = 0.3
        self.action_per_time = 1.0 / self.time_per_action
        self.frames_per_action = 3

        self.walk_speed_km_per_hour = 52.0  # Km / Hour
        self.walk_speed_meter_per_minute = (self.walk_speed_km_per_hour * 1000.0 / 60.0)
        self.walk_speed_meter_per_second = (self.walk_speed_meter_per_minute / 60.0)
        self.walk_speed_pixel_per_second = (self.walk_speed_meter_per_second * play_mode.pixel_per_meter)

        self.HP = 100
        self.Dir = 0
        self.HP_decrease = 0.0  # 0.03

    def init_warnning_var(self):
        # 105 x 25
        self.warning_image = load_image("UI\\warning_sign.png")

        self.warning_frame = 0
        self.warning_time_per_action = 0.6
        self.warning_action_per_time = 1.0 / self.warning_time_per_action
        self.warning_frames_per_action = 10

    def init_sweat_var(self):
        # 66 x 60
        self.sweat_image = load_image("UI\\sweat.png")

        self.sweat_frame = 0
        self.sweat_time_per_action = 0.3
        self.sweat_action_per_time = 1.0 / self.sweat_time_per_action
        self.sweat_frames_per_action = 3

    def init_state_machine(self):
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def get_current_hp(self):
        return self.HP

    def update_hp(self):
        self.HP -= self.HP_decrease  # 0.25
        if self.HP <= 0:
            self.HP, self.HP_decrease, self.Dir = 0, 0, 0
            play_mode.run_speed_pixel_per_second -= play_mode.run_speed_pixel_per_second / 150
            if play_mode.run_speed_pixel_per_second < 10:
                play_mode.run_speed_pixel_per_second = 0
            game_framework.push_mode(over_mode)