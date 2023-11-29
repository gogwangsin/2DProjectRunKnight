from pico2d import load_image, clear_canvas, update_canvas, get_events, hide_cursor
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import play_mode

screen_width, screen_height = 1280, 800  # 640, 400


def init():
    global name, start, title, title_frame, time_per_action, action_per_time, frames_per_action

    hide_cursor()
    title = load_image("GameMode\\title.png")
    name = load_image('GameMode\\title_name.png')
    start = load_image('GameMode\\touch_to_start_sprite.png')

    title_frame = 0
    time_per_action = 2  # 하나의 액션이 소요되는 시간
    action_per_time = 1.0 / time_per_action  # 시간당 수행할 수 있는 액션 개수
    frames_per_action = 20  # 액션 당 필요한 프레임 수


def finish():
    global title, name, start
    del title, name, start


def update():
    global title_frame
    title_frame = (title_frame + frames_per_action * action_per_time * game_framework.frame_time) % 20


def draw():
    clear_canvas()
    title.clip_draw(0, 0, 1280, 720, screen_width // 2, screen_height // 2, screen_width, screen_height)
    name.clip_draw(0, 0, 562, 281, screen_width // 2, screen_height // 2 + 250, 562, 281)
    start.clip_draw(int(title_frame) * 404, 0, 404, 51, screen_width // 2, screen_height // 2 - 270, 404, 51)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def pause():
    pass


def resume():
    pass
