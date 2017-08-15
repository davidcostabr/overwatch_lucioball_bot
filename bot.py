import pyautogui
import random
import time

import win32api, win32con

pyautogui.FAILSAFE = False

time.sleep(2)

import threading
import time


def bt():
    keys = ['w', 'a', 's', 'd']
    firebt = 'home'
    ultimatebt = 'q'
    jumpbt = 'pageup'
    rightbt = 'end'
    jmp = True

    while True:
        key = random.randint(0,3)

        pyautogui.keyDown(keys[key])
        time.sleep(random.randint(0,5))
        pyautogui.keyUp(keys[key])
        fire = random.randint(0,5)
        ultimate = random.randint(0,40)
        jump = random.randint(0,5)
        mouse = random.randint(0,1)

        if jump == 1:
            if jmp:
                pyautogui.keyDown(jumpbt)
                jmp = False
            else:
                pyautogui.keyUp(jumpbt)
                jmp = True


        if random.randint(0,10) == 1:
            pyautogui.press(rightbt)
        if fire == 1:
            pyautogui.press(firebt)
        if ultimate == 1:
            pyautogui.press(ultimatebt)

def timed_output(name, delay, run_event):
    while run_event.is_set():
        xi = random.randint(-1,1)
        yiu = random.randint(-1,1)
        yi = 0
        for x in range(0, random.randint(10,2000)):
            if x % 10 == 0:
                for utr in range(10, random.randint(10,80)):
                    if x % 20 == 0:
                        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,yiu)
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,xi,yi)

            if x % 500 == 0:
                time.sleep(delay)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,xi,yiu)

def main():
    run_event = threading.Event()
    run_event.set()
    d1 = 0.0001
    t1 = threading.Thread(target = timed_output, args = ("bob",d1,run_event))


    t1.start()


    try:
        bt()
    except KeyboardInterrupt:
        run_event.clear()
        t1.join()
        print ("threads successfully closed")



main()
