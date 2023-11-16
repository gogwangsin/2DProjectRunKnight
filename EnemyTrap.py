import random
from pico2d import load_image, get_time
import game_framework
import play_mode

class EnemyTrap:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image("Object\\enemy_trap.png")
        self.draw_x, self.draw_y = 1280 + 158, random.randint(100, 570)
        pass

    def update(self):
        self.draw_x -= play_mode.run_speed_pixel_per_second * game_framework.frame_time
        if self.draw_x < -75:
            self.draw_x, self.draw_y = 1280 + 158, random.randint(100, 570)
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 158, 204, self.draw_x, self.draw_y, 158, 204)
        pass

    def handle_event(self, event):
        pass


