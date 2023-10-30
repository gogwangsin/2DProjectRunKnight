from enemy_crown import Run


class StateMachine:
    def __init__(self, object):
        self.object = object
        self.cur_state = Run
        # 상태 전환 테이블
        pass

    def start(self):
        self.cur_state.entry(self.object, ('START', 0))
        # entry action : event:( key == START, value == 0 )으로 전달

    def update(self):
        self.cur_state.do(self.object)
        pass

    def draw(self):
        self.cur_state.draw(self.object)
        pass

    def handle_event(self, event):
        pass
        # for check_event, next_state in self.transitions[self.cur_state].items():
        #     if check_event(event):
        #         self.cur_state.exit(self.knight, event)
        #         self.cur_state = next_state
        #         self.cur_state.entry(self.knight, event)
        #         return True
        # return False
