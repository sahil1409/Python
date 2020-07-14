# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:04:39 2020

@author: Sahil Shaikh
"""


from tkinter import*
import random
import time
from tkinter import messagebox
colours=['blue','red','yellow','green','red','pink','red','black','green','cyan']
global i
i =0
global redcount
redcount = 0
global greencount
greencount = 0
global canvas

def lvl1():
    global canvas
    n=15
    y = Label(root, text="You have 10 seconds to answer ..",bg = "white",fg="blue",font=("OpenSans", 13, 'bold'))
    y.place (x = 20,y = 550)
    x = startclick(n)
    if x ==1 :
        time.sleep(10)
    messagebox.showinfo("ANSWER ","Number of red balls =" + str (redcount) +" and number of green balls ="+ str(greencount) )
    canvas.delete("all")
    
def lvl2():
    global canvas
    n=25
    y = Label(root, text="You have 8 seconds to answer ..",bg = "white",fg="blue",font=("OpenSans", 13, 'bold'))
    y.place (x = 20,y = 550)
    x = startclick(n)
    if x ==1 :
        time.sleep(8)
    messagebox.showinfo("ANSWER ","Number of red balls =" + str (redcount) +" and number of green balls ="+ str(greencount) )
    canvas.delete("all")
    
def lvl3():
    global canvas
    n=45
    y = Label(root, text="You have 5 seconds to answer ..",bg = "white",fg="blue",font=("OpenSans", 13, 'bold'))
    y.place (x = 20,y = 550)
    x = startclick(n)
    if x ==1 :
        time.sleep(5)
    messagebox.showinfo("ANSWER ","Number of red balls =" + str (redcount) +" and number of green balls ="+ str(greencount) )
    canvas.delete("all")

def startclick(n):
    global i
    global canvas
    global redcount
    global greencount
    redcount=0
    greencount=0
    
    for i in range(0,n+1) :
        m= random.randint(0,10)
        if m == 1 or m==4 or m == 6:
            redcount = redcount+1

        if m == 3 or m==8 :
            greencount = greencount+1
        try:
            a= random.randint(50,250)
            b= random.randint(50,300)
            canvas.create_oval(a, b, a+50, b+50, outline="white", fill=colours[m],width=2)
            canvas.update()
        except:
            print()
    return(1)

root=Tk()
root.title("COUNT THE COLOURS")
root.geometry("800x700+20+20")
canvas=Canvas(width=500,height=500,bg='#87ceeb')
canvas.place(x=20,y=20)
w = Label(root,text="Can you count the number of red and green coloured balls ?",bg= "black",fg="yellow",font=("OpenSans", 13, 'bold'))
w.place (x = 20,y = 500)

lvl1=Button(root,text="LEVEL 1",bg='black',width=20,height=1,font=("OpenSans", 13, 'bold'), fg='white',command=lvl1)
lvl1.place(x=580,y=20)
lvl2=Button(root,text="LEVEL 2",bg='black',width=20,height=1,font=("OpenSans", 13, 'bold'), fg='white',command=lvl2)
lvl2.place(x=580,y=50)
lvl3=Button(root,text="LEVEL 3",bg='black',width=20,height=1,font=("OpenSans", 13, 'bold'), fg='white',command=lvl3)
lvl3.place(x=580,y=80) 
root.mainloop()