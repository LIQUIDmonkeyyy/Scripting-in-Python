import os, time
from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.mouse import Button, Controller
mouse = Controller()
# videos for pynput: https://www.youtube.com/watch?v=2BXr9U6ZL8Y
#                   https://www.youtube.com/watch?v=DTnz8wA6wpw

def main():
    cmd = "open /Applications/Firefox.app"
    os.system(cmd)
    # To open any program by name
    time.sleep(3)

    mouse.position = (484.6484375,74.58984375)
    time.sleep(0.1)
    mouse.click(Button.left, 1)
    keyboard.type("https://orteil.dashnet.org/cookieclicker/")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(4)
    mouse.position = (205.58203125,415.03515625)

    
    loop = 10
    wait = 0.1
    for x in range(loop):
        time.sleep(wait)
        mouse.click(Button.left, 1)
    

main()