import pyautogui as mouse
import random
import time
try:
    while True:
        sleep = random.randint(0,120)
        x = random.randint(0, 1600)
        y = random.randint(0,900)
        mouse.moveTo(x, y)
        print("You're annoyed!")
        # time.sleep(sleep)
except KeyboardInterrupt:
    print('\n')
