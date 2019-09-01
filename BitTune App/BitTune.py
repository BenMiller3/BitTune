# !/usr/bin/python3
from tkinter import filedialog
from tkinter import *
import shutil
from Lexer import Lexer
import ast
import os
from colour import Color
from CreateMelody import createMelody
from PlayMelody import playMelody
from subprocess import call
import sys
import multiprocessing

sys.path.append('../BitTune Lang')
import BitTuneDrawingLanguage

APP_FONT = "Verdana"
 
# Canvas dimension
canvas_width = 800
canvas_height = 320

# colour coordinates
red_x1 = 15 ;red_x2 = 40;red_y1 = 106;red_y2 = 131
orange_x1 = 55;orange_x2 = 80;orange_y1 = 106;orange_y2 = 131
yellow_x1 = 95;yellow_x2 = 120;yellow_y1 = 106;yellow_y2 = 131
green_x1 = 135;green_x2 = 160;green_y1 = 106;green_y2 = 131
blue_x1 = 175;blue_x2 = 200;blue_y1 = 106;blue_y2 = 131
indigo_x1 = 215;indigo_x2 = 240;indigo_y1 = 106;indigo_y2 = 131
violet_x1 = 255;violet_x2 = 280;violet_y1 = 106;violet_y2 = 131

# Brush Size coordinates
thin_x1 = 30;thin_x2 = 65;thin_y1 = 226;thin_y2 = 230
medium_x1 = 130;medium_x2 = 165;medium_y1 = 223;medium_y2 = 233
thick_x1 = 230;thick_x2 = 265;thick_y1 = 218;thick_y2 = 238

# Initial values
counter = 0
coordinates = []
active_colour = "red"
active_note = 'A'
size = 5
lastPlayedCoordinates = []

def paint(event):
   """ This function takes a window event and paints the canvas at the x and y coordinate of the event """
   global coordinates, lastPlayedCoordinates

   x1, y1 = (event.x - size), (event.y - size)
   x2, y2 = (event.x + size), (event.y + size)
   c.create_oval(x1, y1, x2, y2, fill = active_colour, outline="")
  
   coordinates.append([x1, x2, y1, y2, active_colour])
   lastPlayedCoordinates = []
   
def changeTool(event):
   """ Change the users tool based on the event x and y coordinates. Changes to the tool over the mouse. """
   global active_colour, active_note, size

   if ((event.x > red_x1) & (event.x < red_x2) & (event.y > red_y1) & (event.y < red_y2)):
      active_colour = "red"
      active_note = 'A'
   elif ((event.x > orange_x1) & (event.x < orange_x2) & (event.y > orange_y1) & (event.y < orange_y2)):
      active_colour = "orange" 
      active_note = 'B'  
   elif ((event.x > yellow_x1) & (event.x < yellow_x2) & (event.y > yellow_y1) & (event.y < yellow_y2)):
      active_colour = "yellow"
      active_note = 'C'
   elif ((event.x > green_x1) & (event.x < green_x2) & (event.y > green_y1) & (event.y < green_y2)):
      active_colour = "green"
      active_note = 'D'
   elif ((event.x > blue_x1) & (event.x < blue_x2) & (event.y > blue_y1) & (event.y < blue_y2)):
      active_colour = "blue"
      active_note = 'E'
   elif ((event.x > indigo_x1) & (event.x < indigo_x2) & (event.y > indigo_y1) & (event.y < indigo_y2)):
      active_colour = "indigo"
      active_note = 'F'
   elif ((event.x > violet_x1) & (event.x < violet_x2) & (event.y > violet_y1) & (event.y < violet_y2)):
      active_colour = "violet"
      active_note = 'G'
   elif ((event.x > thin_x1) & (event.x < thin_x2) & (event.y > thin_y1 - 15) & (event.y < thin_y2 + 15)):
      size = 2
   elif ((event.x > medium_x1) & (event.x < medium_x2) & (event.y > medium_y1 - 10) & (event.y < medium_y2 + 10)):
      size = 5
   elif ((event.x > thick_x1) & (event.x < thick_x2) & (event.y > thick_y1 - 5) & (event.y < thick_y2 + 5)):
      size = 10

   t.coords(current_option, 133, 40 - size, 168, 41 + size)
   t.itemconfig(current_option , fill = active_colour, outline = active_colour)
   current_note.config(text=active_note)

