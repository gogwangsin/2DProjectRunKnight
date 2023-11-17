# GUI 클래스
from AngelSkillGUI import AngelGUI
from DashSkillGUI import DashGUI
from DistancePannelGUI import DistanceGUI
from HpGUI import HpGUI
from CoinPannelGUI import CoinGUI


class GUI:
    def __init__(self, knight):
        self.HP = HpGUI(knight)
        self.CoinPannel = CoinGUI(knight)
        self.DisPannel = DistanceGUI(knight)
        self.DashSkill = DashGUI(knight)
        self.AngelSkill = AngelGUI(knight)
        pass

    def update(self):
        self.HP.update()
        self.CoinPannel.update()
        self.DisPannel.update()
        self.DashSkill.update()
        self.AngelSkill.update()
        pass

    def draw(self):
        self.HP.draw()
        self.CoinPannel.draw()
        self.DisPannel.draw()
        self.DashSkill.draw()
        self.AngelSkill.draw()
        pass
