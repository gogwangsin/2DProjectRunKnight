# 게임 월드를 관리하는 모듈
# 게임 월드의 표현 [ 객체들의 리스트 ]
# 두 개의 layer를 갖는 게임 월드로 구현

objects = [[], [], []]


def add_object(_obj, depth=0):
    objects[depth].append(_obj)


def update():
    for Layer in objects:
        for _obj in Layer:
            _obj.update()


def render():
    for Layer in objects:
        for _obj in Layer:
            _obj.draw()


def remove_object(_obj):
    for Layer in objects:  # 레이어에 안들어있는데 삭제하려면 오류남 [존재하지 않는 객체 삭제]
        if _obj in Layer:  # --> 만약 레이어 안에 있다면 지우기
            Layer.remove(_obj)  # 오브젝트 안에 있는 모든 레이어에 대해 지워라
            return  # 한 번 지웠으면 굳이 for 루프 돌 필요없다. -> 최적화

    raise ValueError('[오류] 없는데 왜 지우려고 하니?')  # 존재하지 않는 걸 지우려고 할 때

def clear():
    for Layer in objects:
        Layer.clear()
        print('객체가 모두 소멸되었습니다')
