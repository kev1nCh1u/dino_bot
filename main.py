from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
import os

#os.system('chrome://dino/')

def jump():
    global run_time
    #waitDown = 0.200 - 1.05 ** run_time / 1000
    #if waitDown < 0.05:
    #    waitDown = 0.05
    #print(waitDown, end=' ')

    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    while look() < basic:
        pass
    print('jump')
    #time.sleep(waitDown)
    pyautogui.keyUp('space')
    time.sleep(0.012)
    pyautogui.keyDown('down')
    pass

def look():
    global run_time
    x = 190 + run_time / 1.13 #5.2
    y = 410

    if x > 450:
         x = 450
    #x = 190 + 1.045 ** run_time

    image = ImageGrab.grab((x, y, x+150, y+10))
    image = ImageOps.grayscale(image)
    imageNp = np.array(image.getcolors())
    imageNpMean = imageNp.mean()
    print('run_time:%.2f place:%.2f value:%.2f' %(run_time, x, imageNpMean))
    #print(loop, imageNpMean)
    return imageNpMean

def lookDown():
    global run_time
    x = 140
    y = 410

    image = ImageGrab.grab((x, y, x+100, y+10))
    image = ImageOps.grayscale(image)
    imageNp = np.array(image.getcolors())
    imageNpMean = imageNp.mean()
    print('%.2f %.2f %.2f' %(run_time, x, imageNpMean))
    return imageNpMean

input('press any key...')
print('start')
start_time = time.time()
run_time = 0
basic = look()
basicDown = lookDown

pyautogui.moveTo(480, 370)
pyautogui.click()
while True:
    run_time = time.time() - start_time
    if look() < basic :
        jump()