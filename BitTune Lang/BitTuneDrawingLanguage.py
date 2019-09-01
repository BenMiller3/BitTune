import sys
from antlr4 import *
from BitTuneGrammarLexer import BitTuneGrammarLexer
from BitTuneGrammarListener import BitTuneGrammarListener
from BitTuneGrammarParser import BitTuneGrammarParser

total_notes = []

note_coordinates = []
current_shape = "oval"

class BitTuneGrammarListener(BitTuneGrammarListener):

    
    def enterShapeSequence(self, ctx):
        """ 
        When a shape keyword is found, change the current shape to that keyword. 
        This allows for nested shaping, and the shape that is drawn is the one that 
        is assigned last (most inner shape).
        """
        global current_shape
        current_shape = ctx.getText().split('(')[0].lower()
    
    def exitShapeSequence(self, ctx):
        """
        When leaving a shape sequence, ensure that all the notes were drawn on the canvas
        """
        pass

    def enterNoteSequence(self, ctx):
        """ 
        When a note sequence is tokenized, this function grabs the text from the note sequence
        and adds it to the total_notes (all notes in the song)
        """
        global total_notes, current_shape

        note = ctx.getText()
        total_notes.append(note.upper() + "@" + current_shape) # don't append the escape character in the note

    def enterMultiNoteSequence(self, ctx):
        """
        When a multi note sequence is tokenized, this function will be called and it will
        add the appropriate multiple of notes to the global total_notes list
        """
        global total_notes

        note = ctx.getText()

        number = ""
        isNum = True
        
        if (note == ""):
            return

        i = 0
        while isNum: 
            if (note[i].isdigit()):
                number += note[i]
                i += 1
            else:
                isNum = False

        notes = note[len(number):]
        number = int(number)

        for i in range(number):
            total_notes.append(notes.upper() + "@" + current_shape)
        
    def exitProgram(self, ctx):
        """ Currently no action is needed when the program ends """
        pass

def outputSong(fileName):
    """
    This function simply writes the list of note coordinates to a file.
    This file can then be loaded into the BitTune application via. the load function in BitTune

    fileName: the name of the output file that the note coordinates will be written to.
    """
    global note_coordinates

    with open(fileName, 'w') as f:
        f.write(str(note_coordinates))

def generateImage():
    """
    When generating the BitTune Image (.bti) file, the canvas
    currently restricts us to 40 notes, and after reducing our input,
    we call convertNotes to Coordinates to get a valid .bti file. 
    """
    global total_notes, total_shapes
    total_notes = total_notes[0:40] # Can only take 40 notes

    convertNotesToCoordinates()

def convertNotesToCoordinates():
    """
    Given the total_notes (valid input notes) that were parsed by the parser,
    this function converts them into valid note coordinates which can then be
    loaded by the BitTune application.
    """
    global total_notes
    global note_coordinates

    for i in range(len(total_notes)):
        if (total_notes[i].upper() != 'R'):
            note_coordinates += (noteToCoordinate(total_notes[i], i))

def noteToColour(note):
    """
    Converts each note to it's corresponding valid BitTune note

    note: Input letter (A-G | R)
    returns: The string of the colour that represents note
    """
    NOTES = {'A':'red','B':'orange','C':'yellow',
    'D':'green','E':'blue','F':'indigo','G':'violet'
    }

    return NOTES[note]

def noteToCoordinate(note,index):
    """ 
    This function determines the shape of the coordinates by the current shape.
    note: the note to be drawn on the canvas 
    index: 
    """
    current_shape = note.split('@')[1]
    note = note.split('@')[0]
    coordinate = []

    if (current_shape == "oval"):
        xNum = (index + 1)*20

        x1 = xNum - 20
        x2 = xNum

        for i in range(len(note)):
            if (note[i].upper() != 'R'):
                coordinate.append([x1, x2, i*80, (i+1)*80, noteToColour(note[i])])

    elif (current_shape == "line"):
        xNum = (index + 1)*20

        x1 = xNum - 20
        x2 = xNum

        for i in range(len(note)):
            if (note[i].upper() != 'R'):
                coordinate.append([xNum - 10, xNum - 10, i*80, (i+1)*80, noteToColour(note[i])])
    
    elif (current_shape == "rect"):
        xNum = (index + 1)*20

        x1 = xNum - 20
        x2 = xNum

        for i in range(len(note)):
            for j in range(15):
                if (note[i].upper() != 'R'):
                    coordinate.append([xNum + (j - 20), xNum + (j - 20), i*80, (i+1)*80, noteToColour(note[i])])

    elif (current_shape == "dots"):
        xNum = (index + 1)*20

        x1 = xNum - 20
        x2 = xNum

        for i in range(len(note)):
            if (note[i].upper() != 'R'):
                coordinate.append([x1, x2, i*80, (i+1)*80 - 40, noteToColour(note[i])])
                coordinate.append([x1, x2, i*80 + 40, (i+1)*80, noteToColour(note[i])])


    return coordinate

def resetDefaults():
    """ 
    This function is used to restore global variables back to their default values
    so that there is no unexpected side effects of running langauge functions
    """
    global current_shape, note_coordinates, total_notes
    current_shape = "oval"
    note_coordinates = []
    total_notes = []

def generateBitTuneImageFromFile(langInput, outputFileName):
    """ 
    This is the main portion of the BitTune language, essentially what it does is it
    takes the input text, tokenizes it, lexes it, and parses it.
    The result will be a valid BitTune Image (.bit) file that can be loaded into the 
    BitTune application via. the load function.

    langInput: BitTune language text that is ready to be parsed
    outputFileName: The target output file where the parsed code will be written to. 
    """
    global note_coordinates
    global total_notes
    note_coordinates = []
    total_notes = []
    input_stream = FileStream(langInput)
    lexer = BitTuneGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BitTuneGrammarParser(stream)
    tree = parser.program()
    printer = BitTuneGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(printer,tree)

    generateImage()
    outputSong(outputFileName)
    resetDefaults()

def main():
    """ 
    This function will only be called when directly running this file
    As such, a testSong will be tested when this file is run.
    """
    inputFile = "testSong.btu"
    input_stream = FileStream(inputFile)
    lexer = BitTuneGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BitTuneGrammarParser(stream)
    tree = parser.program()
    printer = BitTuneGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(printer,tree)

    generateImage()

    fileName = "outputSong.bti" #.bti is a BitTune Image file
    outputSong(fileName)

if __name__ == '__main__': 
    main()
