# Decision Quality Game Platform
This project is for the `Decision Quality Game Platform` to promote the concepts of Decision Quality.

With this web-based platform Decision Quality concepts can be explained in the form of a game. Multiple users can play the game simultaneously and scores are tracked. New games can be added by game developers where currently the following basic building blocks are available: 
1. Click through questions (for explanations), 
2. Drop down questions (for example for categorizing statements), and 
3. Numerical value questions (to check offline calculations). 

With simple syntax for these three basic building blocks, new games can be created. This project includes example games. 

This platform is freely available via GitHub under an Apache 2.0 license, and made possible with financial support from the European Decision Professionals Network (https://www.decisionprofessionals.com/) and CQM (https://www.cqm.nl/).

## About The Project
The concept for the Decision Quality (DQ) Game Platform originated from prof.dr. Kuno Huisman, who teaches DQ concepts in guest lectures. A detailed R&D investment case study was developed and successfully used for over a decade in both university and business settings. To make this material more accessible, the case was broken down into a step-by-step process using Microsoft Forms, which formed the foundational idea for this interactive game platform. The copyright and IP of the platform is owned by Tilburg University, where prof.dr. Kuno Huisman holds the special chair on Decision Making under Uncertainty that is sponsored by ASML. Link to his profile: https://research.tilburguniversity.edu/en/persons/kuno-huisman/?_gl=1*1kw2l5i*_gcl_au*Mzk3MDIxOTMuMTc1ODY1MTcxMw..*FPAU*Mzk3MDIxOTMuMTc1ODY1MTcxMw..   

## Getting Started as Developer
The project uses Python, HTML and JavaScript. To get started you can use for example Visual Studio Code as the IDE.

* Make sure to have installed
	* Python 3.14 (or higher)
	* The python packages specified in the requirements.txt
* To start the app as a developer run ```python app.py``` in the terminal.
* Open the browser for http://127.0.0.1:5000

## How To Define a Game
Instructions on how to define your own game in this platform can be found [here](define_a_game.md)

## How To Deploy
In order to make the game available the project needs deployment on the web. Read how to [deploy the game on Heroku](heroku.md)
