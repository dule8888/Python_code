# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:24:55 2018

@author: Ebay15
"""

import pandas as pd
import requests

df = pd.read_excel(r"C:\Users\Ebay15\Desktop\routepy\Bos\bosOut1.xlsx", sheetname='Sheet5')

akey='rGobNjAp6aqgF4Amh3ODmuHZQdr1KDqC'
web = 'http://www.mapquestapi.com/directions/v2/route?key=%s&' % (akey)
choice = 'shortest'
biglist = []

for index, row in df.iterrows():
    print(row[0], row[1])

    smalllist = []
    orgin = row[0]
    dest = row[1]
    
    parameter = 'from=%s&to=%s&routeType=%s' % (orgin,dest,choice)
    request = web + parameter
    print(request)
    
    response =requests.get(request).json()
    g = response['route']['distance']
    h = response['route']['formattedTime']
    print(g)
    print(h)
    smalllist.append(orgin)
    smalllist.append(dest)
    smalllist.append(g)    
    smalllist.append(h)     
    biglist.append(smalllist)
    print(index, 'is done')

my_list = pd.DataFrame(biglist)
my_list.to_csv(r'C:\Users\Ebay15\Desktop\routepy\Bos\bosResult.csv', index=False, header=False)