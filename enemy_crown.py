import random
from pico2d import load_image, get_time
import game_framework
import global_var



class Run:

    @staticmethod
    def entry(crown, event):
        crown.Dir = -1
        crown.speed = 2

        crown.last_frame_time = get_time()
        crown.update_frame_time = 0.2  # 프레임 업데이트 시간 간격 : 0.8 -> 스크롤 속도에 영향 받음 : 0.08

    @staticmethod
    def exit(crown, event):
        pass

    @staticmethod  # 함수를 그룹핑 하는 역할
    def do(crown):
        if get_time() - crown.last_frame_time > crown.update_frame_time:
            crown.frame = (crown.frame + 1) % 4
            crown.last_frame_time = get_time()

        crown.draw_x += crown.Dir * (global_var.scroll_speed + crown.speed)
        if crown.draw_x < -crown.draw_width:
            crown.draw_x, crown.draw_y = 1280 + crown.draw_width, random.randint(70, 650)

    @staticmethod
    def draw(crown):  # frame, action, 사진 가로,세로, x,y, 크기 비율
        crown.image.clip_draw(crown.frame * crown.image_width,
                              crown.action * crown.image_height,
                              crown.image_width, crown.image_height,
                              crown.draw_x, crown.draw_y,
                              crown.draw_width, crown.draw_height)


# ==============================================================================
class EnemyCrown:
    image = None

    def __init__(self):
        self.init_crown_var()
        self.init_state_machine()

    def update(self):
        self.state_machine.update()
        self.update_hp()

    def draw(self):
        self.state_machine.draw()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))  # 입력 이벤트

    def init_crown_var(self):
        if self.image == None:
            self.image = load_image("Object\\enemy_crown_axe.png")

        self.image_width = 515
        self.image_height = 452  # 한개 사진 크기

        self.draw_width = 515 * 0.25  # 원본 1/4배
        self.draw_height = 452 * 0.25  # 사진 그릴 크기 [ 비율 조정 ]

        self.draw_x, self.draw_y = 1280 + self.draw_width, random.randint(70, 650)
        # 화면 크기_x+ 그릴 크기_x(밖에 그리기), y범위 70~650

        self.frame = 0
        self.HP = 100
        self.Dir = 0
        self.action = 0  # 0 고정

    def init_state_machine(self):
        from enemy_state_machine import StateMachine
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def get_current_hp(self):
        return self.HP

    def update_hp(self):
        pass
