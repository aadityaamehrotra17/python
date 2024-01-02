#importing modules
from tkinter import *
import random
import os
from PIL import Image, ImageTk

#declaring variables
score = 0       
frame = 20
list=[]

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
    canvas1.after(1000, end_canvas)
    
#adding elements to the canvas
label = Label(canvas, width=15, text='Enter your name:', font=('Helvetica', 16), bg='#04BFCD')
canvas.create_window(632, 325, anchor=E, window=label)
entry = Entry(canvas, width=20, font=('Helvetica', 24))
canvas.create_window(640, 360, anchor=CENTER, window=entry)
button = Button(canvas, width=10, text="Start", fg='white', bg='black', font=('Helvetica', 16), command=click)
canvas.create_window(640, 420, anchor=CENTER, window=button)

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

#running the mainloop
screen.mainloop()