# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:59:12 2017

@author: Ebay15
"""

import pandas as pd


df = pd.read_csv("inv_his.csv", header = None, names = ['Date','Sku','Qty'])
df.head(3)
df['Date'] = df['Date'].astype(str)

test = df[0:10]


