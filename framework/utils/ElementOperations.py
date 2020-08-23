from framework.utils.BaseElement import *
from selenium.webdriver.common.by import By
import random


class Button(BaseElement):

    def getText(self):
        '''
        :return: text of element
        '''
        self._find()
        return self.element.text

    def send(self, keys):
        '''
        :param keys: Text to send
        :return: nothing
        Entering a text to field
        '''
        self._find()
        self.element.send_keys(keys)


class Input(BaseElement):

    def clear(self):
        '''
        :return: nothing
        Clear input textfield
        '''
        self._find()
        self.element.clear()

    def send(self, keys):
        '''
        :param keys: Text to send
        :return: nothing
        Entering a text to field
        '''
        self._find()
        self.element.send_keys(keys)


class Label(BaseElement):
    def getText(self):
        '''
        :return: text of element
        '''
        self._find()
        return self.element.text

class DropDown(BaseElement):
    def random(self):
        '''
        :return: random element of dropdown
        '''
        element = self._finds()
        element = random.choice(element)
        return element


class CheckBox(BaseElement):
     def random(self):
        '''
        :return: random element of dropdown
        '''
        element = self._finds()
        element = random.choice(element)
        return element










