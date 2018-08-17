# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 08:57:56 2017

@author: Ebay15
"""
import xlwt
import xlrd

def read_excel_report(path):
    book = xlrd.open_workbook(path)
    first_sheet = book.sheet_by_index(0)
    string_list = []                           
    for row in range(1,first_sheet.nrows):
        string_list.append([str(first_sheet.cell(row,0).value).upper(),str(first_sheet.cell(row,9).value).upper()])
    return string_list

def exclude_list(path):
    f = open(path)
    list = []
    for i in f:
        list.append(str(i.replace('\n',"")).upper())
    return list
    

def del_not_relevent(string_list,exclude):
    remain_list = []
    for item_pair in string_list:
        if not any(x in item_pair[1] for x in exclude):
            remain_list.append([item_pair[0],item_pair[1]])
    return remain_list

def write_to_excel(remain_list):
    book = xlwt.Workbook()
    sheet = book.add_sheet("Sheet 1")
    for i, l in enumerate(remain_list):
        for j, col in enumerate(l):
            sheet.write(i, j, col)      
    book.save('remain.xls')

a = read_excel_report('Keyword_filter.xlsx') 
b = exclude_list('exclude.txt')
c = del_not_relevent(a,b)
d = write_to_excel(c)