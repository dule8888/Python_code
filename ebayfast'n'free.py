# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:50:01 2017

@author: Ebay15
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
except AttributeError as e:
        return None
    return title

if title == None:
    print("Title could not be found")
else:
    print(title)
    
bsObj.findAll("table")[4].findAll("tr")[2].find("td").findAll("div")[1].find("a")