import random
import time
from pico2d import load_image, draw_rectangle
import game_framework
import game_world
import play_mode
from MonsterAttackedEffect import MonsterAttacked
from MonsterAttackedEffect2 import MonsterAttacked2
from MonsterAttackedEffect3 import MonsterAttacked3


def enemy_skull_add():
    if game_framework.current_time - play_mode.skull_start_time >= random.uniform(3.0, 7.0):
        skull = EnemySkull()
        game_world.add_object(skull, 1)
        game_world.add_collision_pair('Knight:Skull', None, skull)
        game_world.add_collision_pair('Dash:Skull', None, skull)
        game_world.add_collision_pair('Sword:Skull', None, skull)
        play_mode.skull_start_time = time.time()


class Run:

    @staticmethod
    def entry(skull, event):
        skull.Dir = -1

    @staticmethod
    def exit(skull, event):
        pass

    @staticmethod  # 함수를 그룹핑 하는 역할
    def do(skull):
        if skull.draw_x < -396:
            game_world.remove_object(skull)

        skull.frame = (skull.frame + skull.frames_per_action * skull.action_per_time *
                       game_framework.frame_time) % 3
        skull.draw_x += (skull.Dir * (play_mode.scroll_pixel_per_second + skull.walk_pixel_per_second)
                         * game_framework.frame_time)

    @staticmethod
    def draw(skull):  # frame, action, 사진 가로,세로, x,y, 크기 비율
        skull.image.clip_draw(int(skull.frame) * 396, 0, 396, 438, skull.draw_x, skull.draw_y, 396 * 0.4, 438 * 0.4)


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
class EnemySkull:
    image = None

    def __init__(self):
        self.init_skull_var()
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

    def init_skull_var(self):
        if self.image == None:
            self.image = load_image("Object\\enemy_horse_skull.png")
        #  396 438
        self.draw_x, self.draw_y = 1280 + 396, random.randint(90, 670)
        self.layer_y = self.draw_y - 55.0

        self.frame = random.randint(0, 3)
        self.time_per_action = 0.45
        self.action_per_time = 1.0 / self.time_per_action
        self.frames_per_action = 3

        self.walk_km_per_hour = random.randint(10, 15)
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
            (self.draw_x - 25, self.draw_y - 75.0, self.draw_x + 55, self.draw_y + 5),
            (self.draw_x, self.draw_y + 5.0, self.draw_x + 35, self.draw_y + 35)
        ]

    def handle_collision(self, group, other):
        if self.is_valid and group == 'Knight:Skull':
            self.is_valid = False
        elif self.is_valid and group == 'Dash:Skull':  # 처음 맞을 땐 -> 뒤로감 -> 두번째는 디
            attacked = MonsterAttacked3(self)
            game_world.add_object(attacked, 2)
            self.is_valid = False
            game_world.remove_object(self)
        if group == 'Sword:Skull':
            if self.is_valid:
                attacked = MonsterAttacked2(self)
                game_world.add_object(attacked, 2)
                self.is_valid = False
            elif not self.is_valid:
                attacked = MonsterAttacked2(self)
                game_world.add_object(attacked, 2)
                game_world.remove_object(self)
