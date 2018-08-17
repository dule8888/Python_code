# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:26:43 2017

@author: ebay
"""

import openpyxl
from openpyxl.drawing.image import Image
import pandas as pd
import urllib.request
import requests
from lxml import html
import re

class pic:
    def __init__(self):
        self.urls=[]
        self.itemid=[]
        self.pic_url=[]
        self.url_to_crawl=[]

       
    def load_file(self,path,col):
        df=pd.read_excel(path)
        self.urls=[[i] for i in df[col]]
        s=[i for i in df['User Label']]
        for i,j in enumerate(s):
            self.urls[i].append(j)
        
    def get_pic(self,urls,path):
        wb = openpyxl.load_workbook(path)
        ws=wb.active
        for i,j in enumerate(urls):
            try:
                data = urllib.request.urlopen(j[0]).read()
                file = open(str(j[1])+'.jpg', "wb")
                file.write(data)
                file.close()
            
                my_png = Image(str(j[1])+'.jpg')
                ws.add_image(my_png,'C'+str(i+2))
            except:
                continue
        wb.save(path)
    
    
    def load_file_pic(self,path):
        df=pd.read_excel(path)
        for index,row in df.iterrows():
            self.itemid.append(row['itemid'])
        for i in self.itemid:
            self.url_to_crawl.append(['https://www.ebay.com/itm/'+str(i),i])
            
    def get_pic_link(self,url):
        for i in url:
            try:
                c=requests.get(i[0])
                co=html.fromstring(c.content)
                tr=co.xpath("//td[@class='tdThumb']/div/img/@src")
                self.pic_url.append([tr[0],i[1]])
            except:
                continue