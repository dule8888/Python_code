# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:24:01 2017

@author: Ebaycs
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

status=[577848,577632,577640,577720,577632,577602,577933,577848,577749,577728,577800,577744,577854,577645,577579,577890,577946,577713,577714,577633,577909,577695,577603,577689,577820,577735,577952,577871,577754,577587,577662,577601,577609,577880,577925,577885,577760,577758,577887,577605,577787,577582,577701,577688,577908,577628,577768,577584,577718,577898,577593,577687,577876,577592,577635,577791,577646,577620,577784,577947,577756,577636,577945,577846]
#
order=[577603,577689,577820,577735,577952,577871,577754,577587,577662,577601,577609,577880,577925,577885,577760,577758,577887,577605,577787,577582,577701,577688,577908,577628,577768,577584,577718,577898,577593,577687,577876,577592,577635,577791,577646,577620,577784,577947,577756,577636,577945,577846]
driver = webdriver.Chrome(executable_path=r'C:\Users\Ebay15\Desktop\chromedriver_win32\chromedriver.exe')

driver.get('http://k2b-bulk.ebay.com/ws/eBayISAPI.dll?SalesRecordConsole&status=WaitShipment&currentPage=SCSold&ssPageName=STRK:ME:LNLK')
driver.find_element_by_xpath(".//input[@id='userid']").send_keys("auto_lighthouse")
driver.find_element_by_xpath("(//input[@placeholder='Password'])[1]").send_keys("twofor1deal")
driver.find_element_by_xpath('(//input[@id="sgnBt"])[1]').click()
time.sleep(6)
for i in order:
    driver.get('http://k2b-bulk.ebay.com/ws/eBayISAPI.dll?SalesRecordConsole&status=WaitShipment&currentPage=SCSold&ssPageName=STRK:ME:LNLK')
    time.sleep(3)
    Select(driver.find_element_by_id("searchField")).select_by_visible_text("Sales record number")
    driver.find_element_by_id("searchValues").clear()
    driver.find_element_by_id("searchValues").send_keys(str(i))
    driver.find_element_by_id("searchbutton").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[@name='ddmCtl']").click()
    #element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact buyer")))
    #element.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_link_text("Contact buyer").click()
    time.sleep(3)
    try:
        driver.find_element_by_id("msg_cnt_cnt").clear()
    except:
        time.sleep(1)
        status.append((i,'fail'))
        continue     
    driver.find_element_by_id("msg_cnt_cnt").send_keys("Due to recent changes in our shipping options, we are only able to ship to specific zip codes in the US, and yours does not fall in that range. We sincerely apologize for any inconvenience this may have caused you! We have canceled your order and processed the refund via PayPal. You should receive the funds back in your account within 3-5 business days.  Again, we truly apologize! ")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_id("sendBtn").click()
    time.sleep(1)
    print(i)
