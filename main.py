from pico2d import *

import game_world
import global_var

from GUI import GUI
from enemy_crown import EnemyCrown
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

    enemy = EnemyCrown()
    game_world.add_object(enemy, 1)

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


# ==========================================================


def wait_to_start():
    open_screen()
    # 게임 시작 대기 씬 -> 실행 중 한번만 실행
    # 이벤트 발생하면 시작
    create_world()
    print('객체가 생성되었습니다!')


def game_over_scene():
    if True == global_var.running:
        return
    # reset_world()
    # create_world()
    # 이벤트에 따라 종료할지 다시할지


def reset_world():
    for sublist in game_world.objects:
        sublist.clear()
    print('모든 객체가 소멸되었습니다!')


def game_loop():
    while global_var.running:
        handle_event()
        update_world()
        render_world()
        game_over_scene()
        delay(0.01)


wait_to_start()
game_loop()
reset_world()
close_canvas()
