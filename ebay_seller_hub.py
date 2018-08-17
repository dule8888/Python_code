from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup as bs
import time

driver = webdriver.Firefox(executable_path=r'C:\Users\Ebaycs\Desktop\geckodriver.exe')
driver.get('http://www.ebay.com/sh/prf/traffic')


driver.find_element_by_xpath(".//*[@id='pri_signin']/div[4]/span[2]/input").send_keys("auto_lighthouse")
driver.find_element_by_xpath("(//input[@placeholder='Password'])[1]").send_keys("twofor1deal")
driver.find_element_by_xpath('(//input[@id="sgnBt"])[1]').click()
time.sleep(5)


for i in range(3):
    next=driver.find_element_by_xpath('//a[@rel="next"]')
    try:
        next.click()
        time.sleep(5)
        soup=bs(driver.page_source,'lxml')
        a=soup.find_all('tr',{'id':re.compile('gridRowId.*')})
        for i in a:
            for j in i.find_all('p'):
                print(j.text)
    except:
        break


