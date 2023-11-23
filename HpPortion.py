import random
import time

from pico2d import load_image, get_time, draw_rectangle
import game_framework
import game_world
import play_mode

def hp_portion_add():
    if game_framework.current_time - play_mode.hp_start_time >= random.uniform(1.0, 5.0):
        portion = HPportion()
        game_world.add_object(portion, 1)
        game_world.add_collision_pair('Knight:Portion', None, portion)
        play_mode.hp_start_time = time.time()

class HPportion:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image("Object\\portion_object.png")
        self.draw_x, self.draw_y = 1280 + 75, random.randint(50, 630) # 100
        self.layer_y = self.draw_y - 40.0
        pass

    def update(self):
        if self.draw_x < -75:
            game_world.remove_object(self)
        self.draw_x -= play_mode.scroll_pixel_per_second * game_framework.frame_time



    def draw(self):
        self.image.clip_draw(0, 0, 75, 91, self.draw_x, self.draw_y, 75, 91)
        draw_rectangle(*self.get_bounding_box())
        pass

    def handle_event(self, event):
        pass

    def get_bounding_box(self):
        return self.draw_x - 37.5, self.draw_y - 40.0, self.draw_x + 37.5, self.draw_y + 40

    def handle_collision(self, group, other):
        if group == 'Knight:Portion':
            print('포션 획득')
            game_world.remove_object(self)
        pass