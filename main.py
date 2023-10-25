from pico2d import *

import game_world
import global_var

from GUI import GUI
from kingdom import KingDom
from knight import Knight


def handle_event():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 나가기 클릭
            global_var.running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  # ESC키 나가기
            global_var.running = False
        else:
            knight.handle_event(event)


def create_world():
    global kingdom
    global knight
    global enemy
    global gui

    global_var.init_global_var()

    kingdom = KingDom(screen_width, screen_height)
    game_world.add_object(kingdom, 0)

    knight = Knight()
    game_world.add_object(knight, 1)

    gui = GUI(knight)
    game_world.add_object(gui, 2)


def open_screen():
    global screen_width
    global screen_height

    screen_width = 1280
    screen_height = 800
    open_canvas(screen_width, screen_height)


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


def WaitToStart():
    open_screen()
    # 게임 시작 대기 씬 -> 실행 중 한번만 실행
    create_world()
    # 이벤트 발생하면 시작
    pass

def GameOverScene():
    if True == global_var.running:
        return
    ResetWorld()
    create_world()
    # 이벤트에 따라 종료할지 다시할지
def ResetWorld():
    for sublist in game_world.objects:
        sublist.clear()
    print('모든 객체가 소멸되었습니다!')
    pass

def GameLoop():
    while global_var.running:
        handle_event()
        update_world()
        render_world()
        GameOverScene()
        delay(0.01)


WaitToStart()
GameLoop()
ResetWorld()
close_canvas()
