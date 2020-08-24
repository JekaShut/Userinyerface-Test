from framework.utils import ElementOperations
from selenium.webdriver.common.by import By
from framework.logger.logger import Logger
logger = Logger(__file__).getlog()


class MainPage():
    def __init__(self):
        self.startXpath = "//a[@class='start__link']"

    def assertPage(self):
        text = ElementOperations.Button(By.XPATH, self.startXpath).getText()
        return text

    def startGame(self):
        ElementOperations.Button(By.XPATH, self.startXpath).click()