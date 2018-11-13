#! python3

# python by default doesn't load up packages in a path, this loads a path
import sys

sys.path.insert(0, './lib')
import i2n_window as i2win
import i2n_gui as i2gui
# import i2n_tools as i2tool
import time
from pynput.keyboard import Listener as kListener, Key, KeyCode
from pynput.mouse import Listener as mListener

file_path = './logs/temp_log.txt'
temp_log = open(file_path, "w")
# global stopwatch_value
stopwatch_value = 0


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    # debug
    if pressed:
        global stopwatch_value
        if stopwatch_value != 0:
            stopwatch_value = float(time.strftime("%H%M%S", time.gmtime())) - float(stopwatch_value)
            print(stopwatch_value)
            stopwatch_value = 0
        # the stopwatch should only stop on mouse click, mouse click should not start one
        # else:
        #     stopwatch_value = time.strftime("%H%M%S", time.gmtime())

        time.sleep(0.5)
        file_string = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        save_name = './images/' + file_string + '.png'
        window_handle = i2win.getcurrentwindow()
        bounding_box: object = i2win.getbbox(window_handle)
        i2win.screengrab(bounding_box, save_name)
        print("saved: " + save_name)

        # log_string = file_string + ", event, click, " + x + ", " + y + ", " + str(bounding_box) + ", " + save_name
        # temp_log.write(log_string)


def on_press(key):
    print('{0} pressed'.format(key))
    # print(key.value())
    if key == KeyCode.from_char('t'):
        global stopwatch_value
        if stopwatch_value != 0:
            stopwatch_value = float(time.strftime("%H%M%S", time.gmtime())) - float(stopwatch_value)
            print(stopwatch_value)
            stopwatch_value = 0
        else:
            stopwatch_value = time.strftime("%H%M%S", time.gmtime())


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        mListener.stop()
        return False


with kListener(on_press=on_press,
               on_release=on_release) as k_listener:
    with mListener(on_click=on_click) as m_listener:
        i2gui.popupmsg("esc to quit")
        k_listener.join()
        m_listener.join()
