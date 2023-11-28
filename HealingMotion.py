from pico2d import load_image, draw_rectangle
import game_framework
import game_world
import play_mode


class KnightHealing:
    image = None

    def __init__(self, knight):
        if self.image == None:
            self.image = load_image("Skill\\heal_sprite.png")
        self.knight = knight
        self.draw_x, self.draw_y = self.knight.draw_x, self.knight.draw_y
        self.layer_y = self.knight.draw_y - 81
        self.frame = 0
        self.time_per_action = 0.35  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 5  # 액션 당 필요한 프레임 수

    def update(self):
        # if int(self.frame) == 4: self.remove()
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 5
        self.draw_x, self.draw_y = self.knight.draw_x + 25, self.knight.draw_y + 50

    def draw(self):
        self.image.clip_draw(int(self.frame) * 93, 0, 93, 79, self.draw_x, self.draw_y, 93, 79)

    def remove(self):
        game_world.remove_object(self)
        pass