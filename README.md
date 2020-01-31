# Alien Invasion Game!

### Description:
Alien Invasion is a videogame for Windows based on the classic arcade *Space Invaders*. 
Save the Planet Earth as you fight against an endless fleet of aliens with an ever increasing dificulty! 
Enjoy the spacial adventure through colorful and animated graphics, 8-bit sound FX and the techno soundtrack of the game: "Trickshot" (by [PEX](https://soundcloud.com/user-853103120/trickshot)).


The app is developed on Python 3.7 using the modules Pygame and PyInstaller.

---
### Table of contents:
- [Installation](https://github.com/marioal9806/alien_invasion/new/master?readme=1#installation)
- [Usage](https://github.com/marioal9806/alien_invasion/new/master?readme=1#usage)
- [Development](https://github.com/marioal9806/alien_invasion/new/master?readme=1#development)
- [Credits](https://github.com/marioal9806/alien_invasion/new/master?readme=1#credits)
- [License](https://github.com/marioal9806/alien_invasion/new/master?readme=1#license)

---
### Installation:
The game package is built using the PyInstaller module, this allows users to have a self-contained executable game. Easy to use, easy to distribute!
Currently the two available **distribution bundles** are the following:
#### Single File Executable:
  Inside the repository of the project, go to the following directory: `single_file/dist` and download the executable file. 
  Once you have it on your computer, just double click it!
  
  
#### Single Folder Distribution:
  Inside the repository of the project, go to the following directory: `single_folder/dist` and download the directory called *alien_invasion*. 
  Once you have it on your computer, find the *alien_invasion.exe* file and double click it!
  
---
### Usage:

Once you open the game window, just press the Play button at the center of the screen to start playing. 
The status bar shows your ships left, the highest score saved, the current score and the current level.

![Initial screen](https://media.giphy.com/media/UQsZsbASYHjCzE00au/giphy.gif)

![New level](https://media.giphy.com/media/ej0i3n7Ia4y4paXdSa/giphy.gif)

![Life lost](https://media.giphy.com/media/RNWCUohdZriXJH9Ami/giphy.gif)

The gameplay dynamics are very simple. Move your ship left or right to point and shoot to the alien ships to earn points. 
The score per each alien ship increments as you progress through the game.
Don't let the aliens touch you! Don't let them get to the earth! As you will lose one ship if any of this happens. 
You have only three extra spaceships, and you can only shoot three lasers at a time. Use your resources wisely!

- Controls:
  - Press **[SPACEBAR]** to shoot.
  - Press **[LEFT_ARROW]** to move left.
  - Press **[RIGHT_ARROW]** to move right.
  - You can quit the game pressing **[Q]** or by clicking the **X** icon of the window.
  
---
### Development:
The Alien Invasion game is an ongoing project. Ideas for further development include:
- [ ] Add a pause button.
- [ ] Add a main screen for the game before it starts.
- [ ] Add options to change the settings.
- [ ] Modify settings of PyInstaller .spec file to save High-Scores in the single file distribution.

If you wish to edit the game it's as simple as cloning this repo. Feel free to add as many features as you like!


The development process revolves around an object-oriented approach to manage every main item in the game with its own python claass and script. 
The Pygame module facilitates the process of creating the game by handling graphics, sprites, collisions and audio. 
For more info, visit the [Pygame documentation](https://www.pygame.org/docs/tut/PygameIntro.html).

Inside each distribution folder you can download the `alien_invasion.spec` file used to build the appplication with the PyInstaller module. 
For more info, visit the [PyInstaller Manual](https://pyinstaller.readthedocs.io/en/stable/index.html).

Furthermore, the `requirements.txt` file shows the pip packages installed in the virtual environment of the project (using venv).

---
### License:

MIT License
Copyright (c) 2020 Mario Ortega
