import time
import random
from pico2d import load_image, draw_rectangle
from sdl2 import SDL_KEYDOWN, SDLK_LEFT, SDL_KEYUP, SDLK_RIGHT, SDLK_e, SDLK_r, SDLK_w, SDLK_UP, SDLK_DOWN
import game_framework
import game_world
import over_mode
import play_mode
from AngelSkill import KnightAngel
from AttackedEffect import Attacked
from DashSkill import KnightDash
from HealingMotion import KnightHealing
from SwordSkill import KnightSword


# 용사 객체

def up_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_UP


def up_up(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYUP and event[1].key == SDLK_UP


def down_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_DOWN


def down_up(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYUP and event[1].key == SDLK_DOWN


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


def e_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_e


def dash_time_out(event):
    return event[0] == 'TIME_OUT' and event[1] == 4.0


def r_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_r


def angel_time_out(event):
    return event[0] == 'TIME_OUT' and event[1] == 6.0


def w_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_w


def heal_time_out(event):
    return event[0] == 'TIME_OUT' and event[1] == 3.0


# =========================================================
class Run:

    @staticmethod
    def entry(knight, event):
        # 키 flag : 한번 눌렀을 때 방향 정해짐
        if left_down(event) or up_down(event):
            knight.Dir += 1
        elif right_down(event) or down_down(event):
            knight.Dir -= 1
        elif left_up(event) or up_up(event):
            knight.Dir -= 1
        elif right_up(event) or down_up(event):
            knight.Dir += 1

    @staticmethod
    def exit(knight, event):
        global dash, angel, healing

        if e_down(event):
            knight.dash_skill()
        elif knight.dash_mode and dash_time_out(event):
            if knight.dash_cooltime:
                dash.remove()
                knight.dash_cooltime = False  # 한번만 삭제하기

        if r_down(event):
            knight.angel_skill()
        elif knight.angel_mode and angel_time_out(event):
            if knight.angel_cooltime:
                angel.set_time_over()
                knight.angel_cooltime = False

        if w_down(event):
            knight.sword_skill()
        if knight.heal_mode and heal_time_out(event):
            healing.remove()

    @staticmethod  # 함수를 그룹핑 하는 역할
    def do(knight):
        global dash_start_time, angel_start_time, heal_start_time

        if knight.HP <= 30:
            knight.warning_frame = (knight.warning_frame + knight.warning_frames_per_action *
                                    knight.warning_action_per_time * game_framework.frame_time) % 10
            knight.sweat_frame = (knight.sweat_frame + knight.sweat_frames_per_action *
                                  knight.sweat_action_per_time * game_framework.frame_time) % 3

        knight.frame = (
                                   knight.frame + knight.frames_per_action * knight.action_per_time * game_framework.frame_time) % 3
        if 700 >= knight.draw_y + knight.Dir * knight.walk_pixel_per_second * game_framework.frame_time >= 80:
            knight.draw_y += knight.Dir * knight.walk_pixel_per_second * game_framework.frame_time
            knight.layer_y = knight.draw_y - 80

        if knight.dash_mode:
            if game_framework.current_time - dash_start_time >= 8.0:  # 8초 되면 다시 가능
                knight.dash_mode = False
            elif game_framework.current_time - dash_start_time >= 4.0:
                knight.state_machine.handle_event(('TIME_OUT', 4.0))

        if knight.angel_mode:
            if game_framework.current_time - angel_start_time >= 12.0:  # 12초 되면 다시 가능
                knight.angel_mode = False
            elif game_framework.current_time - angel_start_time >= 6.0:
                knight.state_machine.handle_event(('TIME_OUT', 6.0))

        if knight.heal_mode and game_framework.current_time - heal_start_time >= 3.0:
            knight.state_machine.handle_event(('TIME_OUT', 3.0))

    @staticmethod
    def draw(knight):  # frame, action, 사진 가로,세로, x,y, 크기 비율
        knight.knight_image.clip_draw(int(knight.frame) * 146, knight.action * 241, 146, 241,
                                      knight.draw_x, knight.draw_y, 146 * 1.1, 241 * 1.1)
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
            Run: {left_down: Run, left_up: Run, right_down: Run, right_up: Run,
                  up_down: Run, up_up: Run, down_down: Run, down_up: Run,
                  e_down: Run, dash_time_out: Run, r_down: Run, angel_time_out: Run, w_down: Run,
                  heal_time_out: Run}
        }

    def start(self):
        self.cur_state.entry(self.knight, ('START', 0))

    def update(self):
        self.cur_state.do(self.knight)

    def draw(self):
        self.cur_state.draw(self.knight)

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
        self.update_bounding_box()

    def draw(self):
        self.state_machine.draw()
        if play_mode.bb_toggle:
            for box in self.bounding_box_list:
                draw_rectangle(*box)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))  # 입력 이벤트

    def init_knight_var(self):
        self.knight_image = load_image("Object\\KnightSprite.png")
        self.draw_x, self.draw_y = 250, 400
        self.layer_y = self.draw_y - 80
        self.Dir = 0

        self.frame = 0
        self.time_per_action = 0.3
        self.action_per_time = 1.0 / self.time_per_action
        self.frames_per_action = 3

        self.walk_km_per_hour = 52.0  # Km / Hour
        self.walk_meter_per_minute = (self.walk_km_per_hour * 1000.0 / 60.0)
        self.walk_meter_per_second = (self.walk_meter_per_minute / 60.0)
        self.walk_pixel_per_second = (self.walk_meter_per_second * play_mode.pixel_per_meter)

        self.HP = 100
        self.HP_decrease = 0.03  # 0.03
        self.Coin, self.Count = 0, 0
        self.live, self.dash_mode, self.angel_mode, self.sword_mode, self.heal_mode = True, False, False, False, False
        self.dash_cooltime, self.angel_cooltime = False, False
        self.bounding_box_list = []
        self.action = 0

    def init_warnning_var(self):  # 105 x 25
        self.warning_image = load_image("UI\\warning_sign.png")
        self.warning_frame = 0
        self.warning_time_per_action = 0.6
        self.warning_action_per_time = 1.0 / self.warning_time_per_action
        self.warning_frames_per_action = 10

    def init_sweat_var(self):  # 66 x 60
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

    def get_bounding_box(self):
        return self.bounding_box_list

    def update_hp(self):
        if self.HP <= 0:
            if self.live:
                self.live = False
                self.HP, self.HP_decrease, self.Dir = 0, 0, 0
                game_framework.push_mode(over_mode)

            if play_mode.scroll_pixel_per_second < 30:
                play_mode.scroll_meter_per_second = 0
                play_mode.scroll_pixel_per_second = 0
            else:
                play_mode.scroll_pixel_per_second -= play_mode.scroll_pixel_per_second / 500

            return
        self.HP -= self.HP_decrease  # 0.25

    def update_bounding_box(self):
        self.bounding_box_list = [
            (self.draw_x - 50, self.draw_y - 80, self.draw_x - 10, self.draw_y - 10)
        ]

    def dash_skill(self):
        global dash_start_time, dash
        if self.dash_mode == True: return
        self.action = 1
        self.dash_mode = True
        self.dash_cooltime = True
        dash = KnightDash(self)
        game_world.add_object(dash, 1)
        game_world.add_collision_pair('Dash:Crown', dash, None)
        game_world.add_collision_pair('Dash:Girl', dash, None)
        game_world.add_collision_pair('Dash:Skull', dash, None)
        dash_start_time = time.time()

    def angel_skill(self):
        global angel_start_time, angel
        if self.angel_mode == True: return
        self.action = 1
        self.angel_mode = True
        self.angel_cooltime = True
        angel = KnightAngel(self)
        game_world.add_object(angel, 2)
        game_world.add_collision_pair('Angel:Crown', angel, None)
        game_world.add_collision_pair('Angel:Girl', angel, None)
        game_world.add_collision_pair('Angel:Skull', angel, None)
        angel_start_time = time.time()

    def sword_skill(self):
        self.action = 1
        self.sword_mode = True
        sword = KnightSword(self)
        game_world.add_object(sword, 1)
        game_world.add_collision_pair('Sword:Crown', sword, None)
        game_world.add_collision_pair('Sword:Girl', sword, None)
        game_world.add_collision_pair('Sword:Skull', sword, None)

    def handle_collision(self, group, other):
        if group == 'Knight:Portion':
            global heal_start_time, healing
            self.HP += random.randint(10, 25)
            if self.HP > 100: self.HP = 100
            heal_start_time = time.time()
            if not self.heal_mode:
                self.heal_mode = True
                healing = KnightHealing(self)
                game_world.add_object(healing, 1)

        if group == 'Knight:Coin':
            self.Coin += random.randint(100, 500)

        if group == 'Knight:Trap' and other.is_valid:
            if self.angel_cooltime or self.dash_cooltime: return
            self.HP -= 10
            if self.HP < 0: return
            attacked = Attacked(self)
            game_world.add_object(attacked, 2)

        if group == 'Knight:Crown' and other.is_valid:
            if self.angel_cooltime or self.dash_cooltime: return
            self.HP -= 15
            attacked = Attacked(self)
            game_world.add_object(attacked, 2)

        if group == 'Knight:Girl' and other.is_valid:
            if self.angel_cooltime or self.dash_cooltime: return
            self.HP -= 20
            attacked = Attacked(self)
            game_world.add_object(attacked, 2)

        if group == 'Knight:Skull' and other.is_valid:
            if self.angel_cooltime or self.dash_cooltime: return
            self.HP -= 25
            attacked = Attacked(self)
            game_world.add_object(attacked, 2)
