import tkinter as tk
from tkinter import *
from tkinter import  messagebox
import  random
from random import shuffle

answers = ["America","India","Russia","Hello","Paris"]

ques = []

for i in answers:
    words = list(i)
    shuffle(words)
    ques.append(words)

num = random.randint(0, len(ques)-1)

def initial():
    global ques, num
    l1.configure(text=ques[num]) #configure to display the questions

def anscheck():
    global ques, num, answers
    userin = e1.get() #get the answer typed in the text box
    if userin == answers[num]:
        messagebox.showinfo('RESULT','Correct Answer :)')
    else:
        messagebox.showinfo('RESULT','Wrong Answer :/')
        e1.delete(0,END)

def resetswitch():
    global ques,answers,num
    num = random.randint(0, len(ques)-1)
    l1.configure(text=ques[num])
    e1.delete(0,END)


win = tk.Tk()
win.geometry("400x400")
win.config(background='#0D0D0D')

win.title("Jumby")
#win.iconbitmap(r'dicon.ico')
#win.tk.call('wm', 'iconphoto', win._w, tk.PhotoImage(file='/Users/lenovo/Desktop/My Projects/GUI/dicon.ico'))
win.iconphoto(False, tk.PhotoImage(file='/Users/lenovo/Desktop/My Projects/GUI/dicon.ico'))

#bg is background, fg is foreground
l1 = Label(win,width=15, font='times 20', bg='#242B2E', fg='#DDD101')
l1.pack(pady=30, ipady=10, padx=10) #ipady represents internal for y axis, pady represents y-axis and padx x-axis

answer = StringVar()
e1 = Entry(win, textvariable=answer, borderwidth = 10)
e1.pack(ipady=5, ipadx=5)

b1 = Button(win, text="Check", width=20, borderwidth = 10, command=anscheck, bg='#FF6666', fg='#120E43')
b1.pack(pady=30)

b2 = Button(win, text="Reset", width=20, borderwidth = 10, command=resetswitch, bg='#50DBB4', fg='#03203C')
b2.pack()


initial()
win.mainloop()
