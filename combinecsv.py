# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:19:49 2017

@author: Ebay15
"""
import os

fout=open(r'G:\inventory\final\invhistfinal.csv',"a")
# first file:
    
filelist = os.listdir(r"G:\inventory\final")

for fname in filelist:
    f = open(r"G:\inventory\final\%s" %fname)
    for line in f:
         fout.write(line)
    f.close()
    print(fname,'is done')
fout.close()

