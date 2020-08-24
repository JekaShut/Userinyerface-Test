from framework.utils import ElementOperations
from selenium.webdriver.common.by import By
from framework.logger.logger import Logger
logger = Logger(__file__).getlog()


class MainPage():
    def __init__(self):
        self.startXpath = "//a[@class='start__link']"
        self.EXtext = "HERE"

    def assertPage(self):
        logger.info("Trying to get text")
        text = ElementOperations.Button(By.XPATH, self.startXpath).getText()
        return text

    def startGame(self):
        logger.info("Trying to click" + self.startXpath)
        ElementOperations.Button(By.XPATH, self.startXpath).click()