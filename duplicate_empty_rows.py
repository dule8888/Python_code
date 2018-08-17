# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:55:53 2017

@author: Ebay15
"""

import pandas as pd

df = pd.read_excel(r'C:\Users\Ebay15\Desktop\salesvsinventory\morethan10\empty_rows.xlsx', sheetname='Sheet1' , header = None)
a = pd.concat([df]*792)


writer = pd.ExcelWriter(r'C:\Users\Ebay15\Desktop\salesvsinventory\morethan10\duplicatedrows.xlsx')
a.to_excel(writer,'Sheet1')

writer.save()