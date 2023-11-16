import random
import time

from pico2d import load_image
import game_framework
import game_world
import play_mode


class KnightDash:
    image = None

    def __init__(self, knight):
        if self.image == None:
            self.image = load_image("Skill\\skill_dash.png")
        self.knight = knight

        self.draw_x, self.draw_y = self.knight.draw_x, self.knight.draw_y
        self.frame = 0
        self.time_per_action = 0.3  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 3  # 액션 당 필요한 프레임 수

    def update(self):
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 3
        self.draw_x, self.draw_y = self.knight.draw_x - 170, self.knight.draw_y - 35


    def draw(self):
        self.image.clip_draw(int(self.frame) * 300, 0, 300, 187, self.draw_x, self.draw_y, 300 * 0.9, 187 * 0.9)

    def remove(self):
        print('이벤트 발생')
        self.knight.dash_mode = False
        game_world.remove_object(self)
        pass
