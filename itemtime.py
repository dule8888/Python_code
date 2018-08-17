# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:46:17 2017

@author: Ebay15
"""

import requests
from bs4 import BeautifulSoup as bs
import re
import urllib.parse
import xlrd
import xlwt
from xlrd import open_workbook

wb = open_workbook('C:\\Users\\Ebay15\\Desktop\\Searchrank\\itemidtest.xlsx')
for s in wb.sheets():
    #print 'Sheet:',s.name
    values = []
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
        values.append(col_value)

itemid = []
for sublist in values:
    for item in sublist:
        itemid.append(item)
        
base='http://www.ebay.com/itm/'
pagelink_list=[]
for i in itemid:
    url = urllib.parse.urljoin('http://www.ebay.com/itm/', i)
    pagelink_list.append(url)
     
def get_date(pagelink_list):
    listinfo = []
    base='http://www.ebay.com/itm/'
    for i in itemid:
        iteminfo=[]
        url = urllib.parse.urljoin('http://www.ebay.com/itm/', i)
        res=requests.get(url=url)
        soup=bs(res.content,'html.parser')
        iteminfo.append(i)
        try:
            date = soup.find('strong',class_='sh_med_fron vi-acc-del-range').text
        except: pass
        iteminfo.append(date)
        listinfo.append(iteminfo)
    return listinfo

a = get_date(pagelink_list)

book = xlwt.Workbook()
sheet = book.add_sheet("Sheet 1")

for i, l in enumerate(a):
    for j, col in enumerate(l):
        sheet.write(i, j, col)
        
book.save("C:\\Users\\Ebay15\\Desktop\\Searchrank\\itemtime.xls")

