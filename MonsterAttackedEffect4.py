from pico2d import load_image
import game_framework
import game_world


# 엔젤 타격 :153x154 - 17개
class MonsterAttacked4:
    image = None

    def __init__(self, monster):
        if self.image == None:
            self.image = load_image("Skill\\angel_attack_sprite2.png")
        self.mon = monster
        self.draw_x, self.draw_y = self.mon.draw_x + 10, self.mon.draw_y
        self.layer_y = self.draw_y - (154 / 2)
        self.frame = 0
        self.time_per_action = 0.45  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 17  # 액션 당 필요한 프레임 수

    def update(self):
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 17
        if int(self.frame) == 16: self.remove()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 153, 0, 153, 154, self.draw_x, self.draw_y, 153 * 1.3, 154 * 1.3)

    def remove(self):
        game_world.remove_object(self)
