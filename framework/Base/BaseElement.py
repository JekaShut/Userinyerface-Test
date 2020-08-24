from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

from framework.Browser import *
from abc import ABC

WaitTime = jsonGetter.GetJson.getFile(CONFIG, "WaitTime")


class BaseElement(ABC):

    def __init__(self, locatorType, locator, elem=""):
        self.locatorType = locatorType
        self.locator = locator
        self.driver = RunBrowser().driver
        self.element = elem


    def _find(self, WaitTime = WaitTime):
        '''
        :param WaitTime: time in seconds while the driver will try to find an element
        :return: element
        '''
        wait = WebDriverWait(self.driver, WaitTime)

        try:
            logger.info("Waiting for element" + self.locator)
            wait.until(EC.presence_of_element_located((self.locatorType, self.locator)))
        except TimeoutException:
            logger.warn("Cannot find such an element!" + self.locator)
        if self.element == "":
            self.element = self.driver.find_element(self.locatorType, self.locator)
        if self.element != "":
            self.element = self.element.find_element(self.locatorType, self.locator)
        return self.element


    def _finds(self, WaitTime = WaitTime):
        '''
        :param WaitTime: time in seconds while the driver will try to find an element
        :return: Many elements
        '''
        wait = WebDriverWait(self.driver, WaitTime)
        try:
            logger.info("Waiting for element" + self.locator)
            wait.until(EC.presence_of_element_located((self.locatorType, self.locator)))
        except TimeoutException:
            logger.warn("Cannot find such an element!" + self.locator)
        if self.element == "":
            self.elements = self.driver.find_elements(self.locatorType, self.locator)
        if self.element != "":
            self.elements = self.element.find_elements(self.locatorType, self.locator)
        return self.elements

    def click(self):
        '''
        :return: nothing
        Find and click to element
        '''
        self._find()
        self.element.click()


    def move(self):
        '''
        Moves mouse to an element
        '''
        self._find()
        hov = ActionChains(self.driver).move_to_element((self.element)).perform()


