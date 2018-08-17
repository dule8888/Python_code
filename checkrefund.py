# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:07:49 2018

@author: ldu
"""

from selenium import webdriver

import time

import pandas as pd


df = pd.read_csv(r'C:\Users\ldu\Desktop\refundcheck\refundlist.csv')

refundlist = df['so'].tolist()

newlist = []

driver = webdriver.Chrome(executable_path=r'C:\Users\ldu\Desktop\refund\chromedriver.exe')
driver.get('https://k2b-bulk.ebay.com/ws/eBayISAPI.dll?SalesRecordConsole&currentpage=SCSold&ssPageName=STRK:ME:LNLK')
time.sleep(5)
driver.find_element_by_xpath(".//*[@id='pri_signin']/div[3]/span[2]/input").send_keys("auto_lighthouse")#autobodypartsexpress
driver.find_element_by_xpath("(//input[@placeholder='Password'])[1]").send_keys("twofor1deal")
time.sleep(2)
driver.find_element_by_xpath('(//input[@id="sgnBt"])[1]').click()
time.sleep(5)
driver.find_element_by_xpath(".//*[@id='searchField']").click()
driver.find_element_by_xpath(".//*[@value='SalesRecordNumber']").click()
time.sleep(2)
i = 0
for item in refundlist:
    i = i+1
    shortlist = []
    driver.find_element_by_xpath(".//*[@id='searchValues']").send_keys("%s" %item)
    driver.find_element_by_xpath(".//*[@id='searchbutton']").click()
    time.sleep(1)
    try:
        text = driver.find_element_by_xpath(".//*[@style='white-space:normal']").text
        date = driver.find_element_by_xpath(".//*[@id='SaleDate']/span[1]").text

        print(i, 'is done')
    except:
        text = "No comment"
        date = driver.find_element_by_xpath(".//*[@id='SaleDate']/span[1]").text
        print(i, 'no comment is done')
        pass
    shortlist.append(item)
    shortlist.append(text)
    shortlist.append(date)
    newlist.append(shortlist) 
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='searchValues']").clear()