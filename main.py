import pico2d
import global_var
import play_mode


play_mode.open_screen()
play_mode.init()
while global_var.running:
    play_mode.handle_event()
    play_mode.update_world()
    play_mode.draw()
    pico2d.delay(0.01)
play_mode.finish()
pico2d.close_canvas()
