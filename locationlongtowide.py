# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:43:31 2018

@author: apersonett
"""

import pandas as pd

df = pd.read_csv('loc0501.txt',header=None)
df1 = df.iloc[:,[0,3]]
df1.columns = ['sku', 'bin']
df2 = df1.drop_duplicates(subset=['sku', 'bin'], keep=False)
df3 = df2.groupby('sku')
df4 = df3.aggregate(lambda x: tuple(x))

df4.to_csv('temple1.csv')

df5 = pd.read_csv('temple1.csv')

df5['bin'] = df5['bin'].str.replace("'","")
df5['bin'] = df5['bin'].str.replace("(","")
df5['bin'] = df5['bin'].str.replace(")","")

df5.to_csv('final1.csv',index = False)