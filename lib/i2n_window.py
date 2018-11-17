#! python3
"""
manipulating window
"""
import re
import time
import win32gui

import win32com.client
from PIL import ImageGrab


def testload():
    print("i2n-window.py loaded")
# get the title of the current active window

def getcurrentwindow():
    active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    active_window_hwnd = win32gui.GetForegroundWindow()
    # print(active_window_title)
    print(active_window_hwnd)
    # return(active_window_title)
    return(active_window_hwnd)
    # print(getwindowhandle(active_window_title))
    # getwindowhandle(active_window_hwnd)


def getwindowhandle(win_title):
    print("debug - getwindowhandle() called")
    desired_title = win_title
    shell = win32com.client.Dispatch("WScript.Shell")
    print(shell)
    toplist, winlist = [], []
    print("debug - enum_cb defined")
    def enum_cb(hwnd, results):
        winlist.append([hwnd, win32gui.GetWindowText(hwnd)])
    win32gui.EnumWindows(enum_cb, toplist)
    pattern = re.compile('[\W_]+')
    transformed_desired_title = pattern.sub('', desired_title).lower()
    targetwindow = [(hwnd, title) for hwnd, title in winlist if transformed_desired_title in
                    pattern.sub('',title).lower()]
    targetwindow = targetwindow[0]
    print(targetwindow)
    return(targetwindow)


def focuswindow(handle):
    win32gui.SetForegroundWindow(handle)


def focuswindowbytitle(win_title):
    hwnd = getwindowhandle(win_title)
    focuswindow(hwnd)


def screenSave(windowbox):
    im = ImageGrab.grab(windowbox)
    return(im)


def screengrab(windowbox: object, file_name: object) -> object:
    print("debug - screengrab call")
    im = PIL.ImageGrab.grab(windowbox)
    print("debug - ImageGrab.grab(windowbox):" + windowbox)
    im.save(file_name)
    print("debug - screengrab saving and done")


def handleSave(handle, img_filename):
    print(handle)
    window_bounding_box = getbbox(handle)
    print(window_bounding_box)
    im = ImageGrab.grab(window_bounding_box)
    im.save(img_filename)


def getbbox(handle):
    print(win32gui.GetWindowRect(handle))
    return(win32gui.GetWindowRect(handle))


def capturewindow(cursor_x, cursor_y):
    file_string = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    time.sleep(0.5)
    save_name = './images/' + file_string + '.png'
    window_handle = getcurrentwindow()
    rect = win32gui.GetWindowRect(window_handle)
    im = ImageGrab.grab(rect)
    im.save(save_name)
    print("saved image - " + save_name + " and cursor xy:" + str(cursor_x) + ", " + str(cursor_y))
    cursor_pos = [cursor_x, cursor_y]
    # need to do checks to make sure this position isn't negative
    # after testing, if it is negative it will show black on the image
    # probably best to have this happen in another function so it can be looped
    # windowcrop(rect, cursor_pos, im, file_string)
    del im
    print("debug-capturewindow done")


def windowcrop(window_rect, cursor_pos, im, crop_name):
    # take the screenshot and cursor position and save a cropped box that can be matched to it
    print(window_rect)
    # window_rect: 0:left, 1:top, 2:right, 3:bottom
    print(cursor_pos)
    # cursor_pos: 0:x 1:y
    # windows positioning:  bottom-left corner is 0,0.   top-right is max res
    target = [(cursor_pos[0] - window_rect[0]), (cursor_pos[1] - window_rect[1])]
    print(target)
    # draw = ImageDraw.Draw(im)
    # draw.point(target, fill=(0, 255, 0))  #green
    cursor_box = (target[0] - 14, target[1] - 8, target[0] + 14, target[1] + 8)
    cut_im = im.crop(cursor_box)
    # maybe template match here
    crop_name = './images/' + crop_name + '-target.png'
    cut_im.save(crop_name)
    # cut_im.show()
    # im.show()
    del cut_im
    print("debug-windowmath done")
