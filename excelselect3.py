# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:11:53 2017

@author: Ebay15
"""

import shutil
import os
import pandas as pd
import numpy as np 

src = r"C:\Users\Ebay15\Desktop\Irving\files"
for file in os.listdir(src):
    if file.endswith("_2.xlsx"):
        filename = os.path.join(src,file)
        shutil.copy2(filename, 
        r"C:\Users\Ebay15\Desktop\Irving\filteredfile\%s" %file)

filelist = os.listdir(r"C:\Users\Ebay15\Desktop\Irving\filteredfile")

for fname in filelist:
    newname = str("2017" + str(fname[11:13]) + str(fname[14:16] + ".xlsx"))
    os.rename(r"C:\Users\Ebay15\Desktop\Irving\filteredfile\%s" %fname, 
    r"C:\Users\Ebay15\Desktop\Irving\filteredfile\%s" %newname)
    
text_file = open(r"C:\Users\Ebay15\Desktop\Irving\soldmorethan30.txt", "r")
lines = text_file.read().splitlines()
lines = list(set(lines))
text_file.close()   


files = os.listdir(r"C:\Users\Ebay15\Desktop\Irving\file")

for file in os.listdir(r"C:\Users\Ebay15\Desktop\Irving\file"):
    df = pd.read_excel(r"C:\Users\Ebay15\Desktop\Irving\file\%s" %file, 'Sort-H' , header=None)
    midlist = []
    for index,row in df.iterrows():
        shortlist = []
        if str(row[0]) in lines:
            shortlist.append(row[0])
            shortlist.append(row[2])
            midlist.append(shortlist)
    df1 = pd.DataFrame(midlist,columns=["sku","qty"])   
    a = df1.groupby('sku',as_index=False).sum()
    a['date'] = str(file[4:6] + "/" + file[6:8] + '/' + "2017")
    a = a.reindex_axis(['date','sku','qty'], axis=1)
    csvfilename = str(file[0:9] + 'csv')
    a.to_csv(r'C:\Users\Ebay15\Desktop\Irving\filteredfiles30plus\%s' %csvfilename, header = False,index = False)
    print(file + " is done")
           

