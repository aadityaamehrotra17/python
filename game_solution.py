#resolution: 1280x720
#author: Aadityaa Mehrotra

#importing modules
from tkinter import *       #for GUI
import random       #for randomizing the holes
import os       #for checking if file is empty
from PIL import Image, ImageTk      #for controller image
import pickle       #for saving and loading game

#checking if file is empty
def is_file_empty(file_path):       
    return os.stat(file_path).st_size == 0      #returns true if file is empty

#save and load game
def save_game(name, score, bx, by, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, retro):
    global buttonsave,canvas1       #declaring global variables
    buttonsave.config(text="Saved", state=DISABLED)     #changing the text of the save button
    state = {       #creating a dictionary of the variables to be saved
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
    screen.unbind("<space>")        #unbinding the space key
    with open('save.dat', 'wb') as f:      #opening the file in write binary mode
        pickle.dump(state, f)
    canvas1.after(1000, end_canvas)     #calling the end canvas after 1 second

def load_game():
    global name, score, bx, by, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, retro, buttonload     #declaring global variables
    if is_file_empty('save.dat'):      #checking if file is empty
        buttonload.config(text="No Data", state=DISABLED)       #changing the text and state of the load button
    else:
        with open('save.dat', 'rb') as f:      #opening the file in read binary mode
            state = pickle.load(f)      #loading the saved variables
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
        screen.bind("<space>", paused)      #binding the space key to the pause function
        open_canvas1()      #opening the main game canvas

#creating the main window
screen = Tk()
screen.resizable(width = False, height = False)     #disabling window resizing
screen.title("Bat Blitz")
screen.iconbitmap('avatar.ico')
screen.geometry('1280x720')

#declaring variables
retro = False       #variable to check if retro mode is on
cheat = False       #variable to check if cheat mode is on
bx=150      #x coordinate of bat
by=300      #y coordinate of bat
pause = False       #variable to check if game is paused
name = textvar = ''     #name of player and text to be displayed on end canvas
y = score = 0       #score and additional counter variable for leaderboard display
frame = 20      #frame rate
obstacle_x1 = 600       #x coordinate of obstacle 1
obstacle_x2 = 1400      #x coordinate of obstacle 2
hole1 = hole2 = hole3 = hole4 = 0       #sample y coordinates of holes
img = PhotoImage(file="bat.gif")        #bat image
cloud1 = PhotoImage(file="cloud.gif")       #cloud image
cloud2 = PhotoImage(file="cloud.gif")       #cloud image
bg = PhotoImage(file="bg.gif")      #background image for bosskey
#declaring every other variable used in the program (within functions) as None to keep track of them
(canvas, label, entry, button, button2, button_home, button3, button4, buttonsave, buttonload, pic1, labelt, canvas1, controlscanvas, pic4, pic5, pic6, pic2, pic3, background_image, bosscanvas, label1, labelcontrols, button5, buttonp, buttonr, canvas2, scoreboard, c1, c2, bat, display, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, label2) = (None,) * 39

#defining functions to open the next canvas
def click():
    global retro        #declaring global variable
    retro = False       #setting retro mode to false
    if entry.get().strip() != "":       #checking if name is entered
        button.config(state=DISABLED)       #disabling the button
        button2.config(state=DISABLED)      #disabling the button  
        entry.config(state=DISABLED)        #disabling the entry box  
        label.config(text="Loading...           ", font=('Helvetica', 16))      #changing the text of the label  
        canvas.after(1000, open_canvas1)        #calling the main game canvas after 1 second
    else:
        label.config(text=" Name is required!", font=('Helvetica', 16))     #changing the text of the label

def click2():
    global retro        #declaring global variable
    retro = True        #setting retro mode to true
    if entry.get().strip() != "":       #checking if name is entered
        button.config(state=DISABLED)       #disabling the button 
        button2.config(state=DISABLED)      #disabling the button 
        entry.config(state=DISABLED)        #disabling the entry box  
        label.config(text="Loading...           ", font=('Helvetica', 16))      #changing the text of the label  
        canvas.after(1000, open_canvas1)        #calling the main game canvas after 1 second
    else:
        label.config(text=" Name is required!", font=('Helvetica', 16))     #changing the text of the label

#pop up for controls
def controls():
    global controlscanvas, canvas, button5, labelcontrols     #declaring global variables
    controlscanvas = Canvas(canvas, width=1280, height=720, background="turquoise")        #creating the canvas
    canvas.create_window(640, 360, anchor=CENTER, window=controlscanvas)       
    button5 = Button(canvas, width=5, text="Exit", fg='red', bg='black', font=('Helvetica', 16), command=controlscanvas.destroy)       #creating the exit button
    controlscanvas.create_window(1220, 50, anchor=CENTER, window=button5)
    labelcontrols = Label(controlscanvas, width=50, text='Pause/Resume: <Space>\n\nBosskey: <Enter/Return>\n\nExit Bosskey: <Escape>\n\nCheatcode: <C>\n\nUp: <Up-Arrow> [Regular] | <W> [Retro]\n\nUltra Cheatcode: <Left-Arrow & Right-Arrow>\n\nBeware: Higher the score, faster the game!', font=('Helvetica', 32), bg='turquoise')     #creating the label
    controlscanvas.create_window(640, 360, anchor=CENTER, window=labelcontrols)

controller_image = Image.open("controller.png")     #opening the controller image
controller_imagee = ImageTk.PhotoImage(controller_image)        #converting the image to tkinter format

#creating the home canvas
def home_canvas():
    global canvas, label, entry, button, button2, button3, button4, labelt, buttonload, pic1, pic2, pic3, pic4, pic5, pic6      #declaring global variables
    canvas = Canvas(screen, width = 1280, height = 720, background = "#04BFCD",)        #creating the canvas
    canvas.pack()
    #adding elements to the home canvas
    label = Label(canvas, width=15, text='Enter your name:', font=('Helvetica', 16), bg='#04BFCD')      #creating the label
    canvas.create_window(632, 325, anchor=E, window=label)
    entry = Entry(canvas, width=20, font=('Helvetica', 24))     #creating the entry box
    canvas.create_window(640, 360, anchor=CENTER, window=entry)
    button = Button(canvas, width=10, text="Start", fg='black', bg='white', font=('Helvetica', 16), command=click)      #creating the start button      
    canvas.create_window(554, 420, anchor=CENTER, window=button)
    button2 = Button(canvas, width=10, text="Retro", fg='white', bg='black', font=('Helvetica', 16), command=click2)        #creating the retro button
    canvas.create_window(726, 420, anchor=CENTER, window=button2)
    button3 = Button(canvas, width=5, text="Quit", fg='red', bg='white', font=('Helvetica', 16), command=screen.destroy)        #creating the quit button
    canvas.create_window(1220, 40, anchor=CENTER, window=button3)
    button4 = Button(canvas, width=5, text="Help", fg='white', bg='red', font=('Helvetica', 16), command=controls)      #creating the help button
    canvas.create_window(1220, 90, anchor=CENTER, window=button4)
    labelt = Label(canvas, width=40, text='BAT BLITZ', font=('Impact', 96), fg='turquoise', bg='#04BFCD')       #creating the title label
    canvas.create_window(640, 200, anchor=CENTER, window=labelt)
    buttonload = Button(canvas, width=10, text="Load Latest", fg='black', bg='white', font=('Helvetica', 16), command=load_game)        #creating the load button
    canvas.create_window(80, 40, anchor=CENTER, window=buttonload)
    pic1 = canvas.create_image(60, 580, anchor=CENTER, image=controller_imagee)      #creating the controller images
    pic2 = canvas.create_image(140, 630, anchor=CENTER, image=controller_imagee)
    pic3 = canvas.create_image(220, 680, anchor=CENTER, image=controller_imagee)
    pic4 = canvas.create_image(1220, 580, anchor=CENTER, image=controller_imagee)
    pic5 = canvas.create_image(1140, 630, anchor=CENTER, image=controller_imagee)
    pic6 = canvas.create_image(1060, 680, anchor=CENTER, image=controller_imagee)
home_canvas()

#cheat activation
def cheatcode(event=None):
    global cheat        #declaring global variable
    cheat = True        #setting cheat mode to true
screen.bind("<c>", cheatcode)       #binding the c key to the cheatcode function
keys_pressed = {'Left': False, 'Right': False}      #dictionary to check if both left and right keys are pressed

def check_ultracheat(event):        #function to check if both left and right keys are pressed
    global score        #declaring global variable
    keys_pressed[event.keysym] = True       #setting the keys pressed to true
    if keys_pressed['Left'] and keys_pressed['Right']:      #checking if both keys are pressed
        score += 50     #adding 50 to the score

def key_release(event):     #function to check if both left and right keys are released
    keys_pressed[event.keysym] = False      #setting the keys pressed to false
    
screen.bind('<KeyPress-Left>', check_ultracheat)        #binding the left and right keys to the check_ultracheat and key_release functions
screen.bind('<KeyPress-Right>', check_ultracheat)
screen.bind('<KeyRelease-Left>', key_release)
screen.bind('<KeyRelease-Right>', key_release)

#creating the pause key
def paused(event=None):
    global pause, buttonp, buttonr, buttonsave      #declaring global variables
    buttonp.config(state=DISABLED)      #disabling the pause button
    buttonr.config(state=NORMAL)        #enabling the resume button
    buttonsave.config(state=NORMAL)     #enabling the save button
    pause = True        #setting pause to true
    screen.bind("<space>", resume)          #binding the space key to the resume function
    screen.unbind("<c>")        #unbinding the cheat keys
    screen.unbind('<KeyPress-Left>')        
    screen.unbind('<KeyPress-Right>')
    screen.unbind('<KeyRelease-Left>')
    screen.unbind('<KeyRelease-Right>')
screen.bind("<space>", paused)      #binding the space key to the pause function

#creating the resume key
def resume(event=None):
    global pause, buttonr, buttonp, buttonsave      #declaring global variables
    buttonr.config(state=DISABLED)      #disabling the resume button
    buttonp.config(state=NORMAL)        #enabling the pause button
    buttonsave.config(state=DISABLED)       #disabling the save button
    if pause:       #checking if game is paused
        pause = False       #setting pause to false
        obstacle_motion()       #calling the obstacle motion function
        screen.bind("<space>", paused)          #binding the space key to the pause function
    screen.bind("<c>", cheatcode)       #binding the cheat keys
    screen.bind('<KeyPress-Left>', check_ultracheat)        
    screen.bind('<KeyPress-Right>', check_ultracheat)
    screen.bind('<KeyRelease-Left>', key_release)
    screen.bind('<KeyRelease-Right>', key_release)

#creating the main game canvas
def open_canvas1():
    global name, retro, canvas1, c1, c2, bat, buttonsave, display, buttonp, buttonr, obstacle_x1, obstacle_x2, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, hole1, hole2, hole3, hole4     #declaring global variables
    screen.bind("<space>", paused)      #binding the space key to the pause function
    if name=='':        #checking if name is entered
        name = entry.get()      #getting name from entry box
    hole1 = random.randint(0, 260)      #randomizing the y coordinates of the holes
    hole2 = random.randint(360, 620)
    hole3 = random.randint(0, 260)
    hole4 = random.randint(360, 620)
    if retro == True:       #checking if retro mode is on
        canvas1 = Canvas(canvas, width=1280, height=720, background="#FFFFFF")      #creating the canvas
        canvas.create_window(640, 360, anchor=CENTER, window=canvas1)
        bat = canvas1.create_image(bx, by, image=img)       #creating the bat image
        display = canvas1.create_text(1255, 55, text=str(score), font=('Helvetica',64), fill='#000000', anchor=E)       #creating the score display
        obstacle_up1 = canvas1.create_rectangle(obstacle_x1, 0, obstacle_x1 + 50, hole1, fill="#000000")        #creating the obstacles
        obstacle_mid1 = canvas1.create_rectangle(obstacle_x1, hole1 + 100, obstacle_x1 + 50, hole2, fill="#000000")
        obstacle_down1 = canvas1.create_rectangle(obstacle_x1, hole2 + 100, obstacle_x1 + 50, 730, fill="#000000")
        obstacle_up2 = canvas1.create_rectangle(obstacle_x2, 0, obstacle_x2 + 50, hole3, fill="#000000")
        obstacle_mid2 = canvas1.create_rectangle(obstacle_x2, hole3 + 100, obstacle_x2 + 50, hole4, fill="#000000")
        obstacle_down2 = canvas1.create_rectangle(obstacle_x2, hole4 + 100, obstacle_x2 + 50, 730, fill="#000000")
        buttonp = Button(canvas1, width=5, text="Pause", fg='red', bg='black', font=('Helvetica', 16), command=paused)      #creating the pause button
        canvas1.create_window(60, 40, anchor=CENTER, window=buttonp)
        buttonr = Button(canvas1, width=6, text="Resume", fg='green', bg='white', font=('Helvetica', 16), command=resume)       #creating the resume button
        canvas1.create_window(60, 90, anchor=CENTER, window=buttonr)
        buttonsave = Button(canvas1, width=5, text="Save", fg='black', bg='white', font=('Helvetica', 16), state=DISABLED, command=lambda: save_game(name, score, bx, by, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, retro))     #creating the save button
        canvas1.create_window(60, 140, anchor=CENTER, window=buttonsave)
        setup_bindings()        #calling the function to bind the keys
    else:       #if retro mode is off
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
    gravity()       #calling the gravity function
    obstacle_motion()       #calling the obstacle motion function

#defining function for obstacle motion    
def obstacle_motion():
    global obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, cheat, score, pause, frame, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, canvas1, display     #declaring global variables
    if cheat == True:       #checking if cheat mode is on
        score += 5      #adding 5 to the score
    canvas1.itemconfig(display, text=str(score))        #updating the score display
    obstacle_x1 -= 5        #moving the obstacles
    obstacle_x2 -= 5
    canvas1.coords(obstacle_up1, obstacle_x1, 0, obstacle_x1 + 50, hole1)
    canvas1.coords(obstacle_mid1, obstacle_x1, hole1 + 100, obstacle_x1 + 50, hole2)
    canvas1.coords(obstacle_down1, obstacle_x1, hole2 + 100, obstacle_x1 + 50, 730)
    canvas1.coords(obstacle_up2, obstacle_x2, 0, obstacle_x2 + 50, hole3)
    canvas1.coords(obstacle_mid2, obstacle_x2, hole3 + 100, obstacle_x2 + 50, hole4)
    canvas1.coords(obstacle_down2, obstacle_x2, hole4 + 100, obstacle_x2 + 50, 730)
    if obstacle_x1 <= -50:      #checking if obstacle 1 is out of the screen
        score += 1      #adding 1 to the score
        canvas1.itemconfig(display, text=str(score))        #updating the score display
        obstacle_x1 = 1300      #resetting the x coordinate of obstacle 1
        hole1 = random.randint(0, 260)      #randomizing the y coordinates of the holes
        hole2 = random.randint(360, 620)  
    if obstacle_x2 <= -50:      #checking if obstacle 2 is out of the screen
        score += 1
        canvas1.itemconfig(display, text=str(score))
        obstacle_x2 = 1300
        hole3 = random.randint(0, 260)
        hole4 = random.randint(360, 620)
    cheat = False       #setting cheat mode to false
    if score%5==0 and score!=0 and frame>5:     #checking if score is a multiple of 5 and is not 0 and frame rate is greater than 5
                frame-=1        #making the game faster
    if pause == False:      #checking if game is paused 
        canvas1.after(frame, obstacle_motion)       #calling the obstacle motion function
        canvas1.after(frame, collision)     #calling the collision function

#defining function for collision detection
def collision():
    global pause, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, by, canvas1     #declaring global variables
    if 124 <= obstacle_x1 <= 178:       #checking if bat is in the range of obstacle 1
        if not ((hole1 < by < hole1 + 100) or (hole2 < by < hole2 + 100)):      #checking if bat is in the hole  
            pause = True        #setting pause to true
            end_canvas()        #calling the end canvas
    if 124 <= obstacle_x2 <= 178:       #checking if bat is in the range of obstacle 2
        if not ((hole3 < by < hole3 + 100) or (hole4 < by < hole4 + 100)):          #checking if bat is in the hole
            pause = True        #setting pause to true
            end_canvas()        #calling the end canvas
    
#bat control up
def up(event=None):
    global by, bx, pause, canvas1, bat      #declaring global variables
    if canvas1 is not None and pause == False and by>55:        #checking if game is not paused and bat is not at the top
        by-=30    #moving the bat up
        canvas1.coords(bat, bx, by)     #updating the bat coordinates

#gravity function
def gravity():
    global by, bx, pause, canvas1, bat      #declaring global variables
    if canvas1 is not None and pause == False and by < 696:     #checking if game is not paused and bat is not at the bottom
        by += 5     #moving the bat down
        canvas1.coords(bat, bx, by)     #updating the bat coordinates
    canvas1.after(50, gravity)      #calling the gravity function

#binding the keys
def setup_bindings():
    if retro == False:      #checking if retro mode is off
        screen.bind("<Up>", up)     #binding the up key to the up function
    else:
        screen.bind("<w>", up)      #binding the w key to the up function

#defining function to restart the game
def restart_game():
    global canvas2, canvas1, canvas, retro, cheat, bx, by, pause, name, textvar, y, score, buttonsave, buttonload, frame, obstacle_x1, obstacle_x2, hole1, hole2, hole3, hole4, img, cloud1, cloud2, bg, label, entry, button, button2, button_home, button3, button4, labelt, controlscanvas, background_image, bosscanvas, label1, labelcontrols, button5, buttonp, buttonr, scoreboard, c1, c2, bat, display, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, label2, pic1, pic2, pic3, pic4, pic5, pic6     #declaring global variables
    canvas2.destroy()       #destroying the end canvas
    canvas1.destroy()       #destroying the main game canvas
    canvas.destroy()        #destroying the home canvas
    retro = False       #setting retro mode to false
    cheat = False       #setting cheat mode to false
    bx=150      #setting all other variables to their initial values
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
    (canvas, label, entry, button, button2, button_home, button3, button4, labelt, canvas1, pic1, controlscanvas, buttonsave, background_image, bosscanvas, label1, labelcontrols, button5, buttonp, buttonr, canvas2, scoreboard, c1, c2, bat, display, obstacle_up1, obstacle_mid1, obstacle_down1, obstacle_up2, obstacle_mid2, obstacle_down2, pic2, pic3, label2, pic4, pic5, pic6) = (None,) * 38
    home_canvas()       #calling the home canvas

#creating the end canvas
def end_canvas():
    global canvas2, canvas1, scoreboard, textvar, label1, button_home, y, name, score, label2       #declaring global variables
    canvas1.delete("all")       #deleting all elements from the main game canvas
    canvas2 = Canvas(canvas1, width=1280, height=720, background="#04BFCD")     #creating the end canvas    
    canvas1.create_window(640, 360, anchor=CENTER, window=canvas2)
    scoreboard = canvas2.create_rectangle(400, 50, 880, 670, fill="#04BFCD", outline="#2B8ED5", width=5)        #creating the scoreboard
    textvar = "Your score is: " + str(score)        #creating the text to be displayed
    label1 = Label(canvas2, width=15, text=textvar, font=('Helvetica', 16), bg='#04BFCD')       #creating the label
    canvas2.create_window(730, 80, anchor=E, window=label1)
    button_home = Button(canvas2, width=10, text="Home", fg='green', bg='white', font=('Helvetica', 16), command=restart_game)      #creating the home button
    canvas2.create_window(640, 670, anchor=CENTER, window=button_home)
    leaderboard(name, score)        #calling the leaderboard function
    leaderboard_display()       #calling the leaderboard display function

#function to save score to leaderboard
def leaderboard(name, score):
    data=[]     #creating an empty list
    with open('leaderboard.txt', 'r') as file:     #opening the leaderboard file in read mode
        data = file.readlines()     #reading the lines of the file
    player_data = [line for line in data if line.split(":")[0] == name]     #checking if player is already in the leaderboard
    if player_data:     #if player is already in the leaderboard
        old_score = int(player_data[0].split(": ")[1])      #getting the old score
        if score <= old_score:      #checking if new score is less than old score
            return      #returning
    data = [line for line in data if line.split(":")[0] != name]        #removing the old score
    player = f"{name}: {score}\n"       #creating the new score
    data.append(player)     #adding the new score to the list
    data = sorted(data, key=lambda x: int(x.split(': ')[1]), reverse=True)      #sorting the list in descending order
    with open('leaderboard.txt', 'w') as file:     #opening the leaderboard file in write mode
        file.writelines(data[:10])      #writing the first 10 lines of the list to the file (top 10 scores)

#function to display the leaderboard at the end of the game
def leaderboard_display():
    leaders = []    #creating an empty list
    with open('leaderboard.txt', 'r') as file:    #opening the leaderboard file in read mode
        leaders = file.readlines()      #reading the lines of the file
    y=125       #setting the initial y coordinate
    for i, j in enumerate(leaders[:10], start=1):       #looping through the first 10 lines of the file
        label2 = Label(canvas2, width=15, text=f"{i}. {j}", font=('Helvetica', 16), bg='#04BFCD')       #creating the label
        canvas2.create_window(730, y, anchor=E, window=label2)
        y+=55       #incrementing the y coordinate

#creating the bosskey
def bosskey(event=None):
    global pause, bosscanvas, bg, background_image, canvas      #declaring global variables
    pause = True        #setting pause to true
    bosscanvas = Canvas(canvas, width=1280, height=720, background="#FFFFFF")      #creating the bosskey canvas
    canvas.create_window(640, 360, anchor=CENTER, window=bosscanvas)
    bg = PhotoImage(file="bg.gif")      #adding the background image
    background_image = bosscanvas.create_image(640, 360, anchor=CENTER, image=bg)       
    bosscanvas.tkraise(bosscanvas._name)      #raising the bosskey canvas
    screen.unbind("<space>")        #unbinding the space key
    screen.unbind("<Return>")       #unbinding the enter key
    screen.bind("<Escape>", back)       #binding the escape key to the back function
    screen.unbind("<c>")        #unbinding the cheat keys
    screen.unbind('<KeyPress-Left>')        
    screen.unbind('<KeyPress-Right>')
    screen.unbind('<KeyRelease-Left>')
    screen.unbind('<KeyRelease-Right>')
screen.bind("<Return>", bosskey)        #binding the enter key to the bosskey function

#returning to the game
def back(event=None):
    global pause, bosscanvas       #declaring global variables
    if pause:       #checking if game is paused
        pause = False       #setting pause to false
        bosscanvas.destroy()       #destroying the bosskey canvas
        obstacle_motion()       #calling the obstacle motion function
        screen.bind("<space>", paused)      #binding the space key to the pause function
    screen.unbind("<Escape>")       #unbinding the escape key
    screen.bind("<Return>", bosskey)        #binding the enter key to the bosskey function
    screen.bind("<c>", cheatcode)       #binding the cheat keys
    screen.bind('<KeyPress-Left>', check_ultracheat)        
    screen.bind('<KeyPress-Right>', check_ultracheat)
    screen.bind('<KeyRelease-Left>', key_release)
    screen.bind('<KeyRelease-Right>', key_release)
screen.bind("<Escape>", back)       #binding the escape key to the back function

#running the mainloop
screen.mainloop()