from framework.common import jsonGetter
from framework.logger.logger import Logger
from framework.utils import CookieOperations
from framework.utils.BrowserActions import LinkOperations
from pajeObjects.pages import javascriptPage
import time
import pytest


CONFIG = 'resources/config.json'


logger = Logger(logger="TC-1").getlog()


SITE = jsonGetter.GetJson.getFile(CONFIG, "SITE")




@pytest.mark.usefixtures("get_driver")
class TestSuite1:

    def test_one(self):
        logger.info("Trying to open site " + SITE)
        LinkOperations(SITE).get()
        







