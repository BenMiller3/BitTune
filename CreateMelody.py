# Pysynth download and more information can be found at: https://mdoege.github.io/PySynth/
import pysynth as ps
import ast
import wave
import sys
import os
from PlayMelody import playMelody

def loadSong(fileName):
    with open (fileName, 'r') as f:
        testSong = ast.literal_eval(f.read())

    return testSong

def remove_dup(list):
    newList = []
    for note in list:
        if (note == 'R') or (note not in newList):
            newList.append(note)

    return newList

def createMelody(song, outputSongFileName, timing=4):

    wavInput = (())
    #waveList1 = (())
    #waveList2 = (())
    #waveList3 = (())
    #waveList4 = (())

    while song[0] == ['R','R','R','R']:
        song.remove(song[0])
    while song[-1] == ['R','R','R','R']:
        song.remove(song[-1])


    for notesList in song:

        remove_dup(notesList)
        # Affects the pitch of the note
        notesNum = 4
        # since A and B come before C on the scale of pysynth, they need to be one pitch lower to fit in
        if (notesList[0].upper() == 'A' or notesList[0] == 'B'):
            notesNum = 3
        elif (notesList[0].upper() == 'R'):
            notesNum = ''
        wavInput = ((notesList[0].lower() + str(notesNum), timing),) + wavInput
        #waveList1 = ((notesList[0].lower(), timing),) + waveList1
        #waveList2 = ((notesList[1].lower(), timing),) + waveList2
        #waveList3 = ((notesList[2].lower(), timing),) + waveList3
        #waveList4 = ((notesList[3].lower(), timing),) + waveList4


    wavInput = wavInput[::-1]

    ps.make_wav(wavInput, fn = outputSongFileName)
    #ps.make_wav(waveList1, fn = ".bt_temp/waveList1.wav")
    #ps.make_wav(waveList2, fn = ".bt_temp/waveList2.wav")
    #ps.make_wav(waveList3, fn = ".bt_temp/waveList3.wav")
    #ps.make_wav(waveList4, fn = ".bt_temp/waveList4.wav")

    '''
    # merge wave files
    inputFiles = [".bt_temp/waveList1.wav", ".bt_temp/waveList2.wav", ".bt_temp/waveList3.wav", ".bt_temp/waveList4.wav"]
    
    outfile = outputSongFileName

    data = []
    for inputFile in inputFiles:
        w = wave.open(inputFile, 'rb')
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()

    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.writeframes(data[2][1])
    output.writeframes(data[3][1])
    output.close()
    '''


def main():
    #print("\t=== Running Tests ===\n")

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
