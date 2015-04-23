from unittest import TestCase
from selenium import webdriver
from page import Page

class SeleniumWithPage(TestCase):
    def setUp(self):
        # driver = webdriver.Remote(
        # command_executor = 'http://localhost:9515',
        # desired_capabilities={
        # "browserName" : 'chrome'
        # })
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open("http://www.lostfilm.tv")

    def test_DashboardLink(self):
        self.page.setLogin("g1645514@trbvm.com").setPassword("g1645514@trbvm.comg1645514@trbvm.com").input()
        self.assertEqual("http://www.lostfilm.tv/my.php", self.page.getDashboardLink())

    def test_errorParams(self):
        self.page.setLogin("123").setPassword("123").input()
        self.assertEqual("Не удалось войти. Возможно не правильный логин/пароль", self.page.getHtmlPage())

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()