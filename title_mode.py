from pico2d import load_image, get_time, clear_canvas, update_canvas, get_events, close_canvas, open_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE

import game_framework


def init():
    global image
    global logo_start_time

    open_screen()
    image = load_image("GameMode\\title.png")
    logo_start_time = get_time()


def finish():
    global image
    del image


def update():
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.quit()


def draw():
    clear_canvas()
    image.draw(screen_width // 2, screen_height // 2)  # 400, 300
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def pause():
    pass


def resume():
    pass


def open_screen():
    global screen_width
    global screen_height

    screen_width = 1280
    screen_height = 720
    open_canvas(screen_width, screen_height)
