from pico2d import load_image
import game_framework
import game_world
import play_mode


class KnightAngel:
    halo_image = None
    angel_image = None
    def __init__(self, knight):
        if self.halo_image == None or self.angel_image == None:
            self.halo_image = load_image("Skill\\skill_angel_halo.png")
            self.angel_image = load_image("Skill\\skill_angel.png")
        self.knight = knight

        self.draw_x, self.draw_y = 1280 // 2, 800 // 2
        # self.layer_y = self.draw_y - (187 * 0.9 / 2)
        self.frame = 0
        self.time_per_action = 0.3  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 7  # 액션 당 필요한 프레임 수

        self.dash_speed_ratio = 3.0
        play_mode.scroll_pixel_per_second *= self.dash_speed_ratio

    def update(self):
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 7
        # self.draw_x, self.draw_y = self.knight.draw_x - 170, self.knight.draw_y - 35
        # self.layer_y = self.draw_y - (187 * 0.9 / 2)


    def draw(self):
        self.halo_image.clip_draw(int(self.frame) * 1020, 0, 1020, 633, self.draw_x, self.draw_y, 1020, 633)
        self.angel_image.clip_draw(0, 0, 308, 246, self.draw_x, self.draw_y, 308, 246)

    def remove(self):
        play_mode.scroll_pixel_per_second /= self.dash_speed_ratio
        self.knight.angel_mode = False
        game_world.remove_object(self)
        pass
