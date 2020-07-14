# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:17:43 2020

@author: Sahil
"""

import turtle

turtle.bgcolor("black")
tur=turtle.Turtle()

width=5
height=7

dot_distance=25

tur.setpos(-250,250)

def spiral(m,n):
    k=0
    l=0
    f=0
    tur.color("white")
    '''
    k=index of starting row
    l=index of starting column
    
    '''
    while(k<m and l<n):
        
        if(f==1):
            tur.right(90)
        
        #printed the first row from remaining rows
        for i in range(l,n):
            tur.forward(dot_distance)
            #print(a[k][i],end=" ")
            
        k+=1
        f=1
        
        tur.right(90)
        #printing the last column from remaining columns
        for i in range(k,m):
            tur.forward(dot_distance)
            #print(a[i][n-1],end=" ")
            
        n-=1
        tur.right(90)
        
        #we have already checked this condition in while loop but still again checking because we are incrementing k+=1
        if(k<m):
            #printing last row from remaining rows
            for i in range(n-1,l-1,-1): #l-1 because we want to include the first element also(for reverse for loop we decrementn to include first element). Step=-1 as we are decrementing for loop. 
                tur.forward(dot_distance)
                #print(a[m-1][i],end=" ")
                
            m-=1
        tur.right(90)    
        
        if(l<n):
            #printing the first column from remaining columns
            for i in range(m-1,k-1,-1):
                tur.forward(dot_distance)
                #print(a[i][l],end=" ")
                
            l+=1

spiral(20,20)
turtle.done()
        