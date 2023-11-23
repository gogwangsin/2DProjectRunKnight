# 게임 월드를 관리하는 모듈
# 게임 월드의 표현 [ 객체들의 리스트 ]
# 두 개의 layer를 갖는 게임 월드로 구현

objects = [[], [], []]
# [0] : 배경
# [1] : 객체-> Y정렬 가변 랜더링
# [2] : UI
collision_pairs = {}


# 충돌 관점의 월드 정의 dictionary

def add_object(_obj, depth=0):
    objects[depth].append(_obj)


def update():
    for Layer in objects:
        for _obj in Layer:
            _obj.update()


def render():
    layer_0_draw()  # 배경
    layer_1_draw()  # 가변 객체
    layer_2_draw()  # GUI


def remove_object(_obj):
    for Layer in objects:  # 레이어에 안들어있는데 삭제하려면 오류남 [존재하지 않는 객체 삭제]
        if _obj in Layer:  # --> 만약 레이어 안에 있다면 지우기
            Layer.remove(_obj)  # 오브젝트 안에 있는 모든 레이어에 대해 지워라
            remove_collision_object(_obj)
            del _obj
            return  # 한 번 지웠으면 굳이 for 루프 돌 필요없다. -> 최적화

    raise ValueError('[오류] 없는데 왜 지우려고 하니?')  # 존재하지 않는 걸 지우려고 할 때


def clear():
    for Layer in objects:
        Layer.clear()
    print('객체가 모두 소멸되었습니다')


def layer_0_draw():
    layer_0_objects = objects[0]
    for obj in layer_0_objects:
        obj.draw()


def layer_1_draw():
    # obj.draw_y에 따라 정렬 ( reverse 내림차순 )
    layer_1_objects = objects[1]
    sorted_layer_1 = sorted(layer_1_objects, key=lambda obj: obj.layer_y, reverse=True)
    for obj in sorted_layer_1:
        obj.draw()


def layer_2_draw():
    layer_2_objects = objects[2]
    for obj in layer_2_objects:
        obj.draw()


def collide(A, B):
    LeftA, BottomA, RightA, TopA = A.get_bounding_box()
    LeftB, BottomB, RightB, TopB = B.get_bounding_box()

    if LeftA > RightB: return False
    if RightA < LeftB: return False
    if TopA < BottomB: return False
    if BottomA > TopB: return False

    return True


def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'New Group {group} added.')
        collision_pairs[group] = [[], []]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def remove_collision_object(_obj):
    for pairs in collision_pairs.values():
        if _obj in pairs[0]:
            pairs[0].remove(_obj)
        if _obj in pairs[1]:
            pairs[1].remove(_obj)


def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
