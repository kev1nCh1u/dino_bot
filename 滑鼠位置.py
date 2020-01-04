import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

x = 0
while 1:
    x, y=pyautogui.position()
    print(x, y)