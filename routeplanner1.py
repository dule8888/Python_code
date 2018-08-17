# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:51:32 2018

@author: LE&LANG
"""

import pandas as pd
import requests
import numpy as np
import datetime



### set map quest api parameters
akey='rGobNjAp6aqgF4Amh3ODmuHZQdr1KDqC'
web = 'http://www.mapquestapi.com/directions/v2/route?key=%s&' % (akey)
choice = 'shortest'
biglist = []

### read orinal buyers address file, concatenate address city zip and convert into a number, address directionary 
df = pd.read_excel(r"D:\Documents and Settings\apersonett\Desktop\routepy\test\detRoute.xlsx", sheetname='Sheet1')
df['longaddress'] = df.astype(str).apply(lambda x: ' , '.join(x), axis=1)  
df2 = df['longaddress']
df3 = {}
df3 = dict(df2)

### create address and number dictionary
k=df3.keys()
df4={}
for i in k:
    df4[df3[i]]=i

### swap order in route list without change the first and last address
two_opt_swap = lambda r,i,k: np.concatenate((r[0:i],r[k:-len(r)+i-1:-1],r[k+1:len(r)]))

### return distance for each from to city pairs
def getdistance(fromcity,tocity,distancematrix):
    a = distancematrix[(distancematrix['from']==fromcity)&(distancematrix['to']==tocity)]['distance']
    b = a.iloc[0]
    return b
    
### get time list for the final bestdistance route    
def gettimelist(new_route,distancematrix):
    timelist = []
    for i in range(0,len(new_route)-1):
        a = distancematrix[(distancematrix['from']==new_route[i])&(distancematrix['to']==new_route[i+1])]['time']
        b = a.iloc[0] 
        timelist.append(b)
    return timelist

 ### add total time and return total time   
def sumtime(timelist):
    totaltime = datetime.timedelta()
    for i in timelist:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        totaltime += d
    return totaltime

### add distance for inputed route
def sumdistance(new_route,distancematrix):
    distancelist = []
    totaldistance = 0
    for i in range(0,len(new_route)-1):
        distance = 0
        distance = float(getdistance(new_route[i],new_route[i+1],df6))
        distancelist.append(distance)
        totaldistance = totaldistance +  distance
    return totaldistance,distancelist
    
### optimaze route and print out result for best route total time and total distance   
def two_opt(addresslist,distancematrix,improvement_threshold):
    best_distance=10000# 2-opt Algorithm adapted from https://en.wikipedia.org/wiki/2-opt
    route = np.arange(addresslist.shape[0]) # Make an array of row numbers corresponding to cities.
    improvement_factor = 1 # Initialize the improvement factor.
    best_distance,dlist = sumdistance(route,distancematrix) # Calculate the distance of the initial path.
    while improvement_factor > improvement_threshold: # If the route is still improving, keep going!
        distance_to_beat = best_distance # Record the distance at the beginning of the loop.
        for swap_first in range(1,len(route)-3): # From each city except the first and last,
            for swap_last in range(swap_first+1,len(route)-1): # to each of the cities following,
                new_route = two_opt_swap(route,swap_first,swap_last) # try reversing the order of these cities
                new_distance,dlist= sumdistance(new_route,distancematrix) # and check the total distance with this modification.
                if new_distance < best_distance: # If the path distance is an improvement,
                    route = new_route # make this the accepted best route
                    best_distance = new_distance # and update the distance corresponding to this route.
        improvement_factor = 1 - best_distance/distance_to_beat # Calculate how much the route has improved.
    timelist = gettimelist(route,distancematrix)
    besttime = sumtime(timelist)
    print(route+1)
    print(best_distance)
    print(besttime)
    return route,best_distance,besttime,dlist,timelist # When the route is no longer improving substantially, stop searching and return the route.



### get all from to address pair and get distance from map quest api
s =''
c = df['longaddress'].values.flatten().tolist()
for i in c:
    s +=  '"'+ str(i) + '"'+","
s = s[:-1]
route_pairs = [(c[i],c[j]) for i in range(len(c)) for j in range(i+1, len(c))]
for i in range(len(route_pairs)):
    print(i)
    smalllist = []
    orgin = list(route_pairs[i])[0]
    dest = list(route_pairs[i])[1]    
    parameter = 'from=%s&to=%s&routeType=%s' % (orgin,dest,choice)
    request = web + parameter
    print(request) 
    response =requests.get(request).json()
    g = response['route']['distance']
    h = response['route']['formattedTime']
    print(g)
    print(h)
    smalllist.append(orgin)
    smalllist.append(dest)
    smalllist.append(g)    
    smalllist.append(h)     
    biglist.append(smalllist)
    print(i, 'is done')
my_list = pd.DataFrame(biglist)

###  append the address matrix to converte from triangle to full matrix and using index to replace address
my_list.columns = ['from','to','distance','time']
df5 = my_list.copy()
df5 = my_list[['to','from','distance','time']]
df5.columns = ['from','to','distance','time']
df6=pd.DataFrame()
df6 = my_list.append(df5,ignore_index=True)
df6['from'].replace(df4, inplace=True)
df6['to'].replace(df4, inplace=True)




### call two_opt function to get the best route time and miles
bestroute,bestdistance,besttime, distancelist,timelist= two_opt(df,df6,0.0001)







### make the final from to list and write best time distance 
fromlist = bestroute[0:-1]
tolist = bestroute[1:]
df7 = pd.DataFrame({'from':fromlist})
df7['to'] = pd.Series(tolist) 
df7['from'].replace(df3, inplace=True)
df7['to'].replace(df3, inplace=True)
df7['distance'] = pd.Series(distancelist) 
df7['time'] = pd.Series(timelist) 
orderlist = []
for col, data in enumerate(bestroute):
    orderlist.append(data+1)
df7['order'] = pd.Series(orderlist) 
df7['total'] = ' '
df7.iloc[-2,5] = bestdistance
df7.iloc[-1,5] = '%s' %besttime



### export to excel file
df7.to_csv(r'D:\Documents and Settings\apersonett\Desktop\routepy\test\testresult.csv',index=False)

