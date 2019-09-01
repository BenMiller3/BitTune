# Pysynth download and more information can be found at: https://mdoege.github.io/PySynth/
import pysynth as ps
import ast
import wave
import sys
import os
from PlayMelody import playMelody
from subprocess import call
from pydub import AudioSegment

def loadSong(fileName):
    """
    Loads a song from a file as input.

    fileName: Name of the file to be read from
    """
    with open (fileName, 'r') as f:
        testSong = ast.literal_eval(f.read())

    return testSong

def isAllRests(notes):
    """ Check if a given list of notes has only rests within it """
    for note in notes:
        if note[0] != 'r':
            return False
    return True

def remove_dup(noteList):
    """ 
    This function removes duplicate notes from a note line, so that the same note is
    not played twice on the same bar, in order to allow the other notes to be played.

    noteList: A list of length 4 containing valid note sequences 
    """
    newList = []
    for note in noteList:
        if (note == 'R') or (note not in newList):
            newList.append(note)
        else:
            newList.append('R')

    return newList

def createMelody(song, outputSongFileName, timing=4):
    """ 
    Given the valid song format, this function will create a wav file using pysynth
    that is representative of those notes.

    song: Nested list of notes and rests (length 40x4)
    outputSongFileName: The desired output wav file name
    timing: the bpm timing that will be used. Currently applied to all notes.
    """
    wavInput = (())
    wavInput1 = (())
    wavInput2 = (())
    wavInput3 = (())

    # Remove the beginning and end portions of the canvas that are blank
    while song[0] == ['R','R','R','R']:
        del song[0]
    while song[-1] == ['R','R','R','R']:
        del song[-1]

    for notesList in song:

        remove_dup(notesList)

        notesNum = []
        for i in range(len(notesList)):
            if (notesList[i].upper() == 'R'):
                notesNum.append('')
            elif (notesList[i].upper() == 'A' or notesList[i].upper() == 'B'):
                notesNum.append('3')
            else:
                notesNum.append('4')

        wavInput = ((notesList[0].lower() + str(notesNum[0]), timing),) + wavInput
        wavInput1 = ((notesList[1].lower() + str(notesNum[1]), timing),) + wavInput1
        wavInput2 = ((notesList[2].lower() + str(notesNum[2]), timing),) + wavInput2
        wavInput3 = ((notesList[3].lower() + str(notesNum[3]), timing),) + wavInput3


    wavInput = wavInput[::-1]
    wavInput1 = wavInput1[::-1]
    wavInput2 = wavInput2[::-1]
    wavInput3 = wavInput3[::-1]

    wavNames = [".wav1.wav",".wav2.wav",".wav3.wav",".wav4.wav"]
    wavInputs = [wavInput,wavInput1,wavInput2,wavInput3]

    validWavInputs = []

    for i in range(len(wavInputs)):
        if isAllRests(wavInputs[i]) == False:
            validWavInputs.append(wavInputs[i])

    validWavNames = wavNames[:len(validWavInputs)]

    call(['python','GenerateWavFiles.py',str(validWavNames) + "@" + str(validWavInputs)])

    sounds = []
    for i in range(len(validWavNames)):
        sounds.append(AudioSegment.from_wav(validWavNames[i]))

    combined = sounds[0]
    for i in range(1, len(sounds)):
        combined = combined.overlay(sounds[i])

    combined.export(outputSongFileName, format='wav')

def main():
    """ The main function is used to test the different parts of CreateMelody """
    if (len(sys.argv) == 1):
        song = (
        ('c', 4), ('c*', 4), ('eb', 4),
        ('g#', 4),  ('g*', 2), ('g5', 4),
        ('g5*', 4), ('r', 4), ('e5', 16),
        ('f5', 16),  ('e5', 16),  ('d5', 16),
        ('e5*', 4)
        )
        song = (
            ('a3',4), ('b3',4),('c4',4),('d4',4)
        )
        outputSongFile = "testSong.wav"
        timing = 4

        createMelody(song, outputSongFile, timing)
        playMelody(outputSongFile)

    else:
        song = str(sys.argv[1])
        outputSongFile = str(sys.argv[2])
        createMelody(song, outputSongFile, timing)



if __name__ == '__main__': main()
