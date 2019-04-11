# !/usr/bin/python3
from tkinter import filedialog
from tkinter import *
from PIL import ImageGrab
import shutil
from Lexer import Lexer
import ast
import os
from colour import Color
from CreateMelody import createMelody
from PlayMelody import playMelody
import time
from subprocess import call
import sys

sys.path.append('../BitTune Lang')
import BitTuneDrawingLanguage

# Canvas dimension
canvas_width = 800
canvas_height = 320

# Color coordinates
red_x1 = 15
red_x2 = 40
red_y1 = 106
red_y2 = 131

orange_x1 = 55
orange_x2 = 80
orange_y1 = 106
orange_y2 = 131

yellow_x1 = 95
yellow_x2 = 120
yellow_y1 = 106
yellow_y2 = 131

green_x1 = 135
green_x2 = 160
green_y1 = 106
green_y2 = 131

blue_x1 = 175
blue_x2 = 200
blue_y1 = 106
blue_y2 = 131

indigo_x1 = 215
indigo_x2 = 240
indigo_y1 = 106
indigo_y2 = 131

violet_x1 = 255
violet_x2 = 280
violet_y1 = 106
violet_y2 = 131

# Brush Size coordinates
thin_x1 = 30
thin_x2 = 65
thin_y1 = 226
thin_y2 = 230

medium_x1 = 130
medium_x2 = 165
medium_y1 = 223
medium_y2 = 233

thick_x1 = 230
thick_x2 = 265
thick_y1 = 218
thick_y2 = 238

counter = 0

coordinates = []
color = "red"
size = 5

def paint(event):

   x1, y1 = (event.x - size), (event.y - size)
   x2, y2 = (event.x + size), (event.y + size)
   c.create_oval(x1, y1, x2, y2, fill = color, outline="")
  
   coordinates.append([x1, x2, y1, y2, color])
   
def changeTool (event):
   global color, size

   if ((event.x > red_x1) & (event.x < red_x2) & (event.y > red_y1) & (event.y < red_y2)):
      color = "red"
   elif ((event.x > orange_x1) & (event.x < orange_x2) & (event.y > orange_y1) & (event.y < orange_y2)):
      color = "orange"   
   elif ((event.x > yellow_x1) & (event.x < yellow_x2) & (event.y > yellow_y1) & (event.y < yellow_y2)):
   	  color = "yellow"
   elif ((event.x > green_x1) & (event.x < green_x2) & (event.y > green_y1) & (event.y < green_y2)):
      color = "green"
   elif ((event.x > blue_x1) & (event.x < blue_x2) & (event.y > blue_y1) & (event.y < blue_y2)):
      color = "blue"
   elif ((event.x > indigo_x1) & (event.x < indigo_x2) & (event.y > indigo_y1) & (event.y < indigo_y2)):
   	   color = "indigo"
   elif ((event.x > violet_x1) & (event.x < violet_x2) & (event.y > violet_y1) & (event.y < violet_y2)):
   	   color = "violet"
   elif ((event.x > thin_x1) & (event.x < thin_x2) & (event.y > thin_y1 - 15) & (event.y < thin_y2 + 15)):
   	   size = 2
   elif ((event.x > medium_x1) & (event.x < medium_x2) & (event.y > medium_y1 - 10) & (event.y < medium_y2 + 10)):
   	   size = 5
   elif ((event.x > thick_x1) & (event.x < thick_x2) & (event.y > thick_y1 - 5) & (event.y < thick_y2 + 5)):
   	   size = 10

   t.coords(current_option, 133, 40 - size, 168, 41 + size)
   t.itemconfig(current_option , fill = color, outline = color)

def playOutput():
   global coordinates
   
   lex = Lexer(coordinates)
   song = lex.compose_song()
   
   tempDir = ".bt_temp"

   # Delete the old one if it exists
   if os.path.exists(tempDir):
      shutil.rmtree(tempDir)
   # Create temporary directory to store intermediate files
   os.makedirs(tempDir)
   
   
   tempSongPath = tempDir + "/lastPlayedSong.wav"
   if os.path.exists(tempSongPath):
      shutil.rmtree(tempSongPath)

   createMelody(song, tempSongPath)
   call(['python','PlayMelody.py',tempSongPath])
   
   
 
