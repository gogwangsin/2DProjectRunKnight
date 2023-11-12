from pico2d import load_image, get_time, clear_canvas, update_canvas, get_events, close_canvas, open_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import play_mode


def init():
    global title
    global name
    global start
    open_screen()
    title = load_image("GameMode\\title.png")
    name = load_image('GameMode\\title_name.png')
    start = load_image('GameMode\\touch_to_start.png')



def finish():
    global title, name, start
    del title, name, start


def update():
    pass


def draw():
    clear_canvas()
    title.clip_draw(0, 0, 1280, 720, screen_width // 2, screen_height // 2, screen_width, screen_height)
    name.clip_draw(0, 0, 562, 281, screen_width // 2, screen_height // 2 + 210, 506, 253)
    start.clip_draw(0, 0, 404, 51, screen_width // 2, screen_height // 2 - 250, 364, 46)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            close_canvas()
            game_framework.change_mode(play_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
            close_canvas()


def pause():
    pass


def resume():
    pass


def open_screen():
    global screen_width
    global screen_height

    screen_width = 1216
    screen_height = 684
    open_canvas(screen_width, screen_height)
