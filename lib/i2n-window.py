#! python3
"""
manipulating window
"""
import PIL
import os
import time

import win32gui
import win32com.client

def getwindowhandle(win_title):
	desired_title = win_title
	shell = win32com.client.Dispatch("WScript.Shell")
	toplist, winlist = [], []
	def enum_cb(hwnd, results):
	    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
	win32gui.EnumWindows(enum_cb, toplist)

	targetwindow = [(hwnd, title) for hwnd, title in winlist if desired_title in title.lower()]
	targetwindow = targetwindow[0]
	hwnd = targetwindow[0]
	return(hwnd)

def focuswindow(handle):
	win32gui.SetForegroundWindow(handle)

def focuswindowbytitle(win_title):
	hwnd = getwindowhandle(win_title)
	focuswindow(hwnd)

def screenSave(windowbox):
	im = PIL.ImageGrab.grab(windowbox)
	return(im)

def screenGrab(windowbox):
	im = PIL.ImageGrab.grab(windowbox)
	im.save('imagelook.png')

def getbbox(handle):
	return(win32gui.GetWindowRect(handle))

# def main(windowbox):
# 	screenGrab(windowbox)

# if __name__ == '__main__':
# 	main()

