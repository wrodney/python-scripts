import random
from tkinter import *

def Lotto_No():
    q = random.randint(1,48);
    w = random.randint(1,48);
    e = random.randint(1,48);
    r = random.randint(1,48);
    t = random.randint(1,48);
    y = random.randint(1,48);
    num1.set(q)
    num2.set(w)
    num3.set(e)
    num4.set(r)
    num5.set(t)
    num6.set(y)
    return
    
#def TK():
def TK():
    def lottery ("800 x 360")
    frame = Frame(Lottery)
    frame.pack()

#def Lottery(): title('Lottery Number Generator')
lottery .title('Lottery Number Generator')

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Lotto Numbers Generator")
frame1 = Frame(Lottery)
frame1.pack(side = TOP)
label =Label(frame1, textvariable=var, font =("Arial", 48), width= 24)
label.pack(side = TOP)              
label =Label(frame1, textvariable="", width= 24)
label.pack(side = TOP)              
label =Label(frame1, textvariable="", width= 24)
label.pack(side = TOP)

Lottery.mainloop()

frame2 = Frame(Lottery)
frame2.pack(side = TOP)
txtDisplay=Entry(frame2,textvariable = num1, bd=20,insertwidth=1,font=("Arial", 30), justify='center',width=4)
txtDisplay.pack(side=LEFT)            
txtDisplay=Entry(frame2,textvariable = num2, bd=20,insertwidth=1,font=("Arial", 30), justify='center',width=4)
txtDisplay.pack(side=LEFT)
txtDisplay=Entry(frame2,textvariable = num3, bd=20,insertwidth=1,font=("Arial", 30), justify='center',width=4)
txtDisplay.pack(side=LEFT)
txtDisplay=Entry(frame2,textvariable = num4, bd=20,insertwidth=1,font=("Arial", 30), justify='center',width=4)
txtDisplay.pack(side=LEFT)
txtDisplay=Entry(frame2,textvariable = num5, bd=20,insertwidth=1,font=("Arial", 30), justify='center',width=4)
txtDisplay.pack(side=LEFT)
txtDisplay=Entry(frame2,textvariable = num6, bd=20,insertwidth=1,font=("Arial", 30), justify='center',width=4)
txtDisplay.pack(side=LEFT)

frame3 = Frame(lottery)
frame3.pack(side - TOP)

button1 - Button(frame3, padx-8,width -18,pady-8,bd-8,font -("Arial", 26),text-" Lottery Number Generator"), bd-"black"
button1.pack(side=Top)                                                 
                                                 

Lottery.mainloop()
              


