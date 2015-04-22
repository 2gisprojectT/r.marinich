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
        driver.find_element_by_name("login").send_keys("login")
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_css_selector("input.form_b").click()

        self.assertEqual('Не удалось войти.', driver.find_element_by_xpath("//*").get_attribute("outerHTML")[42:59])
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
