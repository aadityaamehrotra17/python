#importing module
from tkinter import *

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
    canvas1 = Canvas(canvas, width=1280, height=720, background="#04BFCD")
    canvas.create_window(640, 360, anchor=CENTER, window=canvas1)

#adding elements to the canvas
label = Label(canvas, width=15, text='Enter your name:', font=('Helvetica', 16), bg='#04BFCD')
canvas.create_window(632, 325, anchor=E, window=label)
entry = Entry(canvas, width=20, font=('Helvetica', 24),)
canvas.create_window(640, 360, anchor=CENTER, window=entry)
button = Button(canvas, width=10, text="Start", fg='white', bg='black', font=('Helvetica', 16), command=click)
canvas.create_window(640, 420, anchor=CENTER, window=button)

#running the mainloop
screen.mainloop()