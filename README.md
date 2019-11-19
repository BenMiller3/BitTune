# BitTune
![BitTuneLogo](https://raw.githubusercontent.com/BenMiller3/BitTune/master/Assets/BitTune_Logo.png)

BitTune is a Python application that transforms pictures into music.
It also is a language, that can transform musical notes written in the BitTune Langauge into BitTune Image files which can be loaded, saved, and played by the BitTune application.

## Quickstart
To download the requirements and run the application, simply execute the following command in the project's root folder:

`pip install -r requirements.txt && cd BitTune\ App && python BitTune.py`

For more details on building the app, refer to: [How to build](#how-to-build)
For more details on how to use the app, refer to: [How to use the application](#how-to-use-the-application)

## Motivation
We were inspired by the different ways an individual could create music, and the various interfaces or Digital Audio Workstations (DAWs) they used to do so. 
Our angle was to provide a fun and creative way to take what the user is imagining (artistically) and translate the corresponding pixels on screen into a melody.

## Features
### BitTune Drawing Application
* Multiple Brush Sizes
* Colours that represent notes
* Intuitive Interface
* Save and Load Features

<audio src="Assets/sample_song.wav" controls preload></audio>

### BitTune Language
* Intuitively transform notes into BitTune images
* Can repeat multiple notes with a number, e.g. 5ACE, plays the chord ACE for 5 beats
* Supports single line comments '//'
* Supports 4 different shapes (dots, rect, line, and oval)

## Language Components

BitTune has two different language components which make up the application:
1. A language to draw pictures
2. A language that translates notes into pictures

## Screenshots
![Screenshot_CustomDrawing](https://raw.githubusercontent.com/BenMiller3/BitTune/master/Assets/Screenshot_1.png)

![Screenshot_GeneratedPicture](https://raw.githubusercontent.com/BenMiller3/BitTune/master/Assets/ScreenShot_2.png)

## How to Build
In order to build BitTune, you will need to have installed Python 3.

To download the python libraries that are used in this project, simply run:

`python -m pip install -r requirements.txt`

Once the libraries have downloaded, to run the app simply run the BitTune.py file with python in the BitTune App folder:

`cd BitTune\ App`

`python BitTune.py`

## Application Components
1. The BitTune window ( blank canvas ) is where the you draw the pictures.
2. The Text Editor window is where the you write your melody.
3. The Tool window allows the you to change line color and thickness. The buttons are also located here.
   * The __Save Image__ button allows you to save the drawing on the canvas.
   * The __Play__ button will transform your drawing on the canvas into music.
   * The __Load Image__ button allows you to load a previously saved drawing.
   * The __Compile Code to Canvas__ button will transform the code in the text editor into a picture on the canvas.
   * The __Clear Canvas__ button will reset the canvas.
   * The __Load Code to Editor__ button will load a .btu file to the code editor. Default folder is templates, for easy access to demo songs.
   * The __Save Code in Editor__ button will save the current contents of the editor into a .btu file.
   * The __Exit__ button will close the application.

## How to Use the Application
The application provides you with two approaches to create music:

The first option is to draw a picture on the canvas using different colors and then transforming it into music by clicking on the Play button. If you like the sound of what you just heard, don't forget to hit the Save Image button.

The second option is to write your own melody using the text editor. The text editor supports notes __A to G__ and uses __R__ to indicate a rest ( no sound playing ). A number in front of the note represents the duration. For example, __2ABC 4R__ will play notes ABC at the same time for 2 beats and then rest for 4 beats. Once you are done writing, click on the Draw button to transform it into a picture on the canvas. Afterwards click on the Play button to transform the picture into music.
To further customize your code, you can get creative by wrapping notes with shape keyword and brackets to draw the corresponding notes on the canvas in that shape. For example: __rect(a b 2de)__ would draw the notes: a, b, de, de in the shape of a rectangle. The currently supported shapes are: {oval, line, dots, and rect}. Currently oval is the default shape if no shape is chosen, otherwise the shape that was last selected will be the default shape.

The application also contains several sample songs which are located in the Templates folder. You can load these songs into the BitTune text editor by clicking the __Load Code to Editor__ button, selecting the song, and then clicking the __Compile Code to Canvas__ button or load the image directly using the __Load Image__ button and selecting __TwinkleTwinkleLittleStar.bti__.

## Future Considerations
In the future, we are hoping to provide preset colour templates in order to assist the user in creating better sounding music. 

We would also like to extend the BitTune Language to be more complex, including loops, different octaves, sharps, flats and potentially other instruments and tempos as well. 

Adding more elements of production such as drum loops or advanced orchestration would bring BitTune to a more technical and customizable level similar to that of a Digital Audio Workstation for children.


## Authors
* Benjamin Miller
* Prakhar Jalan
* Tony Wang
