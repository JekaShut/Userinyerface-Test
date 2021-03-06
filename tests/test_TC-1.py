from framework.common import jsonGetter
from framework.utils import CookieOperations
from framework.utils.BrowserActions import LinkOperations
from pajeObjects.pages import mainPage, gamePage
from pajeObjects.pages.logic.gamePageLogic import Logic
from pytest_testrail.plugin import pytestrail
import pytest

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

CONFIG = 'resources/config.json'
TESTDATA = 'resources/testdata.json'

SITE = jsonGetter.GetJson.getFile(CONFIG, "SITE")
testdata1 = jsonGetter.GetJson.getFile(TESTDATA, "testdata1")
testdata2 = jsonGetter.GetJson.getFile(TESTDATA, "testdata2")

GP = gamePage.GamePage()
MP = mainPage.MainPage()

@pytest.mark.usefixtures("get_driver")
class TestSuite1:
    @pytestrail.case('C19380774')
    @pytest.mark.parametrize("img", testdata1)
    def test_one(self, img):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = MP.getText()
        EXtext = MP.EXtext
        assert text == EXtext, "This is not expected page"

        MP.startGame()
        page = GP.checkPage()
        pageOne = GP.Page1Text
        assert page == pageOne, "This is not expected page"
        passwd = Logic.generate_string()
        GP.sendCreditalsPassword(passwd)
        GP.sendCreditalsEmail(passwd)
        GP.sendCreditalsDomain(passwd)
        GP.sendCreditalsDropDown()
        GP.clickNext()

        GP.wait2page()
        pageTwo = GP.Page2Text
        page = GP.checkPage()
        assert page == pageTwo, "This is not expected page"
        GP.uploadimage(img)
        GP.unselectCheckboxes()
        GP.selectRandomCheckbox(3)
        GP.clickNext()

        GP.wait3page()
        pageThree = GP.Page3Text
        page = GP.checkPage()
        assert page == pageThree, "This is not expected page"

    @pytestrail.case('C19380775')
    def test_two(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = MP.getText()
        EXtext = MP.EXtext
        assert text == EXtext, "This is not expected page"
        MP.startGame()
        GP.removeHelp()
        result = GP.checkHelp()
        assert result == True, "Form is not hidden"

    @pytestrail.case('C19380776')
    def test_three(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = MP.getText()
        EXtext = MP.EXtext
        assert text == EXtext, "This is not expected page"
        MP.startGame()
        elem = GP.removeCookie()
        result = GP.checkCookie(elem)
        assert result == False, "Cookie banner has not been closed"

    @pytestrail.case('C19380777')
    @pytest.mark.parametrize("time", testdata2)
    def test_four(self, time):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        text = MP.getText()
        EXtext = MP.EXtext
        assert text == EXtext, "This is not expected page"
        MP.startGame()
        startTime = GP.checkTimer()
        assert time == startTime, "The countdown does not start from zero"

