from pico2d import load_image, get_time, clear_canvas, update_canvas, get_events, close_canvas, open_canvas
import game_framework
import title_mode


def init():
    global image
    global logo_start_time

    open_screen()
    image = load_image("GameMode\\logo.png")
    logo_start_time = get_time()


def finish():
    global image
    del image


def update():
    global logo_start_time
    if get_time() - logo_start_time >= 3.0:
        close_canvas()
        game_framework.change_mode(title_mode)


def draw():
    clear_canvas()
    image.draw(screen_width // 2, screen_height // 2)  # 400, 300
    # image.clip_draw(0, 0, 800, 600, screen_width // 2, screen_height // 2, screen_width, screen_height)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    pass


def pause():
    pass


def resume():
    pass


def open_screen():
    global screen_width
    global screen_height

    screen_width = 1280
    screen_height = 800
    open_canvas(screen_width, screen_height)
