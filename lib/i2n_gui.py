#! python3
"""
manipulating window
"""
import tkinter as tk
from tkinter import ttk

NORM_FONT = ("Verdana", 10)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("screengrab_running")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    label2 = ttk.Label(popup, text="t to start stopwatch", font=NORM_FONT)
    label2.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="this does nothing", command=popup.destroy)
    B1.pack()
    popup.update()


def mbox(msg, frame=True, t=False, entry=False):
    msgbox = MessageBox(msg, frame, t, entry)
