from pico2d import clear_canvas, update_canvas, get_events, close_canvas, open_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_r

import game_framework
import game_world
import play_mode
import title_mode
from result_pannel import ResultPannel


def init():
    global result
    result = ResultPannel()
    game_world.add_object(result, 2)


def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            game_framework.pop_mode()
            game_framework.run(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            close_canvas()
            game_framework.pop_mode()
            game_framework.run(play_mode)



def pause():
    pass


def resume():
    pass

