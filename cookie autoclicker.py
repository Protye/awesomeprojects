import time
import threading
from pynput.keyboard import Listener, KeyCode

'''the Listener modules listens for keyboard inputs, while the clicker is running as a separate thread in background.
when you press the toggle button, the conditional statement in clicker function runs, which does the autoclicking.

'''
TOGGLE_KEY = KeyCode(char="t")

pressing = False # this is because clicker() is always running in background and we don't want it to activate it's code until we turn it on by pressing our toggle button.
mouse = Controller()

def clicker():
    while True:
        if pressing:
            mouse.click(Button.left, 1)
        time.sleep(0.0001) #allows downtime for toggling

def toggle_event(key):
    if key == TOGGLE_KEY:
        global pressing #why did we define global?
        clicking = not clicking


click_thread = threading.Thread(target=clicker) #main thread listening for toggle key, while other thread does clicking
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

