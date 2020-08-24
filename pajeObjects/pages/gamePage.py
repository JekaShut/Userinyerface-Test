from framework.utils import ElementOperations
from selenium.webdriver.common.by import By
from pajeObjects.pages.logic.gamePageLogic import Generate
from framework.Base import BaseForm
from framework.common import jsonGetter
from framework.utils import SystemActions
import os
import time

from pathlib import Path
from framework.Browser import *
from framework.logger.logger import Logger
logger = Logger(__file__).getlog()


class GamePage():
    def __init__(self):
        self.File = "\\img.jpg" #TODO: вынести в тестовые данные
        self.cookieButtonXpath = "//div[@class='align__cell']/button"
        self.HideHelpXpath = "//span[@class='discrete']"
        self.TimerXpath = "//div[@class='timer timer--white timer--center']"
        self.ExpectedTime = "00:00:00" #TODO: заменить тестовыми данными
        self.UnselectAll = "//label[@for='interest_unselectall']"
        self.PasswordFieldXpath = "//input[@placeholder='Choose Password']"
        self.EmailFieldXpath = "//input[@placeholder='Your email']"
        self.DomainFieldXpath = "//input[@placeholder='Domain']"
        self.DropDownField = "//div[@class='dropdown__field']"
        self.DropDownelements = "//div[@class='dropdown__list-item']"
        self.Checkbox = "//span[@class='checkbox__box']"
        self.NextXpath = "//div[@class='align__cell button-container__secondary']/a[@class='button--secondary']"
        self.Checkboxes = "//div[@class='avatar-and-interests__interests-list__item']"
        self.NextButton = "//button[@class='button button--stroked button--white button--fluid']"
        self.uploadImage = "//a[@class='avatar-and-interests__upload-button']"
        self.cookiesDiv = "//div[@class='cookies']"

    def removeCookie(self):
        ElementOperations.Button(By.XPATH, self.cookieButtonXpath).click()

    def assertCookie(self):
        #TODO: kak?
        pass

    def removeHelp(self):
        ElementOperations.Button(By.XPATH, self.HideHelpXpath).click()

    def checkTimer(self):
        startTime = ElementOperations.Label(By.XPATH, self.TimerXpath).getText()
        return startTime

    def sendCreditals(self):
        Pass = Generate.string()
        ElementOperations.Input(By.XPATH, self.PasswordFieldXpath).clear()
        ElementOperations.Input(By.XPATH, self.PasswordFieldXpath).send(Pass)

        ElementOperations.Input(By.XPATH, self.EmailFieldXpath).clear()
        ElementOperations.Input(By.XPATH, self.EmailFieldXpath).send(Pass)

        ElementOperations.Input(By.XPATH, self.DomainFieldXpath).clear()
        ElementOperations.Input(By.XPATH, self.DomainFieldXpath).send(Pass)

        ElementOperations.Button(By.XPATH, self.DropDownField).click()
        ElementOperations.DropDown(By.XPATH, self.DropDownelements).random().click()
        ElementOperations.CheckBox(By.XPATH, self.Checkbox).click()
        ElementOperations.Button(By.XPATH, self.NextXpath).click()

    def clickNext(self):
        ElementOperations.Button(By.XPATH, self.NextButton).click()

    def unselectCheckboxes(self):
        ElementOperations.CheckBox(By.XPATH, self.UnselectAll).click()

    def selectRandomCheckbox(self):
        ElementOperations.CheckBox(By.XPATH, self.Checkbox).random().click()

    def uploadimage(self):
        ElementOperations.Button(By.XPATH, self.uploadImage).click()
        SystemActions.SysOperations().upload(self.File)

