# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:41:05 2017

@author: Ebay15
"""
import xlwt
import xlrd
import csv

def read_words(path):
    book = xlrd.open_workbook(path)
    first_sheet = book.sheet_by_index(0)
    allWords = []                           
    for row in range(1,first_sheet.nrows):
        allWords.append(str(first_sheet.cell(row,3).value).split())
    return allWords  

def flat_list(allWords):
    flat_list = [item for items in allWords for item in items]
    return flat_list

def getUniqueWords(flat_list) :
    unique_list = []
    for i in flat_list:
       if i not in unique_list:
          unique_list.append(i)
    return unique_list

def write_to_csv(uniqueWords):
    wr = open("output.csv",'w')
    for i in uniqueWords:
        wr.write(i + "\n")
    wr.close()
    
def write_to_txt(uniqueWords):
    wr = open("keywords.txt",'w')
    for i in uniqueWords:
        wr.write(i + "\t")
    wr.close()
    
    
        
a = read_words('searchable_keyword_test.xlsx')
b = flat_list(a)
c = getUniqueWords(b)
d = write_to_txt(c)
