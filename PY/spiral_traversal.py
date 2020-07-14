# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:12:00 2020

@author: Sahil
"""

def spiral(m,n,a):
    k=0
    l=0
    
    '''
    k=index of starting row
    l=index of starting column
    
    '''
    while(k<m and l<n):
        
        #printed the first row from remaining rows
        for i in range(l,n):
            print(a[k][i],end=" ")
            
        k+=1
        
        #printing the last column from remaining columns
        for i in range(k,m):
            print(a[i][n-1],end=" ")
            
        n-=1
        
        #we have already checked this condition in while loop but still again checking because we are incrementing k+=1
        if(k<m):
            #printing last row from remaining rows
            for i in range(n-1,l-1,-1): #l-1 because we want to include the first element also(for reverse for loop we decrementn to include first element). Step=-1 as we are decrementing for loop. 
                print(a[m-1][i],end=" ")
                
            m-=1
            
        if(l<n):
            #printing the first column from remaining columns
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=" ")
                
            l+=1
        
a=[]
count=1
for i in range(4):
    l=[]
    for i in range(4):
        l.append(count)
        count+=1
    a.append(l)
    
print(a)

spiral(4,4,a)
    
        