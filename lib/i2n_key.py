#! python3
"""
sending keyboard commands with different methods

tip functions
"""
import ctypes
import time

import pyautogui

###ctype input###

#setup for directinput req
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actuals Functions
def testload():
	print("i2n-key.py loaded")

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def scanTranslate(key):
	dxkeymap = {
	'up' : 0xC8,
	'down' : 0xD0,
	'left' : 0xCB,
	'right' : 0xCD,
	'enter' : 0x1C,
	'spacebar' : 0x39,
	'1' : 0x02,
	'2' : 0x03,
	'3' : 0x04,
	'4' : 0x05,
	'5' : 0x06,
	'6' : 0x07,
	'esc' : 0x01,
	'q' : 0x10,
	'w' : 0x11,
	'e' : 0x12,
	'r' : 0x13,
	't' : 0x14,
	'y' : 0x15,
	'a' : 0x1E,
	's' : 0x1F,
	'd' : 0x20,
	'f' : 0x21,
	'g' : 0x22,
	'h' : 0x23,
	'np0' : 0x52,
	'np1' : 0x4F,
	'np2' : 0x50,
	'np3' : 0x51,
	'dfdown' : 0x4C,
	'dfup' : 0x48,
	'dfleft' : '0x4B',
	'dfright' : 0x4D,
	'np4' : 0x4B,
	'np5' : 0x4C,
	'np6' : 0x4D,
	'np7' : 0x47,
	'np8' : 0x48,
	'np9' : 0x49,
	}
	return(dxkeymap[key])

###pyautogui input###

#keyboard functions

def kPress(key):
	pyautogui.typewrite(key)

def kHammer(key,times):
	for i in range(times):
		pyautogui.typewrite(key)

def kHold(key, holdtime):
	pyautogui.keyDown(key)
	time.sleep(holdtime)
	pyautogui.keyUp(key)

#directx functions to be used for programs that can only accept directinput
#don't give time for a 0.1 key press
def dkPress(key, times=0.1):
	PressKey(key)
	time.sleep(times)
	ReleaseKey(key)
	time.sleep(0.1)

def dkhold(key):
	PressKey(key)

def dkrelease(key):
	ReleaseKey(key)