def drawOutput():
   
   notes = notes_text.get("1.0", "end-1c")

   tempDir = ".bt_temp"

   # Create the directory only if it does not exist
   try:
      os.makedirs(tempDir)
   except FileExistsError:
      pass

   tempNotesFile = tempDir + "/currentNotes.btu"
   tempNewBTI = tempDir + "/generatedNotes.bti"

   with open(tempNotesFile, 'w') as f:
      f.write(str(notes))

   BitTuneDrawingLanguage.generateBitTuneImageFromFile(tempNotesFile,tempNewBTI)
   clearCanvas()

   loadFromFile(tempNewBTI)
   os.remove(tempNewBTI)
   os.remove(tempNotesFile)

def exitProgram(): 
   canvas.destroy()
   tool.destroy()
   text_editor.destroy()
   sys.exit()

def popUpMessage(message):
    pop_up = Tk()
    pop_up.wm_title("File Error")
    label = Label( pop_up, text = message, font = "Times 12")
    label.pack( side="top", fill="x", pady=20 )
    button = Button(pop_up, text="Okay", command = pop_up.destroy, font = "Times 12 bold", bg = "red", fg="white",  borderwidth=6,)
    button.pack()
    pop_up.mainloop()

def loadFromFile(loadFromPath=""):

   if (loadFromPath == ""):
      load_interface = Tk()
      load_interface.filename = filedialog.askopenfilename( initialdir = os.getcwd() ,title = "Select file",filetypes = (("Bit Tune Image File","*.bti"),("All Files","*.*")))
      load_interface.destroy()

      
      with open (load_interface.filename, 'r') as f:
         new_coordinates = ast.literal_eval(f.read())

   else:
      with open (loadFromPath, 'r') as f:
         new_coordinates = ast.literal_eval(f.read())

         #print("NEW COORDINATES")
         #print(new_coordinates)

   validate = True 
   global coordinates

   error_position = 0
   for i in range (len(new_coordinates)):
       
   	   try:
   	      int (new_coordinates[i][0])
   	      int (new_coordinates[i][1])
   	      int (new_coordinates[i][2])
   	      int (new_coordinates[i][3])
   	      Color (new_coordinates[i][4])

   	   except ValueError: 
   	      validate = False 
   	      error_position = i
   	      break 
   
   # Draw the notes
   if (validate):
       clearCanvas()
       for i in range (len(new_coordinates)):

           c.create_oval(new_coordinates[i][0] , new_coordinates[i][2], new_coordinates[i][1], 
                          new_coordinates[i][3], fill = new_coordinates[i][4], outline="")

           coordinates.append([new_coordinates[i][0], new_coordinates[i][1], new_coordinates[i][2],
       	                         new_coordinates[i][3], new_coordinates[i][4]])
   else :
   	   popUpMessage ("Column " + str(i) + " expected to have format [x1, y1, x2, y1, color] but got " + str(new_coordinates[error_position]))

def saveToFile():
   save_interface = Tk()
   save_interface.filename = filedialog.asksaveasfilename(initialdir = os.getcwd(), defaultextension=".bti", title = "Select file",filetypes = (("Bit Tune Image File","*.bti"),("All Files","*.*")))
   save_interface.destroy()	

   with open (save_interface.filename,'w') as f:
      f.write(str(coordinates))

   ImageGrab.grab((0,0,canvas_width + 15,canvas_height + 60)).save(os.path.splitext( save_interface.filename )[0] + '.jpg')

def drawMusicLines():
   global c
   c.create_line(0 , 3, 800, 3, width=2)
   c.create_line(0 , 79, 800, 79, width=2)
   c.create_line(0 , 159, 800, 159, width=2)
   c.create_line(0 , 239, 800, 239, width=2)
   c.create_line(0 , 319, 800, 319, width=2)

   c.create_line(799 , 0, 799, 320, width=6)
   c.create_line(790 , 0, 790, 320, width=2)

   c.create_line(3, 0, 3, 320, width=2)

def clearCanvas():
   global c, coordinates
   c.delete("all")
   #notes_text.delete("1.0", END)
   drawMusicLines()
   coordinates.clear()


# Canvas
canvas = Tk()
canvas.title("BitTune")
canvas.geometry("+0+0")
canvas.iconbitmap('../Assets/BitTune.ico')
canvas.protocol("WM_DELETE_WINDOW", exitProgram)
canvas.resizable(False, False)
c = Canvas(canvas, width=canvas_width, height=canvas_height, bg="white")
c.pack(expand = YES, fill = BOTH)
c.bind("<B1-Motion>", paint)
c.bind("<Button-1>", paint)

instructions = Label(canvas, text="Press the mouse to draw", font="Times 12")
instructions.pack(side = BOTTOM)

