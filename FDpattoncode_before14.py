# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:27:42 2018

@author: ldu
"""

import pandas as pd
from openpyxl import load_workbook
import glob  
import csv

path = 'C:/Users/ldu/Desktop/pattoncode/irving11to13/'

writer = pd.ExcelWriter(path+'FDNEWSALES11to13.xlsx') 
writer.save()

"""read fd sku list"""
fdlist = pd.read_excel(path + 'patton_and_sku.xlsx', sheet_name='Sheet1', header=None)
fdlist.columns = ["sku","PATENT #"]


"""read all txt from directory"""  
files=glob.glob(path + 'HIVL*.txt')  

"""read irving customer list"""
customerlist = pd.read_csv(path+'HINV0604.txt', sep="\t", header=None)
customerlist.columns = ["so",'CUST CODE']


for filenames in files:
    if filenames[-7:-4] == 'IRV':
            """ read data from source and rename coloumns"""
            longlist = []    
            with open(filenames, newline='') as csvfile:
                spamreader = csv.reader((x.replace('\0', '') for x in csvfile), delimiter=',')
                for row in spamreader:
                    words = [word.replace('"',' ') for word in row]
                    longlist.append(words)
                    
            data = pd.DataFrame(longlist)
            data = data.iloc[:,[0,1,2,3,4,5,8]]
            data[~data[7].isnull()].to_csv(path+filenames[-7:-4]+'problem.csv',index = False)
            data = data.drop(data.index[data[~data[7].isnull()].index.values])
            data = data.iloc[:,:-1]
            
            data.columns = ["so", "date", "sku","desc", "qty","unitprice","COST"]
            data['date'] = data['date'].astype(int) 
            data['so'] = data['so'].astype(int) 

            """ filterout date is 00000000"""
            data1 = data[data.iloc[:,1] != 00000000]
            """ add filter to date"""                            
            data1 = data1[data1.iloc[:,1] >= 20110101]
            data1 = data1[data1.iloc[:,1] <= 20131231]
            data1[["qty","unitprice","COST"]] = data1[["qty","unitprice","COST"]].astype(float)
          
            """ filterout qty is 0"""
            data1 = data1.loc[data1["qty"] != 0]
        
            
        
            """left join sales data with ford list"""
            result = pd.merge(data1,fdlist,how='left',on="sku")
            result1 = result.loc[result['PATENT #'].notna()]
        
            
            """left join sales data with customername"""
            result2 = pd.merge(result1,customerlist,how='left',on="so")
        
                                        
            """ add total price"""
            result2["TOTAL"] = result2.qty * result2.unitprice
            result2 = result2[["so", "date", "sku","desc", "qty","unitprice","TOTAL","COST","PATENT #","CUST CODE"]]
        
            """ write data to excel"""  

            
            with pd.ExcelWriter(path+'FDNEWSALES11to13.xlsx', engine='openpyxl') as writer:
                writer.book = load_workbook(path+'FDNEWSALES11to13.xlsx')
                result2.to_excel(writer, filenames[-7:-4],"1" ,index = False)                  
                writer.save()
            print(filenames,"is done")  