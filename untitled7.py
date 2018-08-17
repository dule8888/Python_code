# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:20:15 2017

@author: Ebay15
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:07:59 2017

@author: Ebay15
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.ebay.com/sh/ovw')
time.sleep(4) # Let the user actually see something!
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
time.sleep(4)
driver.find_element_by_xpath("(//input[@placeholder='Email or username'])").send_keys("autobodypartsexpress")
driver.find_element_by_xpath("(//input[@placeholder='Password'])").send_keys("twofor1deal")
driver.find_element_by_xpath('(//input[@id="sgnBt"])').click()
time.sleep(3)
driver.find_element_by_xpath('(//a[@href="http://k2b-bulk.ebay.com/ws/eBayISAPI.dll?ListingConsole&currentPage=LCActive"])').click()
time.sleep(3)

for i in range(2,134):
    try:
        driver.find_element_by_xpath('(//a[text()="%d"])' %(i)).click()
    except:
        pass
    
    time.sleep(15)
    try:
        driver.find_element_by_xpath('(//input[@title="Select all items"])').click()
    except:
        pass
        driver.find_element_by_xpath('(//input[@title="Select all items"])').click()
        time.sleep(5)
    time.sleep(5)
    
        #driver.find_element_by_xpath('(//input[@value="332372480403"])').click()  
       # driver.find_element_by_xpath('(//input[@value="302444381644"])').click() 
        #driver.find_element_by_xpath("/html/body[@id='body']/div[@id='v4-114']/div[@id='v4-114olp-pad']/div[@class='ov-c1']/div[@class='ov-c2']/div[@id='cntwv4-114']/div[@id='cnv4-114']/div/div/div[@id='v4-112_mu']/ul[@id='v4-112_mu_js']/li[1]/a[@id='v4-112_mu_41_anch']").click()
        #Select(driver.find_element_by_id("searchField")).select_by_visible_text("Sales record number")
    driver.find_element_by_xpath("//*[@id='v4-111_anc']").click()
    time.sleep(5)
        
    actions = ActionChains(driver)
    for _ in range(1):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
    time.sleep(10)    
    driver.find_element_by_xpath("/html/body[@id='body']/div[@id='v4-114']/div[@id='v4-114olp-pad']/div[@class='ov-c1']/div[@class='ov-c2']/div[@id='cntwv4-114']/div[@id='cnv4-114']/div/div/div[@id='v4-112_mu']/ul[@id='v4-112_mu_js']/li[1]/a[@id='v4-112_mu_41_anch']").click()
    time.sleep(15)
    
    if i >1:

        driver.find_element_by_xpath('(//input[@id="chkAll"])').click()
        time.sleep(15)
       
    else:
        driver.find_element_by_xpath('(//input[@id="listingNewRadio"])').click()
        time.sleep(10)
        driver.find_element_by_xpath('(//input[@name="okButton"])').click()
        time.sleep(20)
        driver.find_element_by_xpath('(//input[@id="chkAll"])').click()
        time.sleep(10)
    driver.find_element_by_xpath("/html/body[@id='body']/div[@class='pagewidth']/div[@class='pageminwidth']/div[@class='pagelayout']/div[@class='pagecontainer']/div[@id='CentralArea']/div[@class='bp']/div[@id='pageWrapper']/div[@class='dtPadding']/div[@class='mainwrap']/div/div[@class='hdbtns']/span[@id='v4-11']/a[@id='link_wsEditMenuDrpDwnId_me']").click()
    time.sleep(5)
    driver.find_element_by_xpath('(//a[text()="Item description"])').click()
    time.sleep(5)
    Select(driver.find_element_by_id("edt_drpDwn")).select_by_visible_text("Edit listings in bulk - find and replace")
    time.sleep(10)
    driver.find_element_by_xpath("(//textarea[@id='replace_desc_find_txtArea'])").clear()
    driver.find_element_by_xpath("(//textarea[@id='replace_desc_find_txtArea'])").send_keys("http")
    time.sleep(2)
    driver.find_element_by_xpath("(//textarea[@name='descriptionreplace'])").clear()
    driver.find_element_by_xpath("(//textarea[@name='descriptionreplace'])").send_keys("https")
    time.sleep(2)
    driver.find_element_by_xpath("(//input[@id='but_editolp_saveCloseBtn'])").click()
    time.sleep(20)
    driver.find_element_by_xpath("(//input[@value='Submit changes'])").click()
    time.sleep(15)
    driver.find_element_by_xpath("(//input[@id='but_confirmSubmitBtn'])").click()
    time.sleep(30)
    try:
        driver.find_element_by_xpath("(//input[@id='but_finishId'])").click()
    except:
        pass
        time.sleep(15)
        driver.find_element_by_xpath("(//input[@id='but_finishId'])").click()

    print("%d is done" %(i *200))
    time.sleep(15)
    







