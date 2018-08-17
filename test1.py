# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://sell.terapeak.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self):
        driver = self.driver
        driver.get(self.base_url + "/product-research?buyerCountryCodes&categoryId=33640&endDate=1499529599999&fromPrice&keywords=bumper&listingConditions=&listingTypes=&productIdentifier&sellerCountryCodes=US&site=motors.ebay.com&startDate=1496937600000&toPrice&transactionSite")
        driver.find_element_by_xpath("//div[@id='terapeak-app']/div/div/div/div/div/div/div/div/span[2]").click()
        driver.find_element_by_xpath("(//button[@id='dropdownButton'])[3]").click()
        driver.find_element_by_xpath("//div[@id='terapeak-app']/div/div/div/div/div/div/div[6]/div/div/div[2]/div[4]/div/div[2]/div/div/ul/li[2]/a/span[2]/span/span[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[11]").click()
        driver.find_element_by_css_selector("div.input-box > div.form-group > input.form-control").clear()
        driver.find_element_by_css_selector("div.input-box > div.form-group > input.form-control").send_keys("33640")
        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
    
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
