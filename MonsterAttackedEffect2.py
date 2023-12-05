from pico2d import load_image
import game_framework
import game_world


# 검기 타격
class MonsterAttacked2:
    image = None

    def __init__(self, monster):
        if self.image == None:
            self.image = load_image("Skill\\attack_sprite.png")
        self.mon = monster
        self.draw_x, self.draw_y = self.mon.draw_x + 10, self.mon.draw_y
        self.layer_y = self.draw_y - (203 / 2)
        self.frame = 1
        self.time_per_action = 0.4  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 7  # 액션 당 필요한 프레임 수

    def update(self):
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 7
        if int(self.frame) == 6: self.remove()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 374, 0, 374, 203, self.draw_x, self.draw_y, 374 * 0.95, 203 * 0.95)

    def remove(self):
        game_world.remove_object(self)
