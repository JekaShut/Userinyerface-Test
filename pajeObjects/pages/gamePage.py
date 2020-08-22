from framework.utils import ElementOperations
from selenium.webdriver.common.by import By

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()


class GamePage:
    def __init__(self):
        self.cookieButtonXpath = "//div[@class='align__cell']/button"
        self.HideHelpXpath = "//span[@class='discrete']"
        self.TimerXpath = "//div[@class='timer timer--white timer--center']"
        self.ExpectedTime = "00:00:00"
        self.UnselectAll = "//label[@for='interest_unselectall']"
        self.Pass = "6XD8io2LQLvTF4h8" #10 symb, 1UP, 1Num,
        self.PasswordFieldXpath = "//input[@placeholder='Choose Password']"
        self.EmailFieldXpath = "//input[@placeholder='Your email']"
        self.DomainFieldXpath = "//input[@placeholder='Domain']"
        self.DropDownField = "//div[@class='dropdown__field']"
        self.DropDownElements = ""

    def removeCookie(self):
        ElementOperations.Button(By.XPATH, self.cookieButtonXpath).click()

    def removeHelp(self):
        ElementOperations.Button(By.XPATH, self.HideHelpXpath).click()

    def checkTimer(self):
        startTime = ElementOperations.Label(By.XPATH, self.TimerXpath).getText()
        return startTime

    def sendCreditals(self):
        ElementOperations.Input(By.XPATH, self.PasswordFieldXpath).clear()
        ElementOperations.Input(By.XPATH, self.PasswordFieldXpath).send(self.Pass)
        ElementOperations.Input(By.XPATH, self.EmailFieldXpath).clear()
        ElementOperations.Input(By.XPATH, self.PasswordFieldXpath).send(self.Pass)
        ElementOperations.Input(By.XPATH, self.DomainFieldXpath).clear()
        ElementOperations.Input(By.XPATH, self.PasswordFieldXpath).send(self.Pass)
        ElementOperations.Button(By.XPATH, self.DropDownField).click()
        elements = ElementOperations.Button(By.XPATH, self).finds()
        elements[2].click()

