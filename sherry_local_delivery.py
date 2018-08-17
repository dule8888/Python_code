# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:12:44 2018

@author: le&lang
"""
import pyodbc
import pandas as pd

class local_delivery:
    

    def __init__(self,server_name,username,password):
        self.server_name=server_name
        self.username=username
        self.password=password
        self.data_to_import=[]
    
    #connect to database
    def connect_to_db(self):
        cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+self.server_name+';UID='+self.username+';PWD='+ self.password)
        return cnxn
    
    #read daliy file from local_delivery file and extract the data needed
    def read_jenny_file(self,file_path,sheetname):
        df=pd.read_excel(file_path,sheetname=sheetname)
        for index,row in df.iterrows():
            self.data_to_import.append([row['Order #'],row['SKU'],row['Route'],row['Date'],row['Price']])
       
    #import into database 
    def import_sql(self,data,cnxn):
        cursor=cnxn.cursor()
        cursor.execute('use local_delivery')
        for i in data:
            cursor.execute('insert into daily_local_deliveryall values (\'%s\',\'%s\',\'%s\',%s,\'%s\')' %(i[0],i[1],i[2],i[4],i[3]))
            #cursor.execute('Begin if not exists (select * from daily_local_deliveryall where sales_order =\'%s\' and sku = \'%s\') begin insert into daily_local_deliveryall values (\'%s\',\'%s\',\'%s\',%s,\'%s\') end end' %(i[0],i[1],i[0],i[1],i[2],i[4],i[3]))
        cursor.execute('insert into daily_local_deliverytemp select distinct a.sales_order, a.sku,b.route,a.price,a.qty,b.date from (select sales_order, sku, count(*) as qty, sum(price) as price from daily_local_deliveryall group by sales_order, sku) a left join (select * from daily_local_deliveryall) b on a.sales_order=b.sales_order and a.sku=b.sku')
        cursor.execute('insert into daily_local_delivery(sales_order,sku,route,price,qty,date) select * from daily_local_deliverytemp b where not exists (select * from daily_local_delivery where daily_local_delivery.sales_order=b.sales_order and daily_local_delivery.sku=b.sku)')
        cursor.execute('truncate table daily_local_deliveryall')
        cursor.execute('truncate table daily_local_deliverytemp')
        cnxn.commit()
     
    #write to ship table if shipped and delete from pending
    def write_to_shipped(self,file_path,cnxn,sheetname):
        #load file
        cursor=cnxn.cursor()
        cursor.execute('use local_delivery')
        df=pd.read_excel(file_path,dtype='str',sheetname=sheetname)
        for index,row in df.iterrows():
            print(row['sku'])
            cursor.execute('exec sp_shipped @sales_order=\''+row['order']+'\',@sku=\''+str(row['sku'])+'\',@route_number='+row['route'])
        cnxn.commit()
     
    #generate report for aggregated data by route
    def gen_pending_groupbyroute(self,cnxn,his,qty,datestart,is_export=False,file_path=''):
        cursor=cnxn.cursor()
        cursor.execute('use local_delivery')
        a=cursor.execute('exec sp_daily_list @his = '+str(his)+' , @qty='+str(qty)+', @datestart=\''+datestart+'\'')
        df_export=pd.DataFrame(a.fetchall())
        if is_export:
            df_export.to_csv(file_path,index=False)            
        else:
            print(df_export)
        cnxn.commit()
    
    #generate cost report
    def gen_cost_report(self,cnxn,is_export=False,file_path=''):
        cursor=cnxn.cursor()
        cursor.execute('use local_delivery')
        a=cursor.execute('''select a.route_num,b.ship_date,b.route_q,a.total_unit,a.total_price,driver,b.mileage,b.hours_q,b.frightfee,b.hourlyrate,b.payment,b.paid,b.comment from 
             (select route_num,sum(qty) as total_unit, sum(price) as total_price, min(date_q) as earliest_date 
              from daily_local_shipped
              group by route_num) a
              join 
              (select * from Local_delivery_cost) b
              on a.route_num = b.ID''')
        df_export=pd.DataFrame(a.fetchall())
        if is_export:
            df_export.to_csv(file_path,index=False)            
        else:
            print(df_export)
        cnxn.commit()        

if __name__ == '__main__':
    a=local_delivery('EBAY-PC\SQLEXPRESS','sa','1234')
    a.read_jenny_file(r'Z:\lang\local_delivery_0307.xlsx','Sheet1')
    cnxn=a.connect_to_db()
    a.import_sql(a.data_to_import,cnxn)
    #a.write_to_shipped(r'Z:\lang\daliy_local_delivery.xlsx',cnxn,'UCC')
    #a.gen_cost_report(cnxn)
    cnxn.close()
    
    

'''for i,j in enumerate(sheets):
    df=pd.read_excel(r'Z:\Sherry\Routes Record_Feb.xlsx',sheetname=j,dtype=str)
    df['route_id']=str(16+i)
    if 'ORDER' in df.columns:
        for index,row in df.iterrows():
            data.append([j,row['ORDER'],row['SKU'],row['route_id']])
    if 'Order #' in df.columns:
        for index,row in df.iterrows():
            data.append([j,row['Order #'],row['SKU'],row['route_id']])'''