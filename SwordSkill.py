from pico2d import load_image, draw_rectangle
import game_framework
import game_world
import play_mode


class KnightSword:
    image = None

    def __init__(self, knight):
        if self.image == None:
            self.image = load_image("Skill\\sword_attack.png")
        self.knight = knight

        self.draw_x, self.draw_y = self.knight.draw_x, self.knight.draw_y
        self.layer_y = self.draw_y - (187 * 0.9 / 2)
        self.frame = 0
        self.time_per_action = 0.35  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 4  # 액션 당 필요한 프레임 수

        self.bounding_box_list = []

    def update(self):
        if int(self.frame) == 3: self.remove()
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 4
        self.draw_x, self.draw_y = self.knight.draw_x + 30, self.knight.draw_y - 20
        self.layer_y = self.draw_y - (486 * 0.9 / 2)
        self.update_bounding_box()


    def draw(self):
        self.image.clip_draw(int(self.frame) * 581, 0, 581, 126, self.draw_x, self.draw_y, 581 * 0.45, 126 * 0.45)
        if play_mode.bb_toggle:
            for box in self.bounding_box_list:
                draw_rectangle(*box)

    def remove(self):
        self.knight.action = 0
        game_world.remove_object(self)
        pass

    def get_bounding_box(self):
        return self.bounding_box_list

    def update_bounding_box(self):
        self.bounding_box_list = [
            (self.knight.draw_x - 10, self.draw_y - 15, self.draw_x + 100, self.draw_y + 25)
        ]

    def handle_collision(self, group, other):
        pass