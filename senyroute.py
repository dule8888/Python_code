# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:30:54 2018

@author: Ebay15
"""

import pandas as pd
import requests


df = pd.read_excel(r"C:\Users\Ebay15\Desktop\routepy\Bos\bos.xlsx", sheetname='Sheet1')


df['longaddress'] = df.astype(str).apply(lambda x: ' , '.join(x), axis=1)  
  
  
s =''
c = df['longaddress'].values.flatten().tolist()
for i in c:
    s +=  '"'+ str(i) + '"'+","
s = s[:-1]

akey='rGobNjAp6aqgF4Amh3ODmuHZQdr1KDqC'
web = 'http://www.mapquestapi.com/directions/v2/route?key=%s&' % (akey)
choice = 'shortest'
biglist = []

route_pairs = [(c[i],c[j]) for i in range(len(c)) for j in range(i+1, len(c))]

for i in range(len(route_pairs)):
    print(i)
    smalllist = []
    orgin = list(route_pairs[i])[0]
    dest = list(route_pairs[i])[1]
    
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
    print(i, 'is done')

my_list = pd.DataFrame(biglist)
my_list.to_csv(r'C:\Users\Ebay15\Desktop\routepy\Bos\bosOut.csv', index=False, header=False)