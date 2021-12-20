import psutil
from plyer.utils import platform
from plyer import notification
import time
import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from threading import *
import os
import sys

root = tkinter.Tk()
def on_close():

     #custom close options, here's one example:

     close = messagebox.askokcancel("Close", "Would you like to close the program?")
     if close:
          root.destroy()

root.protocol("WM_DELETE_WINDOW",  on_close)
root.mainloop()