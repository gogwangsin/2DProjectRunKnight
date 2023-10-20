
from pico2d import *

import game_world
from kingdom import KingDom
from knight import Knight


def handle_event():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT: # 나가기 클릭
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE: # ESC키 나가기
            running = False
        else:
            knight.handle_event(event)


def create_world():
    global running
    global kingdom
    global knight
    global enemy

    running = True

    # 레이어 규칙 : 나중 레이어가 덮는다 ( 0 < 1 )
    kingdom = KingDom(screen_width, screen_height)
    game_world.add_object(kingdom, 0) # 제일 먼저

    knight = Knight()
    game_world.add_object(knight, 1) # 두번째 레이어


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
while running:
    handle_event()
    update_world()
    render_world()
    delay(0.01)

close_canvas()