from pico2d import close_canvas, open_canvas

import game_framework
import logo_mode as start_mode
# import title_mode as start_mode
# import play_mode as start_mode
# import over_mode as start_mode

open_canvas(1280, 800)
game_framework.run(start_mode)
close_canvas()


# C:\Drill\LectureCode