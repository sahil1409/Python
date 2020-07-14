# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:25:57 2020

@author: Sahil
"""

import csv

with open('route.csv','r') as f:
    reader=csv.reader(f)
    
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        print(lat)
        print(long)
        print(lat+long)
        