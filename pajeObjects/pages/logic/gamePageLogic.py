from random import choice
from string import ascii_lowercase, ascii_uppercase
from string import digits
import random

class Generate():
    @staticmethod
    def string():
        string1 = [choice(ascii_uppercase) for i in range(4)]
        string2 = [choice(ascii_lowercase) for i in range(4)]
        string3 = [choice(digits) for i in range(4)]
        string = string1 + string2 + string3
        random.shuffle(string)
        string = "".join(string)
        return string

