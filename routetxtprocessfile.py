# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import glob




bad_words = ['Page', 'Sales Report for','For the Year ','March 01, 2018','---', 'S/O Date']


for filename in glob.glob(r'W:\le\braches\Irving\ROUTEANALYSIS\*.txt'):   
    shortlist = []
    with open(filename) as oldfile:
            for line in oldfile:
                if not any(bad_word in line for bad_word in bad_words):
                    shortlist.append(line.replace('\n',' ').replace(' ','').split(':'))
    df =pd.DataFrame(shortlist)
    df = df.iloc[:,:-1]
    df.columns = ['Date','Inv','Cust Code','Trm','Sls','D','Entby','Route','Paid','Inv_Tot','Profit']
    df.to_csv(filename[:-3] + 'csv',index=False)

with open(r'W:\le\braches\Irving\ROUTEANALYSIS\RT160301.txt') as oldfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                shortlist.append(line.replace('\n',' ').replace(' ','').split())
df =pd.DataFrame(shortlist)
df.to_csv(filename[:-3] + 'csv',index=False)