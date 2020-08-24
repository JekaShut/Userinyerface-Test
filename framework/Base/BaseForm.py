from framework.Base import BaseElement
from selenium.common.exceptions import StaleElementReferenceException

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()


class BaseForm():
    def __init__(self, elem= ""):
        self.elem = elem

class Check(BaseForm):
    def isDisplayed(self):
        try:
            result = self.elem.is_displayed()
            return result
        except StaleElementReferenceException:
            return False


