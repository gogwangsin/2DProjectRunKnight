# GUI 클래스
from DashSkillGUI import DashGUI
from HpGUI import HpGUI


class GUI:
    def __init__(self, knight):
        self.HP = HpGUI(knight)
        self.DashSkill = DashGUI(knight)
        pass

    def update(self):
        self.HP.update()
        self.DashSkill.update()
        pass

    def draw(self):
        self.HP.draw()
        self.DashSkill.draw()
        pass
