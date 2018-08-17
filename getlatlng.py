# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:29:02 2018

@author: Ebay15
"""



import pandas as pd
import requests


df = pd.read_excel(r'C:\Users\Ebay15\Desktop\itemlastmonthsold\lastmonthorder.xlsx',sheetname='allpivot')
api_key='AIzaSyDIT-zhkVglFp2ps3ZnyQCwzRQEmTW7Vb8'
web = 'https://maps.googleapis.com/maps/api/geocode/json?'
lista = []



for i in range(0,len(df)):
    smalllist=[]
    address = '%s' % (df['address'].iloc[i])
    nav_request = 'address={}&key={}'.format(address,api_key)
    request = web + nav_request
    print(request)
    response =requests.get(request).json()
    smalllist.append(response['results'][0]['geometry']['location']['lat'])
    smalllist.append(response['results'][0]['geometry']['location']['lng'])
    lista.append(smalllist)


my_list = pd.DataFrame(lista)
my_list.to_csv(r'C:\Users\Ebay15\Desktop\itemlastmonthsold\allpivotlatlngresult.csv', index=False, header=False)
