#! python3

#python by default doesn't load up packages in a path, this loads a path
import sys
from pynput.keyboard import Key
# python by default doesn't load up packages in a path, this loads a path
import sys

from pynput.keyboard import Key

sys.path.insert(0, './lib')
import i2n_window as i2win

from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    i2win.getcurrentwindow()


def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))


def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    # print('{0} release'.format(
    #     key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press,
              on_release=on_release,
              on_click=on_click,
              on_scroll=on_scroll) as listener:
    listener.join()

#
# while True:
#     # wait(1)
#     # key = KeyAsyncReader.getCharsFromEvents()
#     # if not key is None:
#     #     if c == "c":
#     #         break
#     #     print(c)
#     print(msvcrt.kbhit())
#     input_char = msvcrt.getch()
#     print(msvcrt.kbhit())
#     print(input_char)
#     if input_char.upper() == 'S':
#         print('YES')
#         break
