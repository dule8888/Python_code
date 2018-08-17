# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:11:05 2017

@author: Ebay15
"""

import os
import csv

filelist = os.listdir(r"G:\inventory\filterfile")

with open(r'G:\inventory\filterfile\combinedfinal1.csv',"a",newline='') as fout:
    # first file:
    writer = csv.writer(fout, delimiter=",")
    writer.writerow(['Date','Sku',"Qty"])
    
    for filename in filelist:
        with open(r"G:\inventory\filterfile\%s" %filename, 'r') as csvfile:
            f = csv.reader(csvfile)
            next(f)
            for line in f:
                writer.writerow(line)
fout.close()