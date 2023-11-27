from pico2d import load_image
import game_framework
import game_world
import play_mode


class Attacked:
    image = None

    def __init__(self, knight):
        if self.image == None:
            self.image = load_image("Skill\\attacked_sprite.png")
        self.knight = knight
        self.draw_x, self.draw_y = self.knight.draw_x + 10, self.knight.draw_y + 10
        self.layer_y = self.draw_y - (189 / 2)
        self.frame = 0
        self.time_per_action = 0.38  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 4  # 액션 당 필요한 프레임 수

    def update(self):
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 4
        if int(self.frame) == 3: self.remove()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 300, 0, 164, 189, self.draw_x, self.draw_y, 164, 189)

    def remove(self):
        game_world.remove_object(self)
        pass
