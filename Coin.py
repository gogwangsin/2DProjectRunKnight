import random
from pico2d import load_image, get_time
import game_framework
import play_mode

class Coin:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image("Object\\coin_object.png")
        self.draw_x, self.draw_y = 1280 + 81, 50 #random.randint(50, 630)
        self.frame = 0
        self.time_per_action = 0.4  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 5  # 액션 당 필요한 프레임 수


    def update(self):
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 5
        self.draw_x -= play_mode.run_speed_pixel_per_second * game_framework.frame_time
        if self.draw_x < -81:
            self.draw_x, self.draw_y = 1280 + 81, random.randint(50, 630)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 81, 0, 81, 81, self.draw_x, self.draw_y, 81, 81)

    def handle_event(self, event):
        pass


