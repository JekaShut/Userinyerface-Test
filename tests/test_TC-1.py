from framework.common import jsonGetter
from framework.utils import CookieOperations
from framework.utils.BrowserActions import LinkOperations
from pajeObjects.pages import mainPage, gamePage
from pajeObjects.pages.logic.gamePageLogic import Generate

import pytest

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

CONFIG = 'resources/config.json'

SITE = jsonGetter.GetJson.getFile(CONFIG, "SITE")




@pytest.mark.usefixtures("get_driver")
class TestSuite1:


    def test_one(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = mainPage.MainPage().assertPage()
        EXtext = mainPage.MainPage().EXtext
        assert text == EXtext, "This is not expected page"

        mainPage.MainPage().startGame()
        page = gamePage.GamePage().checkPage()
        pageOne = gamePage.GamePage().Page1Text
        assert page == pageOne, "This is not expected page"
        passwd = Generate.string()
        gamePage.GamePage().sendCreditals(passwd)
        gamePage.GamePage().clickNext()

        gamePage.GamePage().wait2page()
        pageTwo = gamePage.GamePage().Page2Text
        page = gamePage.GamePage().checkPage()
        assert page == pageTwo, "This is not expected page"
        gamePage.GamePage().uploadimage()
        gamePage.GamePage().unselectCheckboxes()
        gamePage.GamePage().selectRandomCheckbox()
        gamePage.GamePage().selectRandomCheckbox()
        gamePage.GamePage().selectRandomCheckbox()
        gamePage.GamePage().clickNext()

        gamePage.GamePage().wait3page()
        pageThree = gamePage.GamePage().Page3Text
        page = gamePage.GamePage().checkPage()
        assert page == pageThree, "This is not expected page"



    def test_two(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = mainPage.MainPage().assertPage()
        EXtext = mainPage.MainPage().EXtext
        assert text == EXtext, "This is not expected page"
        mainPage.MainPage().startGame()
        gamePage.GamePage().removeHelp()
        result = gamePage.GamePage().checkHelp()
        assert result == True, "Form is not hidden"


    def test_three(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = mainPage.MainPage().assertPage()
        EXtext = mainPage.MainPage().EXtext
        assert text == EXtext, "This is not expected page"
        mainPage.MainPage().startGame()
        elem = gamePage.GamePage().removeCookie()
        result = gamePage.GamePage().checkCookie(elem)
        assert result == False, "Cookie banner has not been closed"



    def test_four(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = mainPage.MainPage().assertPage()
        EXtext = mainPage.MainPage().EXtext
        assert text == EXtext, "This is not expected page"
        mainPage.MainPage().startGame()
        startTime = gamePage.GamePage().checkTimer()
        ExpectedTime = gamePage.GamePage().ExpectedTime
        assert ExpectedTime == startTime, "The countdown does not start from zero"

