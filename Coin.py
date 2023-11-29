import random
import time
from pico2d import load_image, draw_rectangle
import game_framework
import game_world
import play_mode
from behavior_tree import BehaviorTree, Action, Sequence


def coin_add():
    if game_framework.current_time - play_mode.coin_start_time >= random.uniform(1.0, 5.0):
        coin = Coin()
        game_world.add_object(coin, 1)
        game_world.add_collision_pair('Knight:Coin', None, coin)
        play_mode.coin_start_time = time.time()


class Coin:
    image = None

    def __init__(self):
        if self.image == None:
            self.image = load_image("Object\\coin_object.png")
        self.draw_x, self.draw_y = 1280 + 81, random.randint(50, 630)
        self.layer_y = self.draw_y - 37.5
        self.frame = 0
        self.time_per_action = 0.4  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 5  # 액션 당 필요한 프레임 수
        self.bounding_box_list = []
        self.build_behavior_tree()

    def update(self):
        if self.draw_x < -81:
            game_world.remove_object(self)
            return
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 5
        self.bt.run()
        self.update_bounding_box()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 81, 0, 81, 81, self.draw_x, self.draw_y, 81, 81)
        if play_mode.bb_toggle:
            for box in self.bounding_box_list:
                draw_rectangle(*box)

    def handle_event(self, event):
        pass

    def get_bounding_box(self):
        return self.bounding_box_list

    def handle_collision(self, group, other):
        if group == 'Knight:Coin':
            game_world.remove_object(self)

    def update_bounding_box(self):
        self.bounding_box_list = [
            (self.draw_x - 30.0, self.draw_y - 37.5, self.draw_x + 30.0, self.draw_y + 37.5)
        ]

    def move(self):
        self.draw_x -= play_mode.scroll_pixel_per_second * game_framework.frame_time
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        A1 = Action('스크롤에 따라 이동', self.move)
        root = Sequence('용사에게 끌림 혹은 이동', A1)
        self.bt = BehaviorTree(root)
        pass