# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:03:40 2020

@author: Sahil Shaikh
"""


import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file='data_file.xlsx'
xl=pd.ExcelFile(file) #Read from Excel
dfs=xl.parse(xl.sheet_names[0]) #Parcing Excel sheet to data frame. [0] because in the first column only all the data is there.
dfs=list(dfs['Your Posts']) #Removes blank rows from the data frame.
print(dfs)
sid=SentimentIntensityAnalyzer()
str1='AM'
str2='PM'
count=0
total=0.0
for dat in dfs:
    a = dat.find(str2)
    b = dat.find(str1)
    if(a == -1 and b==-1):
        count=count+1
        ss=sid.polarity_scores(dat)
        total=total+ss['compound']
        print(dat)
        for k in ss:
            print(k,ss[k])

print("=======================")
print("COUNT",count)
print("TOTAL",total)
final=float(total/count)
print("FINAL",final)
