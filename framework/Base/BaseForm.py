from framework.logger.logger import Logger

logger = Logger(logger="JavascriptPage").getlog()


class BaseForm:
    def __init__(self, locatorType= "", locator= "", pageName= ""):
        self.locatorType = locatorType
        self.locator = locator
        self.pageName = pageName
