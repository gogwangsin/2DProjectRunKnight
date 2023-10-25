
# 클래스 간 실시간으로 상호작용 하기 위한 모듈 from이 아닌 import global_variable로 해야 적용된다.

def init_global_var():
    global running
    global scroll_speed

    running = True
    scroll_speed = 6
