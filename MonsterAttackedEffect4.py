from pico2d import load_image
import game_framework
import game_world


# 엔젤 타격 :512x512 - 31개
class MonsterAttacked4:
    image = None

    def __init__(self, monster):
        if self.image == None:
            self.image = load_image("Skill\\angel_attack_sprite.png")
        self.mon = monster
        self.draw_x, self.draw_y = self.mon.draw_x + 10, self.mon.draw_y
        self.layer_y = self.draw_y - (512 / 2)
        self.frame = 0
        self.time_per_action = 1.2  # 하나의 액션이 소요되는 시간
        self.action_per_time = 1.0 / self.time_per_action  # 시간당 수행할 수 있는 액션 개수
        self.frames_per_action = 31  # 액션 당 필요한 프레임 수

    def update(self):
        self.frame = (self.frame + self.frames_per_action * self.action_per_time * game_framework.frame_time) % 31
        if int(self.frame) == 30: self.remove()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 512, 0, 512, 512, self.draw_x, self.draw_y, 512 * 0.5, 512 * 0.5)

    def remove(self):
        game_world.remove_object(self)
