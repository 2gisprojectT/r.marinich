from selenium import webdriver
import unittest

class PythonSiteUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.lostfilm.tv/"
    
    def test_python_site_unit(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element_by_name("login").click()
        driver.find_element_by_name("login").send_keys("g1645514@trbvm.com")
        driver.find_element_by_name("password").send_keys("g1645514@trbvm.comg1645514@trbvm.com")
        driver.find_element_by_css_selector("input.form_b").click()

        self.assertEqual('http://www.lostfilm.tv/my.php', self.driver.find_element_by_class_name('prof').find_element_by_class_name('user_menu_link').get_attribute('href'))
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()