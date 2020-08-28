from random import choice
from string import ascii_lowercase, ascii_uppercase
from string import digits
import random
from framework.utils import ElementOperations
from framework.utils.ElementOperations import By

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
    def removeElems(xpath, elems, elem1, elem2):
        x = []
        for elem in elems:
            text = ElementOperations.CheckBox(By.XPATH, xpath, elem).getText()
            if text == elem1 or text == elem2:
                pass
            else:
                x.append(elem)
        return x

