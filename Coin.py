import math
import random
import time
from pico2d import load_image, draw_rectangle, load_wav
import game_framework
import game_world
import play_mode
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector


def coin_add():
    if game_framework.current_time - play_mode.coin_start_time >= random.uniform(1.0, 5.0):
        coin = Coin()
        game_world.add_object(coin, 1)
        game_world.add_collision_pair('Knight:Coin', None, coin)
        play_mode.coin_start_time = time.time()


class Coin:
    image = None
    sound = None

    def __init__(self):
        if self.image == None:
            self.image = load_image("Object\\coin_object.png")
        if not Coin.sound:
            Coin.sound = load_wav('Sound\\getCoinSound.mp3')
            Coin.sound.set_volume(15)

        self.draw_x, self.draw_y = 1280 + 81, random.randint(50, 630)
        self.layer_y = self.draw_y - 30
        self.frame = 0
        self.time_per_action = 0.4  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 5  # 액션 당 필요한 프레임 수
        self.bounding_box_list = []
        self.build_behavior_tree()
        self.radian_dir = 0.0

    def update(self):
        if self.draw_x < -81:
            game_world.remove_object(self)
            return
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 5
        self.bt.run()
        self.layer_y = self.draw_y - 30
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
            Coin.sound.play()
            game_world.remove_object(self)

    def update_bounding_box(self):
        self.bounding_box_list = [
            # (self.draw_x - 30.0, self.draw_y - 37.5, self.draw_x + 30.0, self.draw_y + 37.5),
            (self.draw_x - 25.0, self.draw_y - 30.0, self.draw_x + 25.0, self.draw_y + 30.0),
        ]

    def distance_less_than(self, x1, y1, x2, y2, r):
        # 거리가 r보다 작으면 - 두 개의 점 (x1,y1) (x2,y2)
        # r은 픽셀 단위이니 거리 단위 m로 변경
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < (play_mode.pixel_per_meter * r) ** 2

    def x_range_less_than(self):
        if self.draw_x >= 25:
            return True
        else:
            return False

    def move_slightly_to(self, tx, ty):
        self.radian_dir = math.atan2(ty - self.draw_y, tx - self.draw_x)
        self.draw_x += (play_mode.scroll_pixel_per_second * 1.5) * math.cos(self.radian_dir) * game_framework.frame_time
        self.draw_y += (play_mode.scroll_pixel_per_second / 3) * math.sin(self.radian_dir) * game_framework.frame_time

    def move(self):
        # A2: action2 node
        self.draw_x -= play_mode.scroll_pixel_per_second * game_framework.frame_time
        return BehaviorTree.SUCCESS

    def is_knight_nearby(self, r):
        # C1: condition1 node
        if self.distance_less_than(play_mode.knight.draw_x, play_mode.knight.draw_y, self.draw_x, self.draw_y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def move_to_knight(self, r=0.5):
        # A1: action1 node
        self.move_slightly_to(play_mode.knight.draw_x, play_mode.knight.draw_y)
        if self.x_range_less_than():
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def build_behavior_tree(self):
        C1 = Condition('용사가 근처에 있는가?', self.is_knight_nearby, 6)
        A1 = Action('용사로 이동', self.move_to_knight)
        A2 = Action('화면 따라서 이동', self.move)

        SEQ_chase_knight = Sequence('코인이 용사 향해 이끌림', C1, A1)
        SEQ_move = Sequence('화면에 따라서 이동', A2)
        root = Selector('이끌림 혹은 이동', SEQ_chase_knight, SEQ_move)
        self.bt = BehaviorTree(root)
