import os, time
from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.mouse import Button, Controller
mouse = Controller()

def main():
    time.sleep(5)
    # use this time to quickly open the application of your choice
    with open('form.txt') as f:
        content = f.readlines()
    
    for x in content:
        line = x.rstrip("\n")
        x = 0
        count = 0
        while x != -1:
            x = line.find(",")
            if x == -1:
                seg = line
            else:
                seg = line[0:x]
                line = line[x+1:]
                prev = x+1
            count += 1
            keyboard.type(seg)
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        
        for x in range(count):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            time.sleep(0.3)

main()