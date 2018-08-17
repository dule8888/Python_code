# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:09:58 2017

@author: Ebay15
"""
import re

#"inv0921.txt", "r"
#inv0921_no0", "w"
with open("PPP.TXT", "r") as filestream:
    with open("PPP_sku_pro.TXT", "w") as filestreamtwo:
        for line in filestream:
            currentline = line.split(",")
            total = str(currentline[0]) +"," + str(currentline[1]) + "\n"
            result = re.match('\"[A-Z]',str(currentline[1]))
            if result != None:
                #print(total)
            #if (str(currentline[0]) != '00000000' or :
             filestreamtwo.write(total)