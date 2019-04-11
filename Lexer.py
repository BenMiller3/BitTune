import ast

class Lexer:

    coordinates = []
    song = [['R']]
    midpoints = []

    horizontalBars = 4
    verticalBars = 40

    canvasHeight = 320
    canvasWidth = 800

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.coordinates = self.remove_duplicates()

        self.midpoints = self.get_midpoints()
        self.colour_midpoints()

        self.song = [['R']*self.horizontalBars for n in range(self.verticalBars)]

    def show_coordinates(self):
        print(self.coordinates)

    def get_coordinates(self):
        return self.coordinates

    def get_midpoints(self):
        midpoints = []

        for coordinate in self.coordinates:
            midPointX = (int(coordinate[0]) + int(coordinate[1]))/2
            midPointY = (int(coordinate[2]) + int(coordinate[3]))/2
            midpoints.append([midPointX, midPointY, coordinate[-1]])

        return midpoints

    def remove_duplicates(self):
        uniqueNotes = []

        for coordinate in self.coordinates:
            if coordinate not in uniqueNotes:
                uniqueNotes.append(coordinate)
        return uniqueNotes

    def colour_midpoints(self):

        for i in range(len(self.midpoints)):
            midpointColour = self.midpoints[i][-1]
            note = self.colour_to_note(midpointColour)

            self.midpoints[i][-1] = note

    def compose_song(self):

        xDivisor = self.canvasWidth / self.verticalBars
        yDivisor = self.canvasHeight / self.horizontalBars

        for note in self.midpoints:
            
            xValue = note[0]
            yValue = note[1]
            letter = note[2]

            if (xValue >= self.canvasWidth):
                xValue -= 1
            if (yValue >= self.canvasHeight):
                yValue -= 1
            

            noteX = int(xValue // xDivisor)
            noteY = int(yValue // yDivisor)         
            
            try:
                self.song[noteX][noteY] = letter
            except IndexError:
                pass
                # Ignoring colours that have a midpoint on the bounds

        return self.song

    def colour_to_note(self, colour):
        if (colour == 'red'):
            return 'A'
        elif(colour == 'orange'):
            return 'B'
        elif(colour == 'yellow'):
            return 'C'
        elif(colour == 'green'):
            return 'D'
        elif(colour == 'blue'):
            return 'E'
        elif(colour == 'indigo'):
            return 'F'
        elif(colour == 'violet'):
            return 'G'
        else:
            return 'R' # R represents a rest, if colour is unknown, play nothing.

    def write_song_to_file(self, fileName):
        with open (fileName, 'w') as f:
            f.write(str(self.song))

def main():
    print("\t=== Running Tests ===\n")

    testCoordinates = []

    try:
        with open ("testCoordinates.txt", 'r') as f:
            testCoordinates = ast.literal_eval(f.read())

    except FileNotFoundError:
        testCoordinates = [[382, 392, 142, 152, 'red'], [383, 393, 142, 152, 'red'], [384, 394, 142, 152, 'red'], [385, 395, 142, 152, 'red'], [387, 397, 142, 152, 'red'], 
        [386, 396, 142, 152, 'red'], [393, 403, 131, 141, 'blue'], [392, 402, 131, 141, 'blue'], [392, 402, 133, 143, 'blue'], [391, 401, 134, 144, 'blue'], 
        [391, 401, 135, 145, 'blue'], [391, 401, 136, 146, 'blue'], [391, 401, 137, 147, 'blue'], [390, 400, 137, 147, 'blue'], [390, 400, 138, 148, 'blue'], 
        [390, 400, 139, 149, 'blue'], [390, 400, 140, 150, 'blue'], [390, 400, 141, 151, 'blue'], [389, 399, 142, 152, 'blue'], [389, 399, 141, 151, 'blue'], 
        [400, 410, 152, 162, 'yellow'], [399, 409, 152, 162, 'yellow'], [398, 408, 152, 162, 'yellow'], [397, 407, 153, 163, 'yellow'], [395, 405, 153, 163, 'yellow'], 
        [394, 404, 153, 163, 'yellow'], [393, 403, 153, 163, 'yellow'], [392, 402, 153, 163, 'yellow'], [390, 400, 154, 164, 'yellow'], [389, 399, 154, 164, 'yellow'], 
        [387, 397, 153, 163, 'yellow'], [386, 396, 153, 163, 'yellow'], [381, 391, 151, 161, 'yellow'], [378, 388, 149, 159, 'yellow'], [377, 387, 149, 159, 'yellow'], 
        [375, 385, 148, 158, 'yellow'], [375, 385, 147, 157, 'yellow'], [374, 384, 147, 157, 'yellow'], [373, 383, 147, 157, 'yellow'], [373, 383, 146, 156, 'yellow'], 
        [373, 383, 145, 155, 'yellow'], [372, 382, 144, 154, 'yellow'], [372, 382, 142, 152, 'yellow'], [372, 382, 141, 151, 'yellow'], [370, 380, 139, 149, 'yellow'], 
        [370, 380, 138, 148, 'yellow'], [370, 380, 135, 145, 'yellow'], [370, 380, 134, 144, 'yellow'], [370, 380, 132, 142, 'yellow'], [370, 380, 131, 141, 'yellow'], 
        [370, 380, 129, 139, 'yellow'], [370, 380, 128, 138, 'yellow'], [371, 381, 127, 137, 'yellow'], [371, 381, 126, 136, 'yellow'], [371, 381, 125, 135, 'yellow'], 
        [370, 380, 125, 135, 'yellow'], [383, 393, 153, 163, 'yellow'], [383, 393, 152, 162, 'yellow'], [384, 394, 146, 156, 'violet'], [378, 388, 144, 154, 'indigo'], 
        [577, 587, 151, 161, 'orange'], [578, 588, 150, 160, 'orange'], [26, 36, 299, 309, 'green']]
    
    

    lexer = Lexer(testCoordinates)
    
    song = lexer.compose_song()
    outputSongFile = "banana.txt"
    lexer.write_song_to_file(outputSongFile)
    print("Successfully wrote the song to the file {}".format(outputSongFile))

if __name__ == "__main__":
    main()