#importing modules
from tkinter import *
import random
import os
from PIL import Image, ImageTk
import pickle

def is_file_empty(file_path):
    return os.stat(file_path).st_size == 0

#save and load game
def save_game(name, score, bx, by, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, retro):
    global buttonsave,canvas1
    buttonsave.config(text="Saved", state=DISABLED)
    state = {
        'name': name,
        'score': score,
        'bx': bx,
        'by': by,
        'obstacle_x1': obstacle_x1,
        'obstacle_x2': obstacle_x2,
        'hole1': hole1,
        'hole2': hole2,
        'hole3': hole3,
        'hole4': hole4,
        'retro': retro,
    }
    with open('save.dat', 'wb') as f:
        pickle.dump(state, f)
    canvas1.after(1000, end_canvas)
def load_game():
    global name, score, bx, by, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, retro, buttonload
    if is_file_empty('save.dat'):
        buttonload.config(text="No Data", state=DISABLED)
    else:
        with open('save.dat', 'rb') as f:
            state = pickle.load(f)
        name = state['name']
        score = state['score']
        bx = state['bx']
        by = state['by']
        obstacle_x1 = state['obstacle_x1']
        obstacle_x2 = state['obstacle_x2']
        hole1 = state['hole1']
        hole2 = state['hole2']
        hole3 = state['hole3']
        hole4 = state['hole4']
        retro = state['retro']
        screen.bind("<space>", paused)
        open_canvas1()

#creating the main window
screen = Tk()
screen.resizable(width = False, height = False)
screen.title("Bat Blitz")
screen.iconbitmap('avatar.ico')
screen.geometry('1280x720')

#declaring variables
retro = False
cheat = False
list=[]
bx=150
by=300
pause = False
name = textvar = ''
y = score = 0
frame = 20
obstacle_x1 = 600
obstacle_x2 = 1400
hole1 = hole2 = hole3 = hole4 = 0
img = PhotoImage(file="bat.gif")
cloud1 = PhotoImage(file="cloud.gif")
cloud2 = PhotoImage(file="cloud.gif")
bg = PhotoImage(file="bg.gif")
(canvas, label, entry, button, button2, buttone, button3, button4, buttonsave, buttonload, pic, labelt, canvas1, canvasm, pib, pibb, pibbb, picc, piccc, bgg, canvasb, label1, labelm, button5, buttonp, buttonr, canvas2, scoreboard, c1, c2, bat, display, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, label2) = (None,) * 39

#defining functions to open the next canvas
def click():
    if entry.get().strip() != "":
        button.config(state=DISABLED)
        button2.config(state=DISABLED)  
        entry.config(state=DISABLED)  
        label.config(text="Loading...           ", font=('Helvetica', 16))  
        canvas.after(1000, open_canvas1)
    else:
        label.config(text=" Name is required!", font=('Helvetica', 16))
def click2():
    global retro
    retro = True
    if entry.get().strip() != "":
        button.config(state=DISABLED) 
        button2.config(state=DISABLED) 
        entry.config(state=DISABLED)  
        label.config(text="Loading...           ", font=('Helvetica', 16))  
        canvas.after(1000, open_canvas1)
    else:
        label.config(text=" Name is required!", font=('Helvetica', 16))

#pop up for controls
def controls():
    global canvasm, canvas, button5, labelm
    canvasm = Canvas(canvas, width=1280, height=720, background="turquoise")
    canvas.create_window(640, 360, anchor=CENTER, window=canvasm)
    button5 = Button(canvas, width=5, text="Exit", fg='red', bg='black', font=('Helvetica', 16), command=canvasm.destroy)
    canvasm.create_window(1220, 50, anchor=CENTER, window=button5)
    labelm = Label(canvasm, width=50, text='Pause/Resume: <Space>\n\nBosskey: <Enter/Return>\n\nExit Bosskey: <Escape>\n\nCheatcode: <C>\n\nUp: <Up-Arrow> [Regular] | <W> [Retro]\n\nUltra Cheatcode: <Left-Arrow & Right-Arrow>', font=('Helvetica', 32), bg='turquoise')
    canvasm.create_window(640, 360, anchor=CENTER, window=labelm)

