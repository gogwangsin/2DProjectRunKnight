import random
import time
from pico2d import load_image, draw_rectangle
import game_framework
import game_world
import play_mode
from MonsterAttackedEffect import MonsterAttacked
from MonsterAttackedEffect2 import MonsterAttacked2


def enemy_crown_add():
    if game_framework.current_time - play_mode.crown_start_time >= random.uniform(1.0, 5.0):
        crown = EnemyCrown()
        game_world.add_object(crown, 1)
        game_world.add_collision_pair('Knight:Crown', None, crown)
        game_world.add_collision_pair('Dash:Crown', None, crown)
        game_world.add_collision_pair('Sword:Crown', None, crown)
        play_mode.crown_start_time = time.time()


class Run:

    @staticmethod
    def entry(crown, event):
        crown.Dir = -1

    @staticmethod
    def exit(crown, event):
        pass

    @staticmethod  # 함수를 그룹핑 하는 역할
    def do(crown):
        if crown.draw_x < -515:
            game_world.remove_object(crown)

        crown.frame = (crown.frame + crown.frames_per_action * crown.action_per_time *
                       game_framework.frame_time) % 4
        crown.draw_x += (crown.Dir * (play_mode.scroll_pixel_per_second + crown.walk_pixel_per_second)
                         * game_framework.frame_time)

    @staticmethod
    def draw(crown):  # frame, action, 사진 가로,세로, x,y, 크기 비율
        crown.image.clip_draw(int(crown.frame) * 515, 0, 515, 452,
                              crown.draw_x, crown.draw_y, 515 * 0.25, 452 * 0.25)


# ==============================================================================

class StateMachine:
    def __init__(self, object):
        self.object = object
        self.cur_state = Run
        # 상태 전환 테이블

    def start(self):
        self.cur_state.entry(self.object, ('START', 0))
        # entry action : event:( key == START, value == 0 )으로 전달

    def update(self):
        self.cur_state.do(self.object)
        pass

    def draw(self):
        self.cur_state.draw(self.object)
        pass

    def handle_event(self, event):
        pass
        # for check_event, next_state in self.transitions[self.cur_state].items():
        #     if check_event(event):
        #         self.cur_state.exit(self.knight, event)
        #         self.cur_state = next_state
        #         self.cur_state.entry(self.knight, event)
        #         return True
        # return False


# ==============================================================================

class EnemyCrown:
    image = None

    def __init__(self):
        self.init_crown_var()
        self.init_state_machine()

    def update(self):
        self.state_machine.update()
        self.update_bounding_box()

    def draw(self):
        self.state_machine.draw()
        if play_mode.bb_toggle:
            for box in self.bounding_box_list:
                draw_rectangle(*box)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))  # 입력 이벤트

    def init_crown_var(self):
        if self.image == None:
            self.image = load_image("Object\\enemy_crown_axe.png")

        self.draw_x, self.draw_y = 1280 + 515, random.randint(70, 650)
        self.layer_y = self.draw_y - 55.0 # <- bb랑 비슷함
        # 화면 크기_x+ 그릴 크기_x(밖에 그리기), y범위 70~650

        self.frame = random.randint(0, 3)
        self.time_per_action = 0.8
        self.action_per_time = 1.0 / self.time_per_action
        self.frames_per_action = 4

        self.walk_km_per_hour = random.randint(10, 45)
        self.walk_meter_per_minute = (self.walk_km_per_hour * 1000.0 / 60.0)
        self.walk_meter_per_second = (self.walk_meter_per_minute / 60.0)
        self.walk_pixel_per_second = (self.walk_meter_per_second * play_mode.pixel_per_meter)

        self.Dir = 0
        self.bounding_box_list = []
        self.is_valid = True

    def init_state_machine(self):
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def get_bounding_box(self):
        return self.bounding_box_list

    def update_bounding_box(self):
        self.bounding_box_list = [
            (self.draw_x - 25.5, self.draw_y - 55.0, self.draw_x + 55, self.draw_y + 25)
        ]

    def handle_collision(self, group, other):
        if self.is_valid and group == 'Knight:Crown':
            self.is_valid = False
        elif self.is_valid and group == 'Dash:Crown':  # 처음 맞을 땐 -> 뒤로감 -> 두번째는 디짐
            attacked = MonsterAttacked(self)
            game_world.add_object(attacked, 2)
            self.is_valid = False
            game_world.remove_object(self)
        if group == 'Sword:Crown':
            if self.is_valid:
                attacked = MonsterAttacked2(self)
                game_world.add_object(attacked, 2)
                self.is_valid = False
            elif not self.is_valid:
                attacked = MonsterAttacked2(self)
                game_world.add_object(attacked, 2)
                game_world.remove_object(self)
