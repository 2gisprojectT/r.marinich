from dashboard import Dashboard

class Page():
    def __init__(self, driver, login=None, password=None):
        self.driver = driver
        self.driver.implicitly_wait(5)

        self._login = login
        self._password = password

        self._dashboard = None

    def open(self, url):
        self.driver.get(url)
        return self

    def setLogin(self, login):
        self._login = login
        return self

    def setPassword(self, password):
        self._password = password
        return self

    def input(self):
        if self._login is None or self._password is None:
            return None
        if self._dashboard is None:
            self._dashboard = Dashboard(self.driver)
        self._dashboard.input(self._login, self._password)
        return self

    def getDashboardLink(self):
        if self._dashboard is None:
            return None
        return self._dashboard.getDashboardLink()

    def getHtmlPage(self):
        if self._dashboard is None:
            return None
        return self._dashboard.getHtmlPage()