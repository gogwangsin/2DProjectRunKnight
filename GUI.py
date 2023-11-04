# GUI 클래스
from HP import HP


class GUI:

    def __init__(self, knight):
        self.HP = HP(knight)
        pass

    def update(self):
        self.HP.update()
        pass

    def draw(self):
        self.HP.draw()
        pass
