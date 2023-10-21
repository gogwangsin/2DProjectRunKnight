# GUI 클래스

class HP:
    def __init__(self, knight_HP):
        self.hp_bar = knight_HP
        print('용사 체력 : ',self.hp_bar)
        pass

    def update(self):
        pass

    def draw(self):
        pass


class GUI:
    def __init__(self, knight):
        GUI.HP = HP(knight.get_hp())


        pass

    def update(self):
        pass


    def draw(self):
        pass