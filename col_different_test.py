# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:13:09 2017

@author: Ebay15
"""

import pandas as pd



newFile = pd.ExcelFile('difference_check1.xlsx')
df = newFile.parse("Sheet1")
df.head()
part = df['PLINK']
company = df['ParsLink']

part_unique = part.unique()
company_unique = company.unique()