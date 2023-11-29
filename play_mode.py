import time

from pico2d import get_events, clear_canvas, update_canvas, hide_cursor
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_b

import game_framework
import game_world
import title_mode
from Coin import coin_add
from EnemyTrap import trap_add
from GUI import GUI
from HpPortion import hp_portion_add
from EnemyCrown import enemy_crown_add
from Kingdom import KingDom
from RunKnight import Knight

screen_width, screen_height = 1280, 800  # 640, 400


def scroll_init():
    global pixel_per_meter, scroll_km_per_hour, scroll_meter_per_minute
    global scroll_meter_per_second, scroll_pixel_per_second

    pixel_per_meter = 10.0 / 0.3  # 10 pixel 30cm
    scroll_km_per_hour = 52.0  # Km / Hour 52.0
    scroll_meter_per_minute = (scroll_km_per_hour * 1000.0 / 60.0)
    scroll_meter_per_second = (scroll_meter_per_minute / 60.0)
    scroll_pixel_per_second = (scroll_meter_per_second * pixel_per_meter)


def handle_events():
    global bb_toggle
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
            if bb_toggle:
                bb_toggle = False
            elif not bb_toggle:
                bb_toggle = True
        else:
            knight.handle_event(event)


def init():
    global hp_start_time, coin_start_time, crown_start_time, trap_start_time
    global kingdom, knight, gui
    global bb_toggle

    bb_toggle = False
    hide_cursor()
    scroll_init()

    kingdom = KingDom(screen_width, screen_height)
    game_world.add_object(kingdom, 0)

    knight = Knight()
    game_world.add_object(knight, 1)
    game_world.add_collision_pair('Knight:Portion', knight, None)
    game_world.add_collision_pair('Knight:Coin', knight, None)
    game_world.add_collision_pair('Knight:Trap', knight, None)
    game_world.add_collision_pair('Knight:Crown', knight, None)

    gui = GUI(knight)
    game_world.add_object(gui, 2)

    hp_start_time = time.time()
    coin_start_time = time.time()
    trap_start_time = time.time()
    crown_start_time = time.time()


def update():
    add_objects()
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def add_objects():
    hp_portion_add()
    coin_add()
    trap_add()
    enemy_crown_add()
