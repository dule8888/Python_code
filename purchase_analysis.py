# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:47:12 2017

@author: Ebay15
"""


import csv

purchase_list = []

with open('purchase.csv',) as f:
    for line in f.readlines():
        date,sku,state = line.strip().split(',')
        purchase_list.append([date,sku,state])
        
purchase_list = purchase_list[1:] 
       
filter_list = []
with open('purchase_list.csv') as f:
    lis = [line.split() for line in f]
    for a in lis[:]:
        filter_list.append(a)
        
filter_list_1 = [item for sublist in filter_list for item in sublist]

final_list = []
for i in purchase_list:
    for j in filter_list_1:
        if i[1] == j:
            final_list.append(i)
            
with open("purchase_final.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(final_list)