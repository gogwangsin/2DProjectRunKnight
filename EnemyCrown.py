import random
import time

from pico2d import load_image, get_time, draw_rectangle
import game_framework
import game_world
import play_mode


def enemy_crown_add():
    if game_framework.current_time - play_mode.crown_start_time >= random.uniform(1.0, 5.0):
        crown = EnemyCrown()
        game_world.add_object(crown, 1)
        game_world.add_collision_pair('Knight:Crown', None, crown)
        game_world.add_collision_pair('Dash:Crown', None, crown)
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
        crown.image.clip_draw(int(crown.frame) * 515, crown.action * 452, 515, 452,
                              crown.draw_x, crown.draw_y, 515 * 0.25, 452 * 0.25)


# ==============================================================================
class EnemyCrown:
    image = None

    def __init__(self):
        self.init_crown_var()
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

    def init_crown_var(self):
        if self.image == None:
            self.image = load_image("Object\\enemy_crown_axe.png")

        self.draw_x, self.draw_y = 1280 + 515, random.randint(70, 650)
        self.layer_y = self.draw_y - 55.0
        # 화면 크기_x+ 그릴 크기_x(밖에 그리기), y범위 70~650

        self.frame = random.randint(0, 3)
        self.time_per_action = 0.8
        self.action_per_time = 1.0 / self.time_per_action
        self.frames_per_action = 4

        self.walk_km_per_hour = random.randint(10, 45)
        self.walk_meter_per_minute = (self.walk_km_per_hour * 1000.0 / 60.0)
        self.walk_meter_per_second = (self.walk_meter_per_minute / 60.0)
        self.walk_pixel_per_second = (self.walk_meter_per_second * play_mode.pixel_per_meter)

        self.HP = 300
        self.Dir = 0
        self.action = 0  # 0 고정
        self.bounding_box_list = []
        self.is_valid = True

    def init_state_machine(self):
        from enemy_state_machine import StateMachine
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def get_current_hp(self):
        return self.HP

    def update_hp(self):
        pass

    def get_bounding_box(self):
        return self.bounding_box_list

    def update_bounding_box(self):
        self.bounding_box_list = [
            (self.draw_x - 25.5, self.draw_y - 55.0, self.draw_x + 55, self.draw_y + 25)
        ]

    def handle_collision(self, group, other):
        if self.is_valid and group == 'Knight:Crown':
            self.walk_pixel_per_second = 0
            self.is_valid = False
        if group == 'Dash:Crown':
            game_world.remove_object(self)