#! python3
"""
sending mouse commands

tip functions
"""
import ctypes

import pyautogui


#mouse functions

def mGet():
	mouseX, mouseY = pyautogui.position()
	return(mouseX, mouseY)

def mMove(x, y, speed):
	pyautogui.moveTo(x, y, speed)

def mRel(x, y, speed):
	pyautogui.moveRel(x, y, speed)

""" If you want to specify which mouse button to use, include the button
keyword argument, with a value of 'left', 'middle', or 'right'. For example,
pyautogui.click(100, 150, button='left') will click the left mouse button at
the coordinates (100, 150), while pyautogui.click(200, 250, button='right')
will perform a right-click at (200, 250). """
def mClick():
	pyautogui.click()

def dmMove(x, y):
	ctypes.windll.user32.SetCursorPos(x,y)


def click():
	ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # left down
	ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left up

#dragTo() and dragRel() for drags