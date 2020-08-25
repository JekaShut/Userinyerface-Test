from framework.Base.BaseElement import *
import pyautogui
import os
import time


FILES = jsonGetter.GetJson.getFile(CONFIG, "Files")


class SysOperations:
    @staticmethod
    def upload(file):
        time.sleep(2)
        path = os.getcwd() + FILES + file
        pyautogui.write(path)
        pyautogui.press('enter')