from pico2d import clear_canvas, update_canvas, get_events, load_image
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_r, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT
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
            game_framework.pop_mode()  # over_mode.finish() 호출 -> game_world.clear() + play_mode 존재
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.pop_mode()
            game_framework.change_mode(play_mode)

        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 800 - 1 - event.y
            set_mouse_toggle(mouse_x, mouse_y)
        if event.type == SDL_MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.x, 800 - 1 - event.y
            click_mouse_for_restart(mouse_x, mouse_y)


def pause():
    pass


def resume():
    pass


def set_mouse_toggle(m_x, m_y):
    global result
    if not result.mouse_toggle:
        # 마우스가 ResultPannel에 restart_button 토글 꺼진 박스 크기 안에 있다면
        if m_x >= 640 - 133.65 and m_x <= 640 + 133.65 and m_y >= 135 - 47.85 and m_y <= 135 + 47.85:
            result.mouse_toggle = True
    if m_x < 640 - 170.1 or m_x > 640 + 170.1 or m_y < 135 - 60.9 or m_y > 135 + 60.9:
        result.mouse_toggle = False
        # 사이즈 커진 범위 벗어나면 False


def click_mouse_for_restart(m_x, m_y):
    global result
    if result.mouse_toggle:
        if m_x >= 640 - 170.1 and m_x <= 640 + 170.1 and m_y >= 135 - 60.9 and m_y <= 135 + 60.9:
            game_framework.pop_mode()
            game_framework.change_mode(play_mode)
