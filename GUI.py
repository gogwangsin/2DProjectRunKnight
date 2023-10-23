# GUI 클래스
from HP import HP


class GUI:

    def __init__(self, knight):
        GUI.HP = HP(knight)
        pass

    def update(self):
        GUI.HP.update()
        pass


    def draw(self):
        GUI.HP.draw()
        pass