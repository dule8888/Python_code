from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r'C:\Users\Ebaycs\Desktop\geckodriver.exe')
driver.get('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&UsingSSL=1&siteid=0&co_partnerId=2&pageType=2332524&ru=http%3A%2F%2Fwww.ebay.com%2Fsh%2Fprf%2Ftraffic')


driver.find_element_by_xpath(".//*[@id='pri_signin']/div[4]/span[2]/input").send_keys("auto_lighthouse")
driver.find_element_by_xpath("(//input[@placeholder='Password'])[1]").send_keys("twofor1deal")
driver.find_element_by_xpath('(//input[@id="sgnBt"])[1]').click()
driver.implicitly_wait(10)
soup=bs(driver.page_source)
a=soup.find_all('tr',{'id':re.compile('gridRowId.*')})
data=[]
for i in a:
    for j in i.find_all('p'):
        print(j.text)