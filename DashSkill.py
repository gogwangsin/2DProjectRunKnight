from pico2d import load_image, draw_rectangle
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
        self.layer_y = self.draw_y - (187 * 0.9 / 2)
        self.frame = 0
        self.time_per_action = 0.3  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 3  # 액션 당 필요한 프레임 수

        self.dash_speed_ratio = 1.8
        play_mode.scroll_pixel_per_second *= self.dash_speed_ratio
        self.bounding_box_list = []

    def update(self):
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 3
        self.draw_x, self.draw_y = self.knight.draw_x - 170, self.knight.draw_y - 35
        self.layer_y = self.draw_y - (187 * 0.9 / 2)
        self.update_bounding_box()


    def draw(self):
        self.image.clip_draw(int(self.frame) * 300, 0, 300, 187, self.draw_x, self.draw_y, 300 * 0.9, 187 * 0.9)
        if play_mode.bb_toggle:
            for box in self.bounding_box_list:
                draw_rectangle(*box)

    def remove(self):
        play_mode.scroll_pixel_per_second /= self.dash_speed_ratio
        self.knight.dash_mode = False
        self.knight.action = 0
        game_world.remove_object(self)
        pass

    def get_bounding_box(self):
        return self.bounding_box_list

    def update_bounding_box(self):
        self.bounding_box_list = [
            (self.knight.draw_x - 70, self.knight.draw_y - 85, self.knight.draw_x + 10, self.knight.draw_y + 70)
        ]

    def handle_collision(self, group, other):
        pass