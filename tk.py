from tkinter import *
app=Tk()
app.title('Calculator')
global first
global operator
first=''
operator=''
e=Entry(app, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def but_add(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,int(str(current)+str(number)))

def but_clear():
    e.delete(0,END)
    
def addition():
    global first
    global operator
    operator="add"
    first=e.get()
    e.delete(0,END)

def subtraction():
    global first
    global operator
    operator="sub"
    first=e.get()
    e.delete(0,END)

def multiplication():
    global first
    global operator
    operator="mul"
    first=e.get()
    e.delete(0,END)

def division():
    global first
    global operator
    operator="div"
    first=e.get()
    e.delete(0,END)
    
def equals():
    second=e.get()
    e.delete(0,END)
    if operator=="add":
        e.insert(0,int(first)+ int(second))
    elif operator=="sub":
        e.insert(0,int(first)-int(second))
    elif operator=="mul":
        e.insert(0,int(first)* int(second))
    elif operator=="div":
        e.insert(0,int(first)/ int(second))
    elif operator=='':
        e.insert("none")
        
    

but_1=Button(app, text="1", padx=20,pady=10,command=lambda: but_add(1))
but_2=Button(app, text="2", padx=20,pady=10,command=lambda: but_add(2))
but_3=Button(app, text="3", padx=20,pady=10,command=lambda: but_add(3))
but_4=Button(app, text="4", padx=20,pady=10,command=lambda: but_add(4))
but_5=Button(app, text="5", padx=20,pady=10,command=lambda: but_add(5))
but_6=Button(app, text="6", padx=20,pady=10,command=lambda: but_add(6))
but_7=Button(app, text="7", padx=20,pady=10,command=lambda: but_add(7))
but_8=Button(app, text="8", padx=20,pady=10,command=lambda: but_add(8))
but_9=Button(app, text="9", padx=20,pady=10,command=lambda: but_add(9))
but_0=Button(app, text="0", padx=20,pady=10,command=lambda: but_add(0))
but_ad=Button(app, text="+", padx=20,pady=10,command=lambda: addition())
but_sub=Button(app, text="-", padx=20,pady=10,command=lambda:subtraction())
but_mul=Button(app, text="*", padx=20,pady=10,command=lambda:multiplication())
but_eql=Button(app, text="=", padx=59,pady=10,command=lambda:equals())
but_div=Button(app, text="/", padx=20,pady=10,command=lambda:division())
but_clr=Button(app, text="Clear", padx=129,pady=10,command=lambda: but_clear())


but_1.grid(row=1,column=0)
but_2.grid(row=1,column=1)
but_3.grid(row=1,column=2)
but_ad.grid(row=1,column=3)

but_4.grid(row=2,column=0)
but_5.grid(row=2,column=1)
but_6.grid(row=2,column=2)
but_sub.grid(row=2,column=3)

but_7.grid(row=3,column=0)
but_8.grid(row=3,column=1)
but_9.grid(row=3,column=2)
but_mul.grid(row=3,column=3)

but_0.grid(row=4,column=0)
but_div.grid(row=4,column=1)
but_eql.grid(row=4,column=2,columnspan=2)

but_clr.grid(row=5,column=0,columnspan=4)

app.mainloop()
