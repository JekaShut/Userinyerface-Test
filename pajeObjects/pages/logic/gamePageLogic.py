from random import choice
from string import ascii_lowercase, ascii_uppercase
from string import digits
import random
from framework.utils.ElementOperations import By
from pajeObjects.pages import gamePage

class Logic():
    @staticmethod
    def generate_string():
        string1 = [choice(ascii_uppercase) for i in range(4)]
        string2 = [choice(ascii_lowercase) for i in range(4)]
        string3 = [choice(digits) for i in range(4)]
        string = string1 + string2 + string3
        random.shuffle(string)
        string = "".join(string)
        return string

    @staticmethod
    def ReturnValidCheckboxes(textXpath, elems, elem1, elem2):
        '''

        :param textXpath: Xpath of checkboxt titles
        :param elems: All the checkboxes
        :param elem1: 1st element to remove from all elements
        :param elem2: 2nd element to remove from all elements
        :return: elements without elem1 and elem 2
        '''

        x = []
        for elem in elems:
            text = gamePage.GamePage().getCheckboxText(By.XPATH, textXpath, elem)
            if text == elem1 or text == elem2:
                pass
            else:
                x.append(elem)
        return x

    @staticmethod
    def ClickCheckboxes(x, num):
        while num != 1:
            elem = gamePage.GamePage().findRandomCheckbox(x)
            elem.click()
            x.remove(elem)
            num -= 1
        return x

