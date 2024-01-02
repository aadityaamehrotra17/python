#importing modules
from tkinter import *
import random
import os
from PIL import Image, ImageTk

#declaring variables
score = 0
frame = 20
list=[]
bx=150
by=300

#creating the main window
screen = Tk()
screen.resizable(width = False, height = False)
screen.title("Game Name")
screen.iconbitmap('avatar.ico')
screen.geometry('1280x720')

#creating the canvas
canvas = Canvas(screen, width = 1280, height = 720, background = "#04BFCD",)
canvas.pack()

#defining functions to open the next canvas
def click():
    button.config(state=DISABLED)  
    entry.config(state=DISABLED)  
    label.config(text="Loading...           ", font=('Helvetica', 16))  
    canvas.after(1000, open_canvas1)
def open_canvas1():
    global name
    name = entry.get()
    global canvas1
    canvas1 = Canvas(canvas, width=1280, height=720, background="#04BFCD")
    canvas.create_window(640, 360, anchor=CENTER, window=canvas1)
    #adding elements to canvas1
    global img, bat
    img = PhotoImage(file="bat.gif")
    bat = canvas1.create_image(bx, by, image=img)
   
#adding elements to the canvas
label = Label(canvas, width=15, text='Enter your name:', font=('Helvetica', 16), bg='#04BFCD')
canvas.create_window(632, 325, anchor=E, window=label)
entry = Entry(canvas, width=20, font=('Helvetica', 24))
canvas.create_window(640, 360, anchor=CENTER, window=entry)
button = Button(canvas, width=10, text="Start", fg='white', bg='black', font=('Helvetica', 16), command=click)
canvas.create_window(640, 420, anchor=CENTER, window=button)

#bat controls
def up(event=None):
    global by
    if by>55:
        by-=20
        canvas1.coords(bat, bx, by)
def down(event=None):
    global by
    if by<665:
        by+=20
        canvas1.coords(bat, bx, by)
screen.bind("<Up>", up)
screen.bind("<Down>", down)

#creating the end screen
def end_canvas():
    global canvas2
    canvas2 = Canvas(canvas1, width=1280, height=720, background="#04BFCD")
    canvas1.create_window(640, 360, anchor=CENTER, window=canvas2)
    global scoreboard
    scoreboard = canvas2.create_rectangle(400, 50, 880, 670, fill="#04BFCD", outline="#2B8ED5", width=5)
    global textvar
    global label1
    textvar = "Your score is: " + str(score)
    label1 = Label(canvas2, width=15, text=textvar, font=('Helvetica', 16), bg='#04BFCD')
    canvas2.create_window(730, 80, anchor=E, window=label1)
    #printing list
    list.append([name,score])
    global y,i
    i=1
    y=125
    for j in sorted(list, key = lambda x: x[1], reverse=True):
        label2 = Label(canvas2, width=15, text=j[0], font=('Helvetica', 16), bg='#04BFCD')
        canvas2.create_window(590, y, anchor=E, window=label2)
        label3 = Label(canvas2, width=15, text=str(j[1]), font=('Helvetica', 16), bg='#04BFCD')
        canvas2.create_window(878, y, anchor=E, window=label3)
        y+=55
        i+=1
        if i==11:
            break

#creating the bosskey
def bosskey(event=None):
    global canvasb
    canvasb = Canvas(canvas, width=1280, height=720, background="#FFFFFF")
    canvas.create_window(640, 360, anchor=CENTER, window=canvasb)
    canvasb.tkraise(canvasb._name)
screen.bind("<Escape>", bosskey)

#running the mainloop
screen.mainloop()