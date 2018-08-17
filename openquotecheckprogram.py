# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 13:23:26 2018

@author: apersonett
"""
"""bkarqivl"""

import pandas as pd
from pandas import ExcelWriter



class printag:
    
    def __init__(self,inputpath,outputpath):
        self.inputpath = inputpath
        self.outputpath = outputpath
    
    def outputfile(self,start_date,end_date):

        df2 = pd.read_csv(self.inputpath,names=["invoice", "quote", "customercode", "customername","deliverymethod","enteredby","totalamt","date"],parse_dates=["date"],header=0,encoding = "ISO-8859-1")
        df3 = df2[['date', 'quote', 'enteredby', 'customercode', 'deliverymethod','totalamt']][df2['invoice']==0]
        mask = (df3['date'] >= start_date) & (df3['date'] <= end_date)
        df3 = df3[mask]
        df3['checkbox'] = ' '
        df3['comment'] = ' '
        df4 = df3.sort_values(['date', 'enteredby'], ascending=[True, False])

        writer = ExcelWriter(self.outputpath)
        df4.to_excel(writer,'Sheet1',index=False)
        writer.save()
    
if __name__=="__main__":
    obj=printag(r'y:\le\quotefollowup\quote0815\QINV0815.txt',r'y:\le\quotefollowup\quote0815\QINVbypersonoutput11.xlsx')
    obj.outputfile('2018-08-09','2018-08-15')
    