from framework.Base.BaseElement import *
import pyautogui
import os
import time


FILES = jsonGetter.GetJson.getFile(CONFIG, "Files")

class SysOperations:
    def __init__(self):
        '''
        :param file: -
        '''
        pass

    def upload(self, file):
        time.sleep(2)
        path = os.getcwd() + FILES + file
        pyautogui.write(path)
        pyautogui.press('enter')