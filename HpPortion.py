import random
import time

from pico2d import load_image, get_time
import game_framework
import game_world
import play_mode

def hp_portion_add():
    global portion

    if game_framework.current_time - play_mode.hp_start_time >= 1:
        print('3초 마다 생성')
        portion = HPportion()
        game_world.add_object(portion, 1)
        play_mode.hp_start_time = time.time()

class HPportion:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image("Object\\portion_object.png")
        self.draw_x, self.draw_y = 1280 + 75, random.randint(50, 630)
        pass

    def update(self):
        self.draw_x -= play_mode.scroll_pixel_per_second * game_framework.frame_time
        if self.draw_x < -75:
            print('포션 삭제')
            game_world.remove_object(self)
            # self.draw_x, self.draw_y = 1280 + 75, random.randint(50, 630)


    def draw(self):
        self.image.clip_draw(0, 0, 75, 91, self.draw_x, self.draw_y, 75, 91)
        pass

    def handle_event(self, event):
        pass


