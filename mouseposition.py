import os, time
from pynput.mouse import Button, Controller
mouse = Controller()

def main():
    cmd = "open /Applications/Firefox.app"
    os.system(cmd)
    # To open any program by name
    time.sleep(3)

    print(mouse.position)

main()