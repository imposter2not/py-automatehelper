#! python3

#python by default doesn't load up packages in a path, this loads a path
import sys
sys.path.insert(0, './lib')
import i2n_window as i2win
import time
from pynput.keyboard import Listener as kListener, Key
from pynput.mouse import Listener as mListener

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    #debug
    if pressed:
        time.sleep(0.5)
        file_string = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        save_name = "./images/" + file_string + ".png"
        window_handle = i2win.getcurrentwindow()
        bounding_box: object = i2win.getbbox(window_handle)
        i2win.screengrab(bounding_box, save_name)
        print("saved: " + save_name)


def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        mListener.stop()
        return False

# Collect events until released
with kListener(on_press=on_press,
                on_release=on_release) as k_listener:
    with mListener(on_click=on_click) as m_listener:
        k_listener.join()
        m_listener.join()

