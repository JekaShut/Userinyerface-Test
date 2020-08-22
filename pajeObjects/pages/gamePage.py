from framework.utils import ElementOperations
from selenium.webdriver.common.by import By

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()


class GamePage:
    def __init__(self):
        self.cookieButtonXpath = "//div[@class='align__cell']/button"
        self.HideHelpXpath = "//span[@class='discrete']"

    def removeCookie(self):
        ElementOperations.Button(By.XPATH, self.cookieButtonXpath).click()

    def removeHelp(self):
        ElementOperations.Button(By.XPATH, self.HideHelpXpath).click()