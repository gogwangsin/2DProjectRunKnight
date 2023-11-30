from pico2d import delay
import time
running = None
stack = None


def change_mode(mode):
    global stack
    print('change_mode 호출', f'{mode}')
    if (len(stack) > 0):
        stack[-1].finish()
        stack.pop()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    global stack
    print('push_mode 호출', f'{mode}')
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    global stack
    print('pop_mode 호출')
    if (len(stack) > 0):
        stack[-1].finish() # -> def finish(): game_world.clear()
        stack.pop()

    if (len(stack) > 0):
        print('STACK[-1]:', f'{stack[-1]}') # play_mode
        stack[-1].resume()


def quit():
    global running
    running = False


def run(start_mode):
    global running, stack
    print('start_mode 호출:', f'{start_mode}')
    running = True
    stack = [start_mode]
    start_mode.init()

    global frame_time, current_time
    frame_time = 0.0
    current_time = time.time()
    while (running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        # delay(0.01)  # 추가
        frame_time = time.time() - current_time
        # frame_rate = 1.0 / frame_time
        current_time += frame_time

    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        print('마지막 모드 종료 stack[-1]',f'{stack[-1]}')
        stack[-1].finish()
        stack.pop()
