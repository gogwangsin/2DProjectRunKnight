# GUI 클래스
from pico2d import load_music

from AngelSkillGUI import AngelGUI
from DashSkillGUI import DashGUI
from DistancePannelGUI import DistanceGUI
from HpGUI import HpGUI
from CoinPannelGUI import CoinGUI
from SwordSkillGUI import SwordGUI


class GUI:
    def __init__(self, knight):
        self.HP = HpGUI(knight)
        self.CoinPannel = CoinGUI(knight)
        self.DisPannel = DistanceGUI(knight)
        self.DashSkill = DashGUI(knight)
        self.AngelSkill = AngelGUI(knight)
        self.SwordSkill = SwordGUI(knight)
        self.bgm = load_music('Sound\\backSoundPlay.wav')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def update(self):
        self.HP.update()
        self.CoinPannel.update()
        self.DisPannel.update()
        self.DashSkill.update()
        self.AngelSkill.update()
        self.SwordSkill.update()

    def draw(self):
        self.HP.draw()
        self.CoinPannel.draw()
        self.DisPannel.draw()
        self.DashSkill.draw()
        self.AngelSkill.draw()
        self.SwordSkill.draw()
