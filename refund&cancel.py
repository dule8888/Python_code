# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 17:29:16 2017

@author: Ebaycs
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from lxml import html
import time
from selenium.webdriver.support.ui import Select

#change date
order=[577602,577933,577848,577749,577728,577800,577744,577854,577645,577579,577890,577946,577713,577714,577633,577909,577695,577603,577689,577820,577735,577952,577871,577754,577587,577662,577601,577609,577880,577925,577885,577760,577758,577887,577605,577787,577582,577701,577688,577908,577628,577768,577584,577718,577898,577593,577687,577876,577592,577635,577791,577646,577620,577784,577947,577756,577636,577945,577846]
price=[]
driver = webdriver.Chrome(executable_path=r'C:\Users\Ebay15\Desktop\chromedriver_win32\chromedriver.exe')
driver.get('http://k2b-bulk.ebay.com/ws/eBayISAPI.dll?SalesRecordConsole&status=WaitShipment&currentPage=SCSold&ssPageName=STRK:ME:LNLK')
time.sleep(5)
#change username and password here
driver.find_element_by_xpath(".//input[@id='userid']").send_keys("auto_lighthouse")#autobodypartsexpress
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
    treee=html.fromstring(driver.page_source)
    if treee.xpath('//span[@class="caHdr-sts"]/text()')[0] == "0":
        price.append((i,"do not found"))
        continue
    driver.find_element_by_id("165:0").click()
    try:
        driver.find_element_by_css_selector("#v4-46_anc > b").click()
    except:
        time.sleep(2)
        driver.find_element_by_css_selector("#v4-46_anc > b").click()
    driver.find_element_by_id("v4-47_mu_js_an_2").click()
    try:
        driver.find_element_by_xpath("//textarea[contains(@id,'v4-IT')]").clear()
    except:
        time.sleep(2)
        driver.find_element_by_xpath("//textarea[contains(@id,'v4-IT')]").clear()
        pass
    driver.find_element_by_xpath("//textarea[contains(@id,'v4-IT')]").send_keys("1/22: Shipping Zip Code -JW")
    driver.find_element_by_id("but_v4-65").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        driver.find_element_by_css_selector("span[name=\"ddmCtl\"]").click()
    except:
        time.sleep(2)
        driver.find_element_by_css_selector("span[name=\"ddmCtl\"]").click()
        pass
    driver.find_element_by_link_text("Cancel order").click()
    time.sleep(3)
    tree=html.fromstring(driver.page_source)
    price.append((i,tree.xpath('//div[@class="itmprc"]/text()')))
    
    driver.find_element_by_id("btn_cancelReason").click()
    driver.find_element_by_id("cancelReason_1").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_id("sellerRefundOlay").click()
    time.sleep(1)
    
    driver.find_element_by_id("rfdBtn").click()
    time.sleep(3)
    if re.search('success',driver.current_url) is not None:
        price.append((i,"success"))
    else:
        price.append((i,"fail"))
    print(i)
    print(price)
    
    
    
    