def playOutput():
   """ 
   This function first transposes the coordinates on the canvas into notes via. the lexer (Lexer.py)
   It then converts these notes into a tuple that is readable by pysynth via. the CreateMelody.py function createMelody
   This function also builds the .wav file from the pysynth output.
   Lastly, using PlayMelody.py in a subprocess it will play the wav file in the users audio speakers. 
   """
   global coordinates, lastPlayedCoordinates

   tempDir = ".bt_temp"
   tempSongPath = tempDir + "/lastPlayedSong.wav"

   if (coordinates == []):
      return

   # If there have been no changes to the canvas, don't recreate the .wav files
   if (coordinates == lastPlayedCoordinates):
      if os.path.isfile(tempSongPath):
         call(['python','PlayMelody.py',tempSongPath])
         return

   lex = Lexer(coordinates)
   song = lex.compose_song()
   
   # Don't create a sub directory and just make them hidden files, this way no permission error

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

   lastPlayedCoordinates = coordinates
   
def drawOutput():
   """ 
   Parses the text on the code editor into the BitTune language, then loads the
   parsed file onto the user's draw canvas.
   """
   global lastPlayedCoordinates
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
   lastPlayedCoordinates = []

def exitProgram():
   """ This function will destory all windows on exit and close the program """
   canvas.destroy()
   tool.destroy()
   code_editor.destroy()
   sys.exit()

def popUpMessage(message):
   """ Creates a pop up window if there are any issues in loading the user file """
   pop_up = Tk()
   pop_up.wm_title("File Error")
   label = Label( pop_up, text = message, font = APP_FONT + " 12")
   label.pack( side="top", fill="x", pady=20 )
   button = Button(pop_up, text="Okay", command = pop_up.destroy, font = APP_FONT + " 12 bold", bg = "red", fg="white",  borderwidth=6,)
   button.pack()
   pop_up.mainloop()

def loadCodeFromFile():
   """ Load bittune language files from folders. Start in the templates folder to easily load the template songs """
   global notes_text

   notes_text.delete("1.0", END)
   load_interface = Tk()
   load_interface.filename = filedialog.askopenfilename( initialdir = ("../Templates") ,title = "Select file",filetypes = (("Bit Tune File","*.btu"),("All Files","*.*")))
   load_interface.destroy()

   with open (load_interface.filename, 'r') as f:
      code = f.read()
   notes_text.insert(END, str(code))

def loadFromFile(loadFromPath=""):
   """ 
   Load a BitTune image file (coordinates) onto the canvas
   loadFromPath: Can be a defined file path, otherwise the file will be loaded from the file dialog (user prompt)
   """
   global coordinates

   if (loadFromPath == ""):
      load_interface = Tk()
      load_interface.filename = filedialog.askopenfilename( initialdir = os.getcwd() ,title = "Select file",filetypes = (("Bit Tune Image File","*.bti"),("All Files","*.*")))
      load_interface.destroy()

      
      with open (load_interface.filename, 'r') as f:
         new_coordinates = ast.literal_eval(f.read())

   else:
      with open (loadFromPath, 'r') as f:
         new_coordinates = ast.literal_eval(f.read())

   validate = True 

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
   	   popUpMessage("Column " + str(i) + " expected to have format [x1, y1, x2, y1, colour] but got " + str(new_coordinates[error_position]))

   coordinates = new_coordinates

def saveCodeToFile():
   """ 
   Save the current contents of the code editor to a file of the users choosing 
   BTU (BitTune) files saved using this format will be able to be loaded by the user using the load code function.
   """
   save_interface = Tk()
   save_interface.filename = filedialog.asksaveasfilename(initialdir = os.getcwd(), defaultextension=".btu", title = "Save as",filetypes = (("Bit Tune Image File","*.btu"),("All Files","*.*")))
   save_interface.destroy()	

   btuCode = notes_text.get( "1.0", "end-1c" )

   with open (save_interface.filename,'w') as f:
      f.write(str(btuCode))
   
   

def saveToFile():
   """ 
   Save the current coordinate structure to a file of the users choosing 
   BTI (BitTune Image) files saved using this format will be able to be loaded by the user using the load function.
   """
   save_interface = Tk()
   save_interface.filename = filedialog.asksaveasfilename(initialdir = os.getcwd(), defaultextension=".bti", title = "Save as",filetypes = (("Bit Tune Image File","*.bti"),("All Files","*.*")))
   save_interface.destroy()	

   with open (save_interface.filename,'w') as f:
      f.write(str(coordinates))

def drawMusicLines():
   """ When redrawing the canvas, this function is used to draw the horizontal lines on the canvas """
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
   """ Clears the canvas of the current image """
   global c, coordinates
   c.delete("all")
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

