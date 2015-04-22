# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class PythonSiteUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.lostfilm.tv/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_python_site_unit(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_name("login").click()
        driver.find_element_by_name("login").send_keys("g1645514@trbvm.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("g1645514@trbvm.comg1645514@trbvm.com")
        driver.find_element_by_css_selector("input.form_b").click()
        driver.find_element_by_xpath("//div[@id='Onwrapper']/div[3]/div[2]/div[2]/a[29]").click()
        driver.find_element_by_xpath("//a[@onclick=\"ShowAllReleases('51','1','99');return false;\"]").click()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

if __name__ == "__main__":
    unittest.main()
