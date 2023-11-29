from pico2d import clear_canvas, update_canvas, get_events, load_image
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_r, SDL_MOUSEMOTION
import game_framework
import game_world
import play_mode
import title_mode
from ResultPannel import ResultPannel

mouse_x, mouse_y = -200, -200
mouse_x_size, mouse_y_size = 97 * 0.9, 92 * 0.9

def init():
    global result, cursor_image
    cursor_image = load_image('UI\\cursor.png')
    result = ResultPannel()
    game_world.add_object(result, 2)


def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    cursor_image.clip_draw(0, 0, 97, 92, mouse_x, mouse_y, mouse_x_size, mouse_y_size)
    update_canvas()


def handle_events():
    global mouse_x, mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()  # over_mode.finish() 호출 -> game_world.clear()
            game_framework.run(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            # game_framework.pop_mode()
            # game_framework.run(play_mode)
            game_framework.change_mode(play_mode)
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 800 - 1 - event.y


def pause():
    pass


def resume():
    pass
