
from pico2d import *

def handle_event():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



screen_width = 1280
screen_height = 800

open_canvas(screen_width, screen_height)

background_image = load_image("BackGround\\road_background.png")
background_image.draw(screen_width // 2 , screen_height // 2)
update_canvas()

running = True

show_lattice()
while running:
    clear_canvas()
    handle_event()
    background_image.clip_draw(0, 0, screen_width, screen_height, screen_width // 2, screen_height // 2 - 45, 1280, 720)
    update_canvas()
    delay(0.01)
