#! python3
"""
manipulating window
"""
from PIL import Image, ImageGrab
import os
import time
import re
import string
import win32gui
import win32com.client


def testload():
    print("i2n-window.py loaded")

# get the title of the current active window


def getcurrentwindow():
    active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    active_window_hwnd = win32gui.GetForegroundWindow()
    # print(active_window_title)
    # print(active_window_hwnd)
    return(active_window_hwnd)
    # print(getwindowhandle(active_window_title))
    # getwindowhandle(active_window_hwnd)


def getwindowhandle(win_title):
    desired_title = win_title
    shell = win32com.client.Dispatch("WScript.Shell")
    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append([hwnd, win32gui.GetWindowText(hwnd)])

    win32gui.EnumWindows(enum_cb, toplist)
    pattern = re.compile('[\W_]+')
    transformed_desired_title = pattern.sub('', desired_title).lower()
    targetwindow = [(hwnd, title) for hwnd, title in winlist if transformed_desired_title in
                    pattern.sub('',title).lower()]
    targetwindow = targetwindow[0]
    return(targetwindow)


def focuswindow(handle):
    win32gui.SetForegroundWindow(handle)


def focuswindowbytitle(win_title):
    hwnd = getwindowhandle(win_title)
    focuswindow(hwnd)


def screenSave(windowbox):
    im = ImageGrab.grab(windowbox)
    return(im)


def screengrab(windowbox, file_name):
    im = ImageGrab.grab(windowbox)
    im.save(file_name)


def handleSave(handle, img_filename):
    print(handle)
    window_bounding_box = getbbox(handle)
    print(window_bounding_box)
    im = ImageGrab.grab(window_bounding_box)
    im.save(img_filename)


def getbbox(handle):
    # print(win32gui.GetWindowRect(handle))
    return(win32gui.GetWindowRect(handle))
    # return win32gui.GetWindowRect(handle)

# def main(windowbox):
# 	screenGrab(windowbox)

# if __name__ == '__main__':
# 	main()

