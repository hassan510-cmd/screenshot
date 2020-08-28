import sched
import pyautogui
#  pip install pyautogui
import time
import win32gui
import win32con

# The_program_to_hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(The_program_to_hide, win32con.SW_HIDE)


def take():
    pic = pyautogui.screenshot()
    pic.save('screenshot'+str(time.asctime()
                              ).replace(":", "-").replace(" ", "-")+'.png')


take()