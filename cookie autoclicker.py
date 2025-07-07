import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

#toggle button

TOGGLE_KEY = KeyCode(char="t")

clicking = False # what thinking did we do to define this variable?
mouse = Controller()
