# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:47:47 2018

@author: apersonett
"""

import pandas as pd
from pandas import ExcelWriter


class workerchecklist:
    
    def __init__(self,printtagfile,breakdownfile,outputfile):
        self.printtagfile = printtagfile
        self.breakdownfile = breakdownfile
        self.outputfile = outputfile
        
    def outputfile_1(self):
        ### read two files outputed from adv
        df1 = pd.read_csv(self.breakdownfile,names=["quote", "date", "sku", "qty","price"],header=0,encoding = "ISO-8859-1")
        df2 = pd.read_excel(self.printtagfile)
        
        ### using open sales quote in the printtag file to filter the breakdown file###
        openso = set(df2['quote'])
        haveopenso = df1.quote.isin(openso)
        df3 = df1[haveopenso]
        
        ### join two files to get data together from two files
        df4 = pd.merge(df3[['quote','sku', 'qty','price']],
                         df2[['date','quote','enteredby', 'customercode','deliverymethod','totalamt']],
                         on='quote',how='left')
        
        ### reorder the coloums to desired data foramt                 
        df5 = df4[['date','quote','enteredby','sku','customercode','deliverymethod','qty','price','totalamt']]

        ### check the last row of each group and keep total amt only in the last row
        df5.groupby('quote').last()  
        lastrow = df5.reset_index().groupby("quote")["index"].last()
        df6 =pd.DataFrame({'quote':lastrow.index, 'idx':lastrow.values})
        kepper = df6.iloc[:,0] 
        kepper = kepper.tolist()
        df5.loc[~df5.index.isin(kepper), 'totalamt'] = ' '
        
        ### check the first row of each group and marked as x for hightlight in excel        
        df5['firstrow'] = ' '
        firstrow = df5.reset_index().groupby("quote")["index"].first()
        df7 =pd.DataFrame({'quote':firstrow.index, 'idx':firstrow.values})
        firstrowkepper = df7.iloc[:,0] 
        firstrowkepper = firstrowkepper.tolist()
        df5.loc[df5.index.isin(firstrowkepper), 'firstrow'] = 'x'
        
        ### output to excel file
        writer = ExcelWriter(self.outputfile)
        df5.to_excel(writer,'Sheet1',index=False)
        writer.save()
        
        
if __name__=="__main__":
    obj = workerchecklist(r'D:\py\QINV0208output.xlsx',r'D:\py\QIVL0208.txt',r'D:\py\workerchecklist0208.xlsx')
    obj.outputfile_1()