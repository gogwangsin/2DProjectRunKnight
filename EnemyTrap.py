import random
import time

from pico2d import load_image, get_time
import game_framework
import game_world
import play_mode


def trap_add():
    global trap

    if game_framework.current_time - play_mode.trap_start_time >= 1:
        trap = EnemyTrap()
        game_world.add_object(trap, 1)
        play_mode.trap_start_time = time.time()

class EnemyTrap:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image("Object\\enemy_trap.png")
        self.draw_x, self.draw_y = 1280 + 158, random.randint(100, 570)

    def update(self):
        self.draw_x -= play_mode.scroll_pixel_per_second * game_framework.frame_time
        if self.draw_x < -75:
            # print('장애물 삭제')
            game_world.remove_object(self)
            # self.draw_x, self.draw_y = 1280 + 158, random.randint(100, 570)

    def draw(self):
        self.image.clip_draw(0, 0, 158, 204, self.draw_x, self.draw_y, 158, 204)
        pass

    def handle_event(self, event):
        pass


