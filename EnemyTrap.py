import random
import time

from pico2d import load_image, get_time, draw_rectangle
import game_framework
import game_world
import play_mode


def trap_add():
    if game_framework.current_time - play_mode.trap_start_time >= random.uniform(1.0, 5.0):
        trap = EnemyTrap()
        game_world.add_object(trap, 0)
        play_mode.trap_start_time = time.time()


class EnemyTrap:
    image = None

    def __init__(self):
        if self.image == None:
            self.image = load_image("Object\\enemy_trap.png")
        self.draw_x, self.draw_y = 1280 + 158, random.randint(100, 570)
        self.bounding_box_list = []
        # self.layer_y = self.draw_y - (204 / 2)

    def update(self):
        if self.draw_x < -75:
            game_world.remove_object(self)
        self.draw_x -= play_mode.scroll_pixel_per_second * game_framework.frame_time
        self.update_bounding_box()

    def draw(self):
        self.image.clip_draw(0, 0, 158, 204, self.draw_x, self.draw_y, 158, 204)
        for box in self.bounding_box_list:
            draw_rectangle(*box)

    def handle_event(self, event):
        pass

    def get_bounding_box(self):
        return self.bounding_box_list

    def update_bounding_box(self):
        self.bounding_box_list = [
            (self.draw_x - 45, self.draw_y - 90.0, self.draw_x - 10, self.draw_y - 10),
            (self.draw_x - 20, self.draw_y - 35.0, self.draw_x + 15, self.draw_y + 45),
            (self.draw_x + 10, self.draw_y + 20.0, self.draw_x + 45, self.draw_y + 100)
        ]
