from framework.Base import BaseElement

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()


class BaseForm():
    def __init__(self, elem):
        self.elem = elem

class Check(BaseForm):
    def isDisplayed(self):
        result = self.elem.is_displayed()
        return result


