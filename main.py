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

    kingdom = KingDom(screen_width, screen_height, global_var.scroll_speed)
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


open_screen()
create_world()
while global_var.running:
    handle_event()
    update_world()
    render_world()
    delay(0.01)

close_canvas()
