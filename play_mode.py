from pico2d import get_events, open_canvas, clear_canvas, update_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE

import game_framework
import game_world
import global_var
from GUI import GUI
from enemy_crown import EnemyCrown
from kingdom import KingDom
from knight import Knight


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            knight.handle_event(event)


def init():
    global kingdom
    global knight
    global enemy
    global gui

    open_screen()
    global_var.scroll_speed = 6.4

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


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    pass
