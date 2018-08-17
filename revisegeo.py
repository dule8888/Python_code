# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:39:35 2017

@author: Ebay15
"""

from pygeocoder import Geocoder
import pandas as pd



df = pd.read_csv(r'C:\Users\Ebay15\Desktop\geocode\test.csv')
test_geocoder = Geocoder(None,'AIzaSyBMrandixPl7FZ9iAcsbDTkq_no_VuyXwQ')
df = df.iloc[:, :-1]
lista = []

for i in range(0,len(df)):
    a = True
    while a:
        try:
            rea = test_geocoder.reverse_geocode(df['Lat'][i],df['Lng'][i])
        #df['address'] = rea.formatted_address
            lista.append(rea.formatted_address)
            a = False
        except:
            print('oh',i)
            continue
df['address'] = lista


df.to_csv(r'C:\Users\Ebay15\Desktop\geocode\out111.csv',index=False)
