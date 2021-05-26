import os, time
from pynput.mouse import Button, Controller
mouse = Controller()

def main():
    cmd = "open /Applications/Firefox.app"
    os.system(cmd)
    time.sleep(0.2)

    mouse.position = (205.58203125,415.03515625)
    loop = 100
    wait = 0.05
    for x in range(loop):
        time.sleep(wait)
        mouse.click(Button.left, 1)

    time.sleep(0.2)
    cmd = "open /Applications/Visual\ Studio\ Code.app"
    os.system(cmd)
    mouse.position = (787.6796875,68.4609375)

main()