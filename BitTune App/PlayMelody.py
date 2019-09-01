import sys
from playsound import playsound

def playMelody(fileName):
    playsound(fileName)

def main():
    #print("\t=== Running Tests ===\n")
    if (len(sys.argv) == 1):
        songFile = 'test.wav'
    else:
        songFile = str(sys.argv[1])

    playMelody(songFile)

if __name__ == '__main__': main()