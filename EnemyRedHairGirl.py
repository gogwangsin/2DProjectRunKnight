import random
import time
from pico2d import load_image, draw_rectangle
import game_framework
import game_world
import play_mode
from MonsterAttackedEffect import MonsterAttacked
from MonsterAttackedEffect2 import MonsterAttacked2
from MonsterAttackedEffect3 import MonsterAttacked3
from MonsterAttackedEffect4 import MonsterAttacked4


def enemy_girl_add():
    if game_framework.current_time - play_mode.girl_start_time >= random.uniform(1.0, 5.0):
        girl = EnemyRedGirl()
        game_world.add_object(girl, 1)
        game_world.add_collision_pair('Knight:Girl', None, girl)
        game_world.add_collision_pair('Dash:Girl', None, girl)
        game_world.add_collision_pair('Sword:Girl', None, girl)
        game_world.add_collision_pair('Angel:Girl', None, girl)
        play_mode.girl_start_time = time.time()


class Run:

    @staticmethod
    def entry(girl, event):
        girl.Dir = -1

    @staticmethod
    def exit(girl, event):
        pass

    @staticmethod  # 함수를 그룹핑 하는 역할
    def do(girl):
        if girl.draw_x < -132:
            game_world.remove_object(girl)

        girl.frame = (girl.frame + girl.frames_per_action * girl.action_per_time *
                      game_framework.frame_time) % 8
        girl.draw_x += (girl.Dir * (play_mode.scroll_pixel_per_second + girl.walk_pixel_per_second)
                        * game_framework.frame_time)

    @staticmethod
    def draw(girl):  # frame, action, 사진 가로,세로, x,y, 크기 비율
        girl.image.clip_draw(int(girl.frame) * 132, 0, 132, 133, girl.draw_x, girl.draw_y, 132 * 1.1, 133 * 1.1)


# ==============================================================================

class StateMachine:
    def __init__(self, object):
        self.object = object
        self.cur_state = Run

    def start(self):
        self.cur_state.entry(self.object, ('START', 0))

    def update(self):
        self.cur_state.do(self.object)
        pass

    def draw(self):
        self.cur_state.draw(self.object)
        pass

    def handle_event(self, event):
        pass

# ==============================================================================
class EnemyRedGirl:
    image = None

    def __init__(self):
        self.init_girl_var()
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

    def init_girl_var(self):
        if self.image == None:
            self.image = load_image("Object\\enemy_red_hair_girl.png")
        # 132 / 133
        self.draw_x, self.draw_y = 1280 + 132, random.randint(70, 680)
        self.layer_y = self.draw_y - 65.0

        self.frame = random.randint(0, 7)
        self.time_per_action = 1.5
        self.action_per_time = 1.0 / self.time_per_action
        self.frames_per_action = 8

        self.walk_km_per_hour = random.randint(10, 35)
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
            (self.draw_x + 10, self.draw_y - 65.0, self.draw_x + 35, self.draw_y + 5)
        ]

    def handle_collision(self, group, other):
        if self.is_valid and group == 'Knight:Girl':
            self.is_valid = False

        if self.is_valid and group == 'Dash:Girl':  # 처음 맞을 땐 -> 뒤로감 -> 두번째는 디짐
            attacked = MonsterAttacked3(self)
            game_world.add_object(attacked, 2)
            self.is_valid = False
            game_world.remove_object(self)

        if group == 'Sword:Girl':
            if self.is_valid:
                attacked = MonsterAttacked2(self)
                game_world.add_object(attacked, 2)
                self.is_valid = False
            elif not self.is_valid:
                attacked = MonsterAttacked2(self)
                game_world.add_object(attacked, 2)
                game_world.remove_object(self)

        if self.is_valid and group == 'Angel:Girl':  # 처음 맞을 땐 -> 뒤로감 -> 두번째는 디짐
            attacked = MonsterAttacked4(self)
            game_world.add_object(attacked, 2)
            self.is_valid = False
            game_world.remove_object(self)