instructions = Label(canvas, text="Press the mouse to draw", font=APP_FONT + " 12")
instructions.pack(side = BOTTOM)

start = Label(canvas, text = "← START", font = APP_FONT + " 12")
start.place(x=0, y=323)

start = Label(canvas, text = "END →", font = APP_FONT + " 12")
start.place(x=745, y=323)

drawMusicLines()

# Code Editor
code_editor = Tk()
code_editor.title("BitTune Code Editor")
code_editor.geometry("+0+380")
code_editor.iconbitmap('../Assets/BitTune.ico')
code_editor.protocol("WM_DELETE_WINDOW", exitProgram)
code_editor.resizable(False, False)

te = Canvas(code_editor, width = canvas_width, height = 140, bg="white")
notes_text = Text(code_editor, height = 25, width = 100, font = "Courier 14", bg = "white", borderwidth = 2)
notes_text.place(x = 0, y = 0)
te.pack()

# Tool
tool = Tk()
tool.title("BitTune Tool Bar")
tool.geometry("+805+0")
tool.iconbitmap('../Assets/BitTune.ico')
tool.protocol("WM_DELETE_WINDOW", exitProgram)
tool.resizable(False, False)
t = Canvas(tool, width=290, height=canvas_height + 200, bg="white")
t.create_line(0 , 380, 800, 380, width=2)

# Current 
current_colour = Label(tool, text="Current", font=APP_FONT + " 12 bold", bg="white")
current_colour.place(x=110, y=2)
current_option = t.create_rectangle(133, 40 - size, 168, 41 + size, outline = active_colour, width = 2, fill = active_colour)

current_note = Label(tool, text=active_note, font=APP_FONT + " 12 bold", bg="white")
current_note.place(x=115, y=29)

# Select Colour
select_colour = Label(tool, text="Select Colour", font=APP_FONT + " 12 bold", bg="white")
select_colour.place(x=110, y=80)

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
select_colour = Label(tool, text = "Select Brush Size", font=APP_FONT + " 12 bold", bg="white")
select_colour.place( x=90, y=190)

# Thin
t.create_rectangle(thin_x1, thin_y1, thin_x2, thin_y2, outline="black", width=2, fill="black")

# Medium
t.create_rectangle(medium_x1, medium_y1, medium_x2 , medium_y2, outline="black", width=2, fill="black")

# Thick
t.create_rectangle(thick_x1, thick_y1, thick_x2, thick_y2, outline="black", width=2, fill="black")

# Size Names
note_names = Label(tool, text = "Thin         Medium        Thick", font = APP_FONT + " 12", bg = "white")
note_names.place( x=25, y=240)

t.pack()

t.bind("<Button-1>", changeTool)

# Save Button
save = Button(tool, text="Save Image", font=APP_FONT + " 10 bold", bg = "#696969", fg = "white", borderwidth=2, command = saveToFile)
save.place(x=155, y=300)

# Play Button
play = Button(tool, text="Play", font=APP_FONT + " 12 bold", bg = "Green", fg ="white", borderwidth=2, command = playOutput)
play.place(x=40, y=300)

# Load Button
load = Button(tool, text="Load Image", font=APP_FONT + " 10 bold", bg = "#696969", fg ="white", borderwidth=2, command = loadFromFile)
load.place(x=155, y=340)

# Clear Button
clear = Button(tool, text="Clear Canvas", font=APP_FONT + " 10 bold", bg = "#696969", fg ="white", borderwidth=2, command = clearCanvas)
clear.place(x=15, y=340)

# Compiler Button
draw = Button(tool, text="Compile Code to Canvas", font=APP_FONT + " 10 bold", bg ="blue", fg ="white", borderwidth=4, command = drawOutput)
draw.place(x=15, y=400)

# Load Code Button
load_code = Button(tool, text="Load Code to Editor", font=APP_FONT + " 10 bold", bg ="#696969", fg ="white", borderwidth=4, command = loadCodeFromFile)
load_code.place(x=15, y=440)

# Save Code Button
load_code = Button(tool, text="Save Code in Editor", font=APP_FONT + " 10 bold", bg ="#696969", fg ="white", borderwidth=4, command = saveCodeToFile)
load_code.place(x=15, y=480)

# Exit Button
exit = Button(tool, text="Exit", font=APP_FONT + " 10 bold", bg ="Black", fg ="white", borderwidth=2, command = exitProgram)
exit.place(x=240, y=490)

# Note names
note_names = Label(tool, text = "A     B     C     D     E     F     G", font=APP_FONT + " 12", bg="white")
note_names.place(x=17, y=140)

mainloop()