start = Label(canvas, text="← START", font="Times 12")
start.place(x=0, y=323)

start = Label(canvas, text="END →", font="Times 12")
start.place(x=745, y=323)

drawMusicLines()

# Tool
tool = Tk()
tool.title("Tool Bar")
tool.geometry("+805+0")
tool.iconbitmap('../Assets/BitTune.ico')
tool.protocol("WM_DELETE_WINDOW", exitProgram)
tool.resizable(False, False)
t = Canvas(tool, width=290, height=canvas_height + 180, bg="white")

# Current 
current_color = Label(tool, text="Current", font="Times 12 bold", bg="white")
current_color.place(x=120, y=2)
current_option = t.create_rectangle(133, 40 - size, 168, 41 + size, outline = color, width = 2, fill = color)

# Select Color
select_color = Label(tool, text="Select Color", font="Times 12 bold", bg="white")
select_color.place(x=110, y=80)

#Red
t.create_rectangle(red_x1, red_y1, red_x2, red_y2, outline="black", width=2, fill="red")

# Orange
t.create_rectangle(orange_x1, orange_y1, orange_x2, orange_y2, outline="black", width=2, fill="orange")

# Yellow
t.create_rectangle(yellow_x1, yellow_y1, yellow_x2, yellow_y2, outline="black", width=2, fill="yellow")

# Green
t.create_rectangle(green_x1, green_y1, green_x2, green_y2, outline="black", width=2, fill="green")

# Blue
t.create_rectangle(blue_x1, blue_y1, blue_x2, blue_y2, outline="black", width=2, fill="blue")

# Indigo
t.create_rectangle(indigo_x1, indigo_y1, indigo_x2, indigo_y2, outline="black", width=2, fill="indigo")

# Violet
t.create_rectangle(violet_x1, violet_y1, violet_x2, violet_y2, outline="black", width=2, fill="violet")

# Select Brush Size
select_color = Label(tool, text = "Select Brush Size", font="Times 12 bold", bg="white")
select_color.place( x=90, y=190)

# Thin
t.create_rectangle(thin_x1, thin_y1, thin_x2, thin_y2, outline="black", width=2, fill="black")

# Medium
t.create_rectangle(medium_x1, medium_y1, medium_x2 , medium_y2, outline="black", width=2, fill="black")

# Thick
t.create_rectangle(thick_x1, thick_y1, thick_x2, thick_y2, outline="black", width=2, fill="black")

# Size Names
note_names = Label(tool, text = "Thin                Medium              Thick", font="Times 12", bg="white")
note_names.place( x=30, y=240)

t.pack()

t.bind("<Button-1>", changeTool)

# Save Button
save = Button(tool, text="Save", font="Times 12 bold",bg ="Blue", fg ="white", borderwidth=4, command = saveToFile)
save.place( x=15, y=300 )

# Play Button
play = Button(tool, text="Play", font="Times 12 bold",bg ="Green", fg ="white", borderwidth=4, command = playOutput)
play.place(x=125, y=300 )

# Load Button
load = Button(tool, text="Load", font="Times 12 bold",bg ="Violet", fg ="white", borderwidth=4, command = loadFromFile)
load.place(x=225, y=300 )

# Draw Button
draw = Button(tool, text="Draw", font="Times 12 bold", bg ="Orange", fg ="white", borderwidth=4, command = drawOutput)
draw.place(x=15, y=380 )

# Clear Button
clear = Button(tool, text="Clear", font="Times 12 bold",bg ="Red", fg ="white", borderwidth=4, command = clearCanvas)
clear.place(x=122, y=380 )

# Exit Button
exit = Button(tool, text="Exit", font="Times 12 bold", bg ="Black", fg ="white", borderwidth=4, command = exitProgram)
exit.place(x=230, y=380 )

# Note names
note_names = Label(tool, text = "A        B       C        D       E        F       G", font="Times 12", bg="white")
note_names.place(x=17, y=140)

# Text Editor
text_editor = Tk()
text_editor.title("BitTune Code Editor")
text_editor.geometry("+0+385")
text_editor.iconbitmap('../Assets/BitTune.ico')
text_editor.protocol("WM_DELETE_WINDOW", exitProgram)
text_editor.resizable(False, False)

te = Canvas(text_editor, width = canvas_width, height = 115, bg="white")
notes_text = Text(text_editor, height = 5, width = 100, font = "Times 14 bold", bg = "white", borderwidth = 2)
notes_text.place(x = 0, y = 0)
te.pack()

mainloop()
