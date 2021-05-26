import os, time
from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.mouse import Button, Controller
mouse = Controller()

def main():
    cmd = "open /Applications/Firefox.app"
    os.system(cmd)
    time.sleep(5)

    mouse.position = (484.6484375,74.58984375)
    time.sleep(0.1)
    mouse.click(Button.left, 1)
    keyboard.type("https://drive.google.com/drive/u/0/my-drive")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(5)
    mouse.position = (80.09765625, 223.8046875)
    mouse.click(Button.left, 1)
    time.sleep(0.8)
    mouse.position = (109.8828125, 392.98828125)
    time.sleep(0.8)
    mouse.click(Button.left, 1)
    time.sleep(5)

    #only use the code below if you don't want the program to open your application
    #or you can use formfiller2.py, it's the same thing

    with open('form.txt') as f:
        content = f.readlines()
    
    for x in content:
        line = x.rstrip("\n")
        x = 0
        count = 0
        while x != -1:
            x = line.find(",")
            # each segment is seperated by ',' wich can be changed to your choosing
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
            time.sleep(0.5)


main()