from framework.utils import ElementOperations
from selenium.webdriver.common.by import By
from framework.Base.BaseForm import BaseForm
#from framework.Base.BaseForm import Check
from pajeObjects.pages.logic import gamePageLogic
from framework.common import jsonGetter
from framework.utils import SystemActions
from framework.Browser import *
from framework.logger.logger import Logger
logger = Logger(__file__).getlog()


class GamePage(BaseForm):
    def __init__(self):
        self.cookieButtonXpath = "//div[@class='align__cell']/button"
        self.HideHelpXpath = "//span[@class='discrete']"
        self.TimerXpath = "//div[@class='timer timer--white timer--center']"
        self.UnselectAll = "//label[@for='interest_unselectall']"
        self.PasswordFieldXpath = "//input[@placeholder='Choose Password']"
        self.EmailFieldXpath = "//input[@placeholder='Your email']"
        self.DomainFieldXpath = "//input[@placeholder='Domain']"
        self.DropDownField = "//div[@class='dropdown__field']"
        self.DropDownelements = "//div[@class='dropdown__list-item']"
        self.PreCheckboxXpath = "//div[@class='avatar-and-interests__interests-list__item']"
        self.Checkbox = "/div/span/label"
        self.StartCheckBox = "//span[@class='checkbox__box']"
        self.CheckboxClick = ""
        self.CheckboxText = "/div/span[not(@class)]" #ansector::
        self.select = "Select all"
        self.unselect = "Unselect all"
        self.NextXpath = "//div[@class='align__cell button-container__secondary']/a[@class='button--secondary']"
        self.Checkboxes = "//div[@class='avatar-and-interests__interests-list__item']"
        self.NextButton = "//button[@class='button button--stroked button--white button--fluid']"
        self.uploadImage = "//a[@class='avatar-and-interests__upload-button']"
        self.cookiesDiv = "//div[@class='cookies']"
        self.HelpHidden = "//div[@class='help-form is-hidden']"
        self.Pageidentificator = "//div[@class='page-indicator']"
        self.Page1Text = "1 "
        self.Unic2 = "//p[@class='avatar-and-interests__text']"
        self.Unic3 = "//div[@class='personal-details']"
        self.Page2Text = "2 "
        self.Page3Text = "3 "
        self.Page4Text = "4 "


    def checkPage(self):

        text = ElementOperations.Label(By.XPATH, self.Pageidentificator).getText()
        result = gamePageLogic.Logic().GetPageNumber(text)

        return result

    def removeCookie(self):

        elem = ElementOperations.Button(By.XPATH, self.cookieButtonXpath)._find()
        ElementOperations.Button(By.XPATH, self.cookieButtonXpath).click()
        return elem

    def checkCookie(self, elem):

        result = BaseForm(elem).isDisplayed()
        return result

    def removeHelp(self):
        elem = ElementOperations.Button(By.XPATH, self.HideHelpXpath)._find()
        ElementOperations.Button(By.XPATH, self.HideHelpXpath).click()
        return elem

    def checkHelp(self):
        elem = ElementOperations.Form(By.XPATH, self.HelpHidden)._find()
        result = BaseForm(elem).isDisplayed()

        return result

    def checkTimer(self):

        startTime = ElementOperations.Label(By.XPATH, self.TimerXpath).getText()
        return startTime

    def sendCreditalsPassword(self, passwd):
        logger.info("Trying to generate string")

        ElementOperations.Input(By.XPATH, self.PasswordFieldXpath).clear()
        ElementOperations.Input(By.XPATH, self.PasswordFieldXpath).send(passwd)

    def sendCreditalsEmail(self, passwd):
        ElementOperations.Input(By.XPATH, self.EmailFieldXpath).clear()
        ElementOperations.Input(By.XPATH, self.EmailFieldXpath).send(passwd)

    def sendCreditalsDomain(self, passwd):
        ElementOperations.Input(By.XPATH, self.DomainFieldXpath).clear()
        ElementOperations.Input(By.XPATH, self.DomainFieldXpath).send(passwd)

    def sendCreditalsDropDown(self):
        ElementOperations.Button(By.XPATH, self.DropDownField).click()
        ElementOperations.DropDown(By.XPATH, self.DropDownelements).random().click()
        ElementOperations.CheckBox(By.XPATH, self.StartCheckBox).click()
        ElementOperations.Button(By.XPATH, self.NextXpath).click()

    def clickNext(self):
        logger.info("Trying to click NEXT button")
        ElementOperations.Button(By.XPATH, self.NextButton).click()

    def unselectCheckboxes(self):
        logger.info("Trying to click unselect all button")
        ElementOperations.CheckBox(By.XPATH, self.UnselectAll).click()

    def getCheckboxText(self, locatorType, locator, elem):
        text = ElementOperations.CheckBox(locatorType, locator, elem).getText()
        return text

    def findRandomCheckbox(self, x):
        elem = ElementOperations.CheckBox(By.XPATH, self.CheckboxClick, x).random()
        return elem

    def selectRandomCheckbox(self, num):
        logger.info("Trying to select a random checkbox")
        path = self.PreCheckboxXpath + self.Checkbox
        pathtext = self.PreCheckboxXpath + self.CheckboxText
        elems = ElementOperations.CheckBox(By.XPATH, path)._finds()
        x = gamePageLogic.Logic().ReturnValidCheckboxes(pathtext, elems, self.select, self.unselect)
        x = gamePageLogic.Logic().ClickCheckboxes(x, num)
        elem = ElementOperations.CheckBox(By.XPATH, self.CheckboxClick, x).random().click()

    def uploadimage(self, img):
        logger.info("Trying to upload an image")
        ElementOperations.Button(By.XPATH, self.uploadImage).click()
        SystemActions.SysOperations().upload(img)

    def wait2page(self):
        ElementOperations.Label(By.XPATH, self.Unic2)._find()

    def wait3page(self):
        ElementOperations.Label(By.XPATH, self.Unic3)._find()


