from tkinter import *

root = Tk() 
root.title("My Calculator")

e = Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    #to get number passed
    first = e.get()
    #fnum is global so that can be used in all the functions
    global fnum
    global m 
    m = "add"   
    fnum = int(first)
    e.delete(0, END)

def button_sub():
    first = e.get()
    global fnum
    global m 
    m = "sub" 
    fnum = int(first)
    e.delete(0, END) 

def button_mul():
    first = e.get()
    global fnum
    global m 
    m = "mul" 
    fnum = int(first)
    e.delete(0, END)   

def button_div():
    first = e.get()
    global fnum
    global m 
    m = "div" 
    fnum = int(first)
    e.delete(0, END)    

def button_equal():
    second = int(e.get())
    e.delete(0,END)
    if m == "add":
        e.insert(0, fnum + second)
    if m == "sub":
        e.insert(0, fnum - second)
    if m == "mul":
        e.insert(0, fnum * second)
    if m == "div":
        e.insert(0, fnum / second)


b1 = Button(root, text="1", command=lambda: button_click(1), padx=40, pady = 20)
b2 = Button(root, text="2", command=lambda: button_click(2), padx=40, pady = 20)
b3 = Button(root, text="3", command=lambda: button_click(3), padx=40, pady = 20)
b4 = Button(root, text="4", command=lambda: button_click(4), padx=40, pady = 20)
b5 = Button(root, text="5", command=lambda: button_click(5), padx=40, pady = 20)
b6 = Button(root, text="6", command=lambda: button_click(6), padx=40, pady = 20)
b7 = Button(root, text="7", command=lambda: button_click(7), padx=40, pady = 20)
b8 = Button(root, text="8", command=lambda: button_click(8), padx=40, pady = 20)
b9 = Button(root, text="9", command=lambda: button_click(9), padx=40, pady = 20)
b0 = Button(root, text="0", command=lambda: button_click(0), padx=40, pady = 20)

b_add = Button(root, text="+", command=button_add, padx=39, pady = 20)
b_sub = Button(root, text="-", command=button_sub, padx=40, pady = 20)
b_mul = Button(root, text="*", command=button_mul, padx=40, pady = 20)
b_div = Button(root, text="/", command=button_div, padx=40, pady = 20)

b_eq = Button(root, text="=", command=button_equal, padx=89, pady = 20)
b_clr = Button(root, text="Clear", command=button_clear, padx=79, pady = 20)


b1.grid(row=3, column=0 )
b2.grid(row=3, column=1 )
b3.grid(row=3, column=2 )
b4.grid(row=2, column=0 )
b5.grid(row=2, column=1 )
b6.grid(row=2, column=2 )
b7.grid(row=1, column=0 )
b8.grid(row=1, column=1 )
b9.grid(row=1, column=2 )

b0.grid(row=4, column=0 )
b_clr.grid(row=4, column=1,columnspan=2)
b_eq.grid(row=5, column=1,columnspan=2)
b_add.grid(row=5, column=0 )

b_sub.grid(row=6, column=0 )
b_mul.grid(row=6, column=1 )
b_div.grid(row=6, column=2 )


root.mainloop()