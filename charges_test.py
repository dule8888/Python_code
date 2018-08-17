# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:37:47 2017

@author: ebay
"""

import csv
import pandas as pd

longlist = []

with open('fedex_charges.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for lines in reader:
        for i in range(1,len(lines),2):
            shortlist = []
            if lines[i] != '':
                shortlist.append(lines[0])
                shortlist.append(lines[i])
                shortlist.append(lines[i+1])
                longlist.append(shortlist)
            
 
df = pd.DataFrame(longlist,columns=['id','chargefor','price'])

dfwide = pd.pivot_table(df, index='id', columns=['chargefor'], aggfunc=max)

dfwide.fillna(0, inplace=True)

dfwide.to_csv('charge_wide.csv',encoding='utf-8')