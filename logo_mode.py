from pico2d import load_image, get_time, clear_canvas, update_canvas, hide_cursor
import game_framework
import title_mode

screen_width, screen_height = 1280, 800  # 640, 400


def init():
    global image, logo_start_time
    hide_cursor()
    image = load_image("GameMode\\logo.png")
    logo_start_time = get_time()


def finish():
    global image
    del image


def update():
    global logo_start_time
    if get_time() - logo_start_time >= 3.0:
        game_framework.change_mode(title_mode)


def draw():
    clear_canvas()
    image.draw(640, 400)
    update_canvas()
    pass


def handle_events():
    pass


def pause():
    pass


def resume():
    pass
