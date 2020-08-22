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




@pytest.mark.usefixtures("get_driver")
class TestSuite1:
#TODO: добавить логгер
    def test_one(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        mainPage.MainPage().startGame()
        gamePage.GamePage().sendCreditals()
        time.sleep(4)


    def test_two(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        mainPage.MainPage().startGame()
        gamePage.GamePage().removeHelp()
        #TODO: добавить проверку того, что хелп уехал

    def test_three(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        mainPage.MainPage().startGame()
        gamePage.GamePage().removeCookie()
        #TODO: добавить проверку того, что форма скрыта


    def test_four(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        mainPage.MainPage().startGame()
        startTime = gamePage.GamePage().checkTimer()
        ExpectedTime = gamePage.GamePage().ExpectedTime
        assert ExpectedTime == startTime, "The countdown does not start from zero"

