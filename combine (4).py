# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:11:05 2017

@author: Ebay15
"""

import os
import csv

filelist = os.listdir(r"C:\Users\Ebay15\Desktop\Irving\filteredfiles1to2")

with open(r'C:\Users\Ebay15\Desktop\Irving\combined1to2.csv',"a",newline='') as fout:
    # first file:
    writer = csv.writer(fout, delimiter=",")
    writer.writerow(['Date','Sku',"Qty"])
    
    for filename in filelist:
        with open(r"C:\Users\Ebay15\Desktop\Irving\filteredfiles1to2\%s" %filename, 'r') as csvfile:
            f = csv.reader(csvfile)
            next(f)
            for line in f:
                writer.writerow(line)
fout.close()