# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:16:53 2018

@author: ebay
"""

import ebaysdk

import requests

import re
import csv
import pandas as pd
import openpyxl
import time
import urllib.request
import xlsxwriter
from io import BytesIO

from ebaysdk.shopping import Connection as Shopping

from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

df=pd.read_excel(r'C:\Users\ldu\Desktop\large_to_small_fast_mover_price_check\Book1.xlsx',sheetname='Sheet1')

l=[i for i in df['partlinks']]
len(l)

api_res=[]
real_list=pd.DataFrame([])
len(api_res)

count = 0


for i in l:
#    print(i)
    if count ==3:
        print('exit')
        break
    else:
        try:
            api=Finding(config_file=r'C:\Users\ldu\Desktop\large_to_small_fast_mover_price_check\ebay.yaml')
            #api = Finding(config_file=r'C:\Users\ebay\Anaconda3\Lib\site-packages\ebaysdk-2.1.4-py3.6.egg\ebay.yaml')
        #api = Finding(config_file=r'Z:\lang\partslink\ebay.yaml')
            response = api.execute('findItemsAdvanced', {'categoryId':'6000','keywords': str(i),'outputSelector':['SellerInfo','QuantitySold'],'paginationInput': {'entriesPerPage': '50','pageNumber': '1'}})
            api_res.append([i,response.dict()])
            time.sleep(0.3)
        except Exception as e:
            count = count + 1
            if count ==1:
                api=Finding(config_file=r'C:\Users\ldu\Desktop\large_to_small_fast_mover_price_check\ebay.yaml')
                print('now trying lqin')
                time.sleep(1)
            elif count ==2:
                api=Finding(config_file=r'C:\Users\ldu\Desktop\large_to_small_fast_mover_price_check\ebay.yaml')
                print('now trying sunny')
                time.sleep(1)
            else:
                count=3
                print(e.response.dict())
                

api_res[1][1]

for j in api_res:
    if 'item' in j[1]['searchResult'].keys():
       
        for i in j[1]['searchResult']['item']:
            if 'watchCount' in i['listingInfo'].keys():
#                 print(j[0])
#                 print(i['primaryCategory']['categoryId'])
#                 print(i.keys())
                 try:                 
                      real_list_temp=pd.DataFrame({
                            'Parts link':j[0],
                            'topRatedListing':i['topRatedListing'],
                            'categoryId':i['primaryCategory']['categoryId'],
                            'itemId':i['itemId'],
#                            'sellerInfo':i['sellerInfo'],
                            'value':i['sellingStatus']['convertedCurrentPrice']['value'],
                            'title':i['title'],
                            'sellerUserName':i['sellerInfo']['sellerUserName'],
                            'handlingTime':i['shippingInfo']['handlingTime'],
                            'shipCost':i['shippingInfo']['shippingServiceCost']['value'],
                            'watchCount':i['listingInfo']['watchCount']
                                  },index=[0])
                      real_list=real_list.append(real_list_temp,ignore_index=True)
                 except:
                    continue
            else:
            
                try:
                    real_list_temp=pd.DataFrame({
                            'Parts link':j[0],
                            'topRatedListing':i['topRatedListing'],
                            'categoryId':i['primaryCategory']['categoryId'],
                            'itemId':i['itemId'],
#                            'sellerInfo':i['sellerInfo'],
                            'value':i['sellingStatus']['convertedCurrentPrice']['value'],
                            'title':i['title'],
                            'sellerUserName':i['sellerInfo']['sellerUserName'],
                            'handlingTime':i['shippingInfo']['handlingTime'],
                            'shipCost':i['shippingInfo']['shippingServiceCost']['value'],
                            'watchCount':i['listingInfo']['watchCount']
                                  },index=[0])
                    real_list=real_list.append(real_list_temp,ignore_index=True)
                except:
                    continue
                

   
real_list.to_excel(r'C:\Users\ldu\Desktop\large_to_small_fast_mover_price_check\result.xlsx',index=False)
                