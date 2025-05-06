import pyautogui as pg
import time 
from pynput.mouse import Listener


class Click():
    def __init__(x, y, time, color = (1, 1, 1)): 
        self.x 
        self.y
        self.time 
        self.color = color #must be a tupple (r, g, b)

def on_click(x, y, button, pressed): 
    if pressed: 
        print(f"Ponto: ({x},{y})")

with Listener(on_click = on_click) as listener: 
    listener.join()

