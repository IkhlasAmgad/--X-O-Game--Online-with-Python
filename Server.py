 # -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:25:46 2019

@author: DELL
"""

import tkinter 
from tkinter import *
from tkinter import messagebox
import socket
from _thread import *
import threading



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= "127.0.0.1"
port = 9800
s.bind((host,port))
s.listen(5)



def clicked1():    #define the Function Clicked1
    
    if(btn1['text'] == " "): 
        btn1['text'] = "o"
        value = "1" 
        c.send(value.encode("utf-8")) #Send the value to the client
    check()  #Function to check the winner if a complete row,col,diagonal...
        
def clicked2():    #define the Function Clicked1
   
    if(btn2['text'] == " "):
        btn2['text'] = "o"
        value = "2"
        c.send(value.encode("utf-8"))
        
    check()  #Function to check the winner if a complete row,col,diagonal..

def clicked3():    #define the Function Clicked1
    
    if(btn3['text'] == " "):
        btn3['text'] = "o"
        value = "3"
        c.send(value.encode("utf-8"))
    check()  #Function to check the winner if a complete row,col,diagonal..

def clicked4():    #define the Function Clicked1
    global turn
    if(btn4['text'] == " "):
        btn4['text'] = "o"
        value = "4"
        c.send(value.encode("utf-8"))
        
    check()  #Function to check the winner if a complete row,col,diagonal..

def clicked5():    #define the Function Clicked1
    global turn
    if(btn5['text'] == " "):
        btn5['text'] = "o"
        value = "5"
        c.send(value.encode("utf-8"))   
    check()  #Function to check the winner if a complete row,col,diagonal..
        
def clicked6():    #define the Function Clicked1
    global turn
    if(btn6['text'] == " "):
        btn6['text'] = "o"
        value = "6"
        c.send(value.encode("utf-8"))
        
    check()  #Function to check the winner if a complete row,col,diagonal..
def clicked7():    #define the Function Clicked1
    global turn
    if(btn7['text'] == " "):
        btn7['text'] = "o"
        value = "7"
        c.send(value.encode("utf-8"))
        
    check()  #Function to check the winner if a complete row,col,diagonal..
def clicked8():    #define the Function Clicked1
    global turn
    if(btn8['text'] == " "):
        btn8['text'] = "o"
        value = "8"
        c.send(value.encode("utf-8"))
        
    check()  #Function to check the winner if a complete row,col,diagonal..
def clicked9():    #define the Function Clicked1
    global turn
    if(btn9['text'] == " "):
        btn9['text'] = "o"
        value = "9"
        c.send(value.encode("utf-8"))
        
    check()  #Function to check the winner if a complete row,col,diagonal..

#33333333333333333333333333333333333333333333333333333333333333333333333333333333333
        
        
        
        
        
flag=0       
def check() :
      
    global flag
    flag=flag+1
    b1=btn1["text"]    #E5tsarn l Btn tb2a b :)
    b2=btn2["text"]
    b3=btn3["text"]
    b4=btn4["text"]
    b5=btn5["text"]
    b6=btn6["text"]
    b7=btn7["text"]
    b8=btn8["text"]
    b9=btn9["text"]
 # the 8 possible winning issues#################################3
 
    if (b1==b2 and b2==b3 and b1=='o') or (b1==b2 and b2==b3 and b1=='x'):
        win(b1) #Function for the winner  MSG.
    if (b4==b5 and b5==b6 and b4=='o') or (b4==b5 and b5==b6 and b4=='x'):
        win(b4) #Function for the winner  MSG.
    if (b7==b8 and b8==b9 and b9=='o') or (b7==b8 and b8==b9 and b7=='x'):
        win(b9) #Function for the winner  MSG.
         
    if (b1==b4 and b4==b7 and b4=='o') or (b1==b4 and b2==b3 and b1=='x'):
         win(b1) #Function for the winner  MSG.
    if (b2==b5 and b5==b8 and b5=='o') or (b2==b5 and b5==b8 and b8=='x'):
         win(b4) #Function for the winner  MSG.
    if (b3==b6 and b6==b9 and b9=='o') or (b3==b6 and b6==b9 and b9=='x'):
        win(b9) #Function for the winner  MSG.
             #DIAGONALS
    if (b1==b5 and b5==b9 and b1=='o') or (b1==b5 and b5==b9 and b1=='x'):
        win(b1) #Function for the winner  MSG.
    if (b3==b5 and b5==b7 and b7=='o') or (b3==b5 and b5==b7 and b3=='x'):
        win(b3) #Function for the winner  MSG.
      
    if  flag==10:
         
         messagebox.showinfo("Result","LOSERSSSSSSSS")
     
 #3333333333333333333333333333333333
def recv(c):   #check the Sent value of the client 
    while True:
        btnValue =c.recv(1024).decode("utf-8")

        if(btnValue == "1" and btn1['text'] == " "):
            btn1['text'] = "x"
        if(btnValue == "2" and btn2['text'] == " "):
            btn2['text'] = "x"
        if(btnValue == "3" and btn3['text'] == " "):
            btn3['text'] = "x"
        if(btnValue == "4" and btn4['text'] == " "):
            btn4['text'] = "x"
        if(btnValue == "5" and btn5['text'] == " "):
            btn5['text'] = "x"
        if(btnValue == "6" and btn6['text'] == " "):
            btn6['text'] = "x"
        if(btnValue == "7" and btn7['text'] == " "):
            btn7['text'] = "x"
        if(btnValue == "8" and btn8['text'] == " "):
            btn8['text'] = "x"
        if(btnValue == "9" and btn9['text'] == " "):
            btn9['text'] = "x"
        check()
        print(btnValue)     
 
 
 
def win(player):
    messagebox.showinfo("congrates","Mabrouk")  
    wind.destroy()      
            
                

wind=Tk() #to creat a window and name it "wind"
wind.title("SERVER")
wind.geometry("400x300")

lab1=Label(wind,text="player1:x",font=('Hekvetic','15')) #creat a labels inside a window&(font name,size)
lab1.grid(row=0,column=0) #position of the label inside the window

lab2=Label(wind,text="player2:O",font=('Hekvetic','15'))
lab2.grid(row=1,column=0)

btn1=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Hekvetic','15'),command=clicked1)
     #clicked1 is a function ,"black" is the X-O when they are pressed
btn1.grid(row=0,column=1)

btn2=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Hekvetic','15'),command=clicked2)
btn2.grid(row=0,column=2)

btn3=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Hekvetic','15'),command=clicked3)
btn3.grid(row=0,column=3)

btn4=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Hekvetic','15'),command=clicked4)
btn4.grid(row=1,column=1)

btn5=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Hekvetic','15'),command=clicked5)
btn5.grid(row=1,column=2)

btn6=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Hekvetic','15'),command=clicked6)
btn6.grid(row=1,column=3)

btn7=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Hekvetic','15'),command=clicked7)
btn7.grid(row=2,column=1)

btn8=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Hekvetic','15'),command=clicked8)
btn8.grid(row=2,column=2)

btn9=Button(wind,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Hekvetic','15'),command=clicked9)
btn9.grid(row=2,column=3)

c,add = s.accept()
print("connection established")
start_new_thread(recv, (c,))
#_thread.start_new_thread(recv, () )

wind.mainloop()


