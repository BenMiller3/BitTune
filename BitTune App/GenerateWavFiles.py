from ast import literal_eval
import multiprocessing
import pysynth as ps
import sys

def createWav(songInfo):
    """ Create a .wav file given a song name, and it's corresponding notes """
    songName = songInfo[0]
    songNotes = songInfo[1]
    ps.make_wav(songNotes, fn = songName, silent = True)

def main():
    print("Number of cpu : ", multiprocessing.cpu_count())

if __name__ == '__main__':

    songInfo = sys.argv[1:]
    songNames = literal_eval(songInfo[0].split('@')[0])
    songNotes = literal_eval(songInfo[0].split('@')[1])

    songs = []
    for i in range(len(songNames)):
        songs.append([songNames[i], songNotes[i]])

    with multiprocessing.Pool() as pool:
        pool.map(createWav, songs)