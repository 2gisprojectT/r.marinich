# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import easygui

class PythonSiteUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.lostfilm.tv/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxserials = 187

    def test_python_site_unit(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Остальные сериалы...").click()

        i=1
        while(i<self.maxserials):
            a = driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div[4]/div[1]/div[1]/div[2]/a[" + str(i) + "]")
            print(a[0].text)
            i+=1
        #easygui.msgbox("a :=" + a[0].text + "; b :=" + b[0].text, title="simple gui")

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

    def tearDown(self):
        print("ok.")
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
