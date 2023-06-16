import keyboard
import mouse
import time

isClicking = False


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Off')
    else:
        isClicking = True
        print('On')


keyboard.add_hotkey('k', set_clicker())

while True:
    if isClicking:
        mouse.double_click(button='left')
        time.sleep(0.01)

