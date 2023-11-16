import random
from pico2d import load_image, get_time
import game_framework
import play_mode

class HPportion:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image("Object\\portion_object.png")
        self.draw_x, self.draw_y = 1280 + 75, random.randint(50, 630)
        pass

    def update(self):
        self.draw_x -= play_mode.run_speed_pixel_per_second * game_framework.frame_time
        if self.draw_x < -75:
            self.draw_x, self.draw_y = 1280 + 75, random.randint(50, 630)
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 75, 91, self.draw_x, self.draw_y, 75, 91)
        pass

    def handle_event(self, event):
        pass


