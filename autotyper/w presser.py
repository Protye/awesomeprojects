import pyautogui
import time
import threading
from pynput.keyboard import Listener, KeyCode


'''once pressed toggled button, continuous press down on the key 'w' until toggled off
'''

TOGGLE_KEY = KeyCode(char="t")

pressing = False

def toggle_event(key):
    if key == TOGGLE_KEY:
        global pressing #global to refer to the global instead of a one-time local
        pressing = not pressing


def walker():
    while True:
        if pressing: #why do I need this ifstatement? why not just the while?
            pyautogui.keyDown("w")
    time.sleep(0.001)

click_thread = threading.Thread(target=walker) #main thread listening for toggle key, while other thread does clicking
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

