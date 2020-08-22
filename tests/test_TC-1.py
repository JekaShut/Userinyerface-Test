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

    #def test_one(self):
    #    logger.info("Trying to open site " + SITE)
    #    LinkOperations(SITE).get()
    #    mainPage.MainPage().startGame()
#
#
    def test_two(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        mainPage.MainPage().startGame()
        gamePage.GamePage().removeHelp()

    def test_three(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        mainPage.MainPage().startGame()
        gamePage.GamePage().removeCookie()


    def test_four(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        mainPage.MainPage().startGame()


