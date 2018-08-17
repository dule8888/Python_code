# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from pandas import ExcelWriter



class printag:
    
    def __init__(self,inputpath,outputpath):
        self.inputpath = inputpath
        self.outputpath = outputpath
    
    def outputfile(self,start_date,end_date):

        df2 = pd.read_csv(self.inputpath,names=["invoice", "quote", "customercode", "customername","deliverymethod","enteredby","totalamt","date"],parse_dates=["date"],header=0,encoding = "ISO-8859-1")
        df3 = df2[['date', 'quote', 'enteredby', 'customercode', 'deliverymethod','totalamt']][df2['invoice']==0]
        mask = (df3['date'] > start_date) & (df3['date'] <= end_date)
        df3 = df3[mask]
        df3['checkbox'] = ' '
        df3['comment'] = ' '
        df4 = df3.sort(['date', 'enteredby'], ascending=[True, False])

        writer = ExcelWriter(self.outputpath)
        df4.to_excel(writer,'Sheet1',index=False)
        writer.save()
    
if __name__=="__main__":
    obj=printag(r'D:\py\QINV0208.txt',r'D:\py\QINV0208output.xlsx')
    obj.outputfile('2018-01-01','2018-01-31')