controller_image = Image.open("controller.png")
controller_imagee = ImageTk.PhotoImage(controller_image)
def home_canvas():
    global canvas, label, entry, button, button2, button3, button4, labelt, buttonload, pic, picc, piccc, pib, pibb, pibbb
    #creating the home canvas
    canvas = Canvas(screen, width = 1280, height = 720, background = "#04BFCD",)
    canvas.pack()
    #adding elements to the home canvas
    label = Label(canvas, width=15, text='Enter your name:', font=('Helvetica', 16), bg='#04BFCD')
    canvas.create_window(632, 325, anchor=E, window=label)
    entry = Entry(canvas, width=20, font=('Helvetica', 24))
    canvas.create_window(640, 360, anchor=CENTER, window=entry)
    button = Button(canvas, width=10, text="Start", fg='black', bg='white', font=('Helvetica', 16), command=click)
    canvas.create_window(554, 420, anchor=CENTER, window=button)
    button2 = Button(canvas, width=10, text="Retro", fg='white', bg='black', font=('Helvetica', 16), command=click2)
    canvas.create_window(726, 420, anchor=CENTER, window=button2)
    button3 = Button(canvas, width=5, text="Quit", fg='red', bg='white', font=('Helvetica', 16), command=screen.destroy)
    canvas.create_window(1220, 40, anchor=CENTER, window=button3)
    button4 = Button(canvas, width=5, text="Help", fg='white', bg='red', font=('Helvetica', 16), command=controls)
    canvas.create_window(1220, 90, anchor=CENTER, window=button4)
    labelt = Label(canvas, width=40, text='BAT BLITZ', font=('Impact', 96), fg='turquoise', bg='#04BFCD')
    canvas.create_window(640, 200, anchor=CENTER, window=labelt)
    buttonload = Button(canvas, width=10, text="Load Latest", fg='black', bg='white', font=('Helvetica', 16), command=load_game)
    canvas.create_window(80, 40, anchor=CENTER, window=buttonload)
    pic = canvas.create_image(60, 580, anchor=CENTER, image=controller_imagee)
    picc = canvas.create_image(140, 630, anchor=CENTER, image=controller_imagee)
    piccc = canvas.create_image(220, 680, anchor=CENTER, image=controller_imagee)
    pib = canvas.create_image(1220, 580, anchor=CENTER, image=controller_imagee)
    pibb = canvas.create_image(1140, 630, anchor=CENTER, image=controller_imagee)
    pibbb = canvas.create_image(1060, 680, anchor=CENTER, image=controller_imagee)
home_canvas()

#cheat activation
def cheatcode(event=None):
    global cheat
    cheat = True
screen.bind("<c>", cheatcode)
keys_pressed = {'Left': False, 'Right': False}
def check_ultracheat(event):
    global score
    keys_pressed[event.keysym] = True
    if keys_pressed['Left'] and keys_pressed['Right']:
        score += 50
def key_release(event):
    keys_pressed[event.keysym] = False
screen.bind('<KeyPress-Left>', check_ultracheat)
screen.bind('<KeyPress-Right>', check_ultracheat)
screen.bind('<KeyRelease-Left>', key_release)
screen.bind('<KeyRelease-Right>', key_release)

#creating the pause key
def paused(event=None):
    global pause, buttonp, buttonr, buttonsave
    buttonp.config(state=DISABLED)
    buttonr.config(state=NORMAL)
    buttonsave.config(state=NORMAL)
    pause = True
    screen.bind("<space>", resume)  
screen.bind("<space>", paused)

#creating the resume key
def resume(event=None):
    global pause, buttonr, buttonp, buttonsave
    buttonr.config(state=DISABLED)
    buttonp.config(state=NORMAL)
    buttonsave.config(state=DISABLED)
    if pause:
        pause = False
        obstacle_motion()
        screen.bind("<space>", paused)  

#creating the main game canvas
def open_canvas1():
    global name, retro, canvas1, c1, c2, bat, buttonsave, display, buttonp, buttonr, obstacle_x1, obstacle_x2, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, hole1, hole2, hole3, hole4
    screen.bind("<space>", paused)
    if name=='':
        name = entry.get()
    hole1 = random.randint(0, 260)
    hole2 = random.randint(360, 620)
    hole3 = random.randint(0, 260)
    hole4 = random.randint(360, 620)
    if retro == True:
        canvas1 = Canvas(canvas, width=1280, height=720, background="#FFFFFF")
        canvas.create_window(640, 360, anchor=CENTER, window=canvas1)
        bat = canvas1.create_image(bx, by, image=img)
        display = canvas1.create_text(1255, 55, text=str(score), font=('Helvetica',64), fill='#000000', anchor=E)
        obstacle_up1 = canvas1.create_rectangle(obstacle_x1, 0, obstacle_x1 + 50, hole1, fill="#000000")
        obstacle_mid1 = canvas1.create_rectangle(obstacle_x1, hole1 + 100, obstacle_x1 + 50, hole2, fill="#000000")
        obstacle_down1 = canvas1.create_rectangle(obstacle_x1, hole2 + 100, obstacle_x1 + 50, 730, fill="#000000")
        obstacle_up2 = canvas1.create_rectangle(obstacle_x2, 0, obstacle_x2 + 50, hole3, fill="#000000")
        obstacle_mid2 = canvas1.create_rectangle(obstacle_x2, hole3 + 100, obstacle_x2 + 50, hole4, fill="#000000")
        obstacle_down2 = canvas1.create_rectangle(obstacle_x2, hole4 + 100, obstacle_x2 + 50, 730, fill="#000000")
        buttonp = Button(canvas1, width=5, text="Pause", fg='red', bg='black', font=('Helvetica', 16), command=paused)
        canvas1.create_window(60, 40, anchor=CENTER, window=buttonp)
        buttonr = Button(canvas1, width=6, text="Resume", fg='green', bg='white', font=('Helvetica', 16), command=resume)
        canvas1.create_window(60, 90, anchor=CENTER, window=buttonr)
        buttonsave = Button(canvas1, width=5, text="Save", fg='black', bg='white', font=('Helvetica', 16), state=DISABLED, command=lambda: save_game(name, score, bx, by, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, retro))
        canvas1.create_window(60, 140, anchor=CENTER, window=buttonsave)
        setup_bindings()
    else:    
        canvas1 = Canvas(canvas, width=1280, height=720, background="#04BFCD")
        canvas.create_window(640, 360, anchor=CENTER, window=canvas1)
        c1 = canvas1.create_image(400, 120, image=cloud1)
        c2 = canvas1.create_image(1000, 200, image=cloud2)
        bat = canvas1.create_image(bx, by, image=img)
        display = canvas1.create_text(1255, 55, text=str(score), font=('Helvetica',64), fill='#000000', anchor=E)
        obstacle_up1 = canvas1.create_rectangle(obstacle_x1, 0, obstacle_x1 + 50, hole1, fill="#5A3AB6")
        obstacle_mid1 = canvas1.create_rectangle(obstacle_x1, hole1 + 100, obstacle_x1 + 50, hole2, fill="#5A3AB6")
        obstacle_down1 = canvas1.create_rectangle(obstacle_x1, hole2 + 100, obstacle_x1 + 50, 730, fill="#5A3AB6")
        obstacle_up2 = canvas1.create_rectangle(obstacle_x2, 0, obstacle_x2 + 50, hole3, fill="#5A3AB6")
        obstacle_mid2 = canvas1.create_rectangle(obstacle_x2, hole3 + 100, obstacle_x2 + 50, hole4, fill="#5A3AB6")
        obstacle_down2 = canvas1.create_rectangle(obstacle_x2, hole4 + 100, obstacle_x2 + 50, 730, fill="#5A3AB6")
        buttonp = Button(canvas1, width=5, text="Pause", fg='red', bg='black', font=('Helvetica', 16), command=paused)
        canvas1.create_window(60, 40, anchor=CENTER, window=buttonp)
        buttonr = Button(canvas1, width=6, text="Resume", fg='green', bg='white', font=('Helvetica', 16), command=resume)
        canvas1.create_window(60, 90, anchor=CENTER, window=buttonr)
        buttonsave = Button(canvas1, width=5, text="Save", fg='black', bg='white', font=('Helvetica', 16), state=DISABLED, command=lambda: save_game(name, score, bx, by, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, retro))
        canvas1.create_window(60, 140, anchor=CENTER, window=buttonsave)
        setup_bindings()
    gravity()
    obstacle_motion()

#defining function for obstacle motion    
def obstacle_motion():
    global obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, cheat, score, pause, frame, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, canvas1, display
    if cheat == True:
        score += 5
    canvas1.itemconfig(display, text=str(score))
    obstacle_x1 -= 5
    obstacle_x2 -= 5
    canvas1.coords(obstacle_up1, obstacle_x1, 0, obstacle_x1 + 50, hole1)
    canvas1.coords(obstacle_mid1, obstacle_x1, hole1 + 100, obstacle_x1 + 50, hole2)
    canvas1.coords(obstacle_down1, obstacle_x1, hole2 + 100, obstacle_x1 + 50, 730)
    canvas1.coords(obstacle_up2, obstacle_x2, 0, obstacle_x2 + 50, hole3)
    canvas1.coords(obstacle_mid2, obstacle_x2, hole3 + 100, obstacle_x2 + 50, hole4)
    canvas1.coords(obstacle_down2, obstacle_x2, hole4 + 100, obstacle_x2 + 50, 730)
    if obstacle_x1 <= -50:
        score += 1
        canvas1.itemconfig(display, text=str(score))
        obstacle_x1 = 1300
        hole1 = random.randint(0, 260)
        hole2 = random.randint(360, 620)  
    if obstacle_x2 <= -50:
        score += 1
        canvas1.itemconfig(display, text=str(score))
        obstacle_x2 = 1300
        hole3 = random.randint(0, 260)
        hole4 = random.randint(360, 620)
    cheat = False
    if pause == False:
        canvas1.after(frame, obstacle_motion)
        canvas1.after(frame, collision)

#defining function for collision detection
def collision():
    global pause, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, by, canvas1
    if 124 <= obstacle_x1 <= 178:
        if not ((hole1 < by < hole1 + 100) or (hole2 < by < hole2 + 100)):  
            pause = True
            canvas1.after(1000,end_canvas())
    if 124 <= obstacle_x2 <= 178:
        if not ((hole3 < by < hole3 + 100) or (hole4 < by < hole4 + 100)):  
            pause = True
            canvas1.after(1000,end_canvas())
    
#bat control up
def up(event=None):
    global by, bx, pause, canvas1, bat
    if canvas1 is not None and pause == False and by>55:
        by-=30
        canvas1.coords(bat, bx, by)

#gravity function
def gravity():
    global by, bx, pause, canvas1, bat
    if canvas1 is not None and pause == False and by < 696:
        by += 5
        canvas1.coords(bat, bx, by)
    canvas1.after(50, gravity)

#binding the keys
def setup_bindings():
    if retro == False:
        screen.bind("<Up>", up)
    else:
        screen.bind("<w>", up)

#defining function to restart the game
def restart_game():
    global canvas2, canvas1, canvas, retro, cheat, list, bx, by, pause, name, textvar, y, score, buttonsave, buttonload, frame, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, img, cloud1, cloud2, bg, label, entry, button, button2, buttone, button3, button4, labelt, canvasm, bgg, canvasb, label1, labelm, button5, buttonp, buttonr, scoreboard, c1, c2, bat, display, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, label2, pic, picc, piccc, pib, pibb, pibbb
    canvas2.destroy()
    canvas1.destroy()
    canvas.destroy()
    retro = False
    cheat = False
    list=[]
    bx=150
    by=300
    pause = False
    name = textvar = ""
    y = score = 0
    frame = 20
    obstacle_x1 = 600
    obstacle_x2 = 1400
    hole1 = hole2 = hole3 = hole4 = 0
    img = PhotoImage(file="bat.gif")
    cloud1 = PhotoImage(file="cloud.gif")
    cloud2 = PhotoImage(file="cloud.gif")
    bg = PhotoImage(file="bg.gif")
    (canvas, label, entry, button, button2, buttone, button3, button4, labelt, canvas1, pic, canvasm, buttonsave, bgg, canvasb, label1, labelm, button5, buttonp, buttonr, canvas2, scoreboard, c1, c2, bat, display, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, picc, piccc, label2, pib, pibb, pibbb) = (None,) * 38
    home_canvas()

#creating the end canvas
def end_canvas():
    global canvas2, canvas1, scoreboard, textvar, label1, buttone, list, y, name, score, label2
    canvas1.delete("all")
    canvas2 = Canvas(canvas1, width=1280, height=720, background="#04BFCD")
    canvas1.create_window(640, 360, anchor=CENTER, window=canvas2)
    scoreboard = canvas2.create_rectangle(400, 50, 880, 670, fill="#04BFCD", outline="#2B8ED5", width=5)
    textvar = "Your score is: " + str(score)
    label1 = Label(canvas2, width=15, text=textvar, font=('Helvetica', 16), bg='#04BFCD')
    canvas2.create_window(730, 80, anchor=E, window=label1)
    buttone = Button(canvas2, width=10, text="Home", fg='green', bg='white', font=('Helvetica', 16), command=restart_game)
    canvas2.create_window(640, 670, anchor=CENTER, window=buttone)
    leaderboard(name, score)
    leaderboard_display()

#function to save score to leaderboard
def leaderboard(name, score):
    data=[]
    with open('leaderboard.txt', 'r') as file:
        data = file.readlines()
    player_data = [line for line in data if line.split(":")[0] == name]
    if player_data:
        old_score = int(player_data[0].split(": ")[1])
        if score <= old_score:
            return
    data = [line for line in data if line.split(":")[0] != name]  # Remove old score
    player = f"{name}: {score}\n"
    data.append(player)  # Add new score
    data = sorted(data, key=lambda x: int(x.split(': ')[1]), reverse=True)
    with open('leaderboard.txt', 'w') as file:
        file.writelines(data[:10])

#function to display the leaderboard at the end of the game
def leaderboard_display():
    leaders = []
    with open('leaderboard.txt', 'r') as file:
        leaders = file.readlines()
    y=125
    for i, j in enumerate(leaders[:10], start=1):
        label2 = Label(canvas2, width=15, text=f"{i}. {j}", font=('Helvetica', 16), bg='#04BFCD')
        canvas2.create_window(590, y, anchor=E, window=label2)
        y+=55

#creating the bosskey
def bosskey(event=None):
    global pause, canvasb, bg, bgg, canvas
    pause = True
    canvasb = Canvas(canvas, width=1280, height=720, background="#FFFFFF")
    canvas.create_window(640, 360, anchor=CENTER, window=canvasb)
    bg = PhotoImage(file="bg.gif")
    bgg = canvasb.create_image(640, 360, anchor=CENTER, image=bg)
    canvasb.tkraise(canvasb._name)
screen.bind("<Return>", bosskey)

#returning to the game
def back(event=None):
    global pause, canvasb
    if pause:
        pause = False
        canvasb.destroy()
        obstacle_motion()
        screen.bind("<space>", paused)
screen.bind("<Escape>", back)

#running the mainloop
screen.mainloop()