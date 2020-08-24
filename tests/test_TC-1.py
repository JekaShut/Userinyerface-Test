from framework.common import jsonGetter
from framework.utils import CookieOperations
from framework.utils.BrowserActions import LinkOperations
from pajeObjects.pages import mainPage, gamePage
import time

import pytest

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

CONFIG = 'resources/config.json'

SITE = jsonGetter.GetJson.getFile(CONFIG, "SITE")

#TODO: Как найти что-нибудь в уже найденном элементе



@pytest.mark.usefixtures("get_driver")
class TestSuite1:
#TODO: добавить логгер
    # TODO: 1 assert ready
    def test_one(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = mainPage.MainPage().assertPage()
        assert text == "HERE", "This is not expected page" #TODO: hardcode
        mainPage.MainPage().startGame()
        gamePage.GamePage().sendCreditals()
        gamePage.GamePage().clickNext()

        gamePage.GamePage().uploadimage()
        gamePage.GamePage().unselectCheckboxes()
        gamePage.GamePage().selectRandomCheckbox()
        gamePage.GamePage().selectRandomCheckbox()
        gamePage.GamePage().selectRandomCheckbox()
        gamePage.GamePage().clickNext()

        time.sleep(4)

    # TODO: 1 assert ready
    def test_two(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = mainPage.MainPage().assertPage()
        assert text == "HERE", "This is not expected page"  # TODO: hardcode
        mainPage.MainPage().startGame()
        gamePage.GamePage().removeHelp()
        #TODO: добавить проверку того, что хелп уехал

    # TODO: 1 assert ready
    def test_three(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = mainPage.MainPage().assertPage()
        assert text == "HERE", "This is not expected page"  # TODO: hardcode
        mainPage.MainPage().startGame()
        gamePage.GamePage().removeCookie()
        #TODO: добавить проверку того, что форма скрыта

    #TODO: asserts ready
    def test_four(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = mainPage.MainPage().assertPage()
        assert text == "HERE", "This is not expected page"  # TODO: hardcode
        mainPage.MainPage().startGame()
        startTime = gamePage.GamePage().checkTimer()
        ExpectedTime = gamePage.GamePage().ExpectedTime
        assert ExpectedTime == startTime, "The countdown does not start from zero"

