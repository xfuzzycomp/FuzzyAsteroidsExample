# FuzzyAsteroidsExample

This repository holds the example code needed for the 2021 University of Cincinnati Fuzzy Challenge.

## The Challenge

AI agents will be developed using Machine Learning algorithms and Fuzzy Inference Systems in the game/environment provided. For Spring 2021, the game will be a version of the classic arcade game "Asteroid" where the player/agent controls a vehicle that can move and fire at asteroids around them.

Further details on the competition aspect of the challenge will be decided soon.

## Getting Started

1. Install a Python interpreter (with pip), make sure the Python executable is on your System PATH. 
[Download Python here.](https://www.python.org/downloads/)
2. Install GIT on your computer [Download GIT here.](https://git-scm.com/downloads)
3. Install your preferred IDE (see below.)
4. Connect GIT + Python to your IDE (follow the directions for your specific IDE)
5. Clone this repository through your GIT Graphical User Interface or via

    ```git clone https://github.com/TimArnettThales/UCFuzzyChallenge```

6. In the command line, run the following command

    ```pip install -r requirements.txt```

7. Now you should be able to run Asteroid Smasher!

## Updating the FuzzyAsteroids environment

We may make occasional improvements to the FuzzyAsteroids environment and will push to this repository. 
[https://github.com/TimArnettThales/FuzzyAsteroids](https://github.com/TimArnettThales/FuzzyAsteroids)

If you wish to upgrade ALL of your project dependencies, you can use the following command. 

    pip install --upgrade --force-reinstall -r requirements.txt

If you wish to upgrade ONLY the Fuzzy Asteroids environment, you can also do the following

    pip install --upgrade --force-reinstall  git+https://github.com/TimArnettThales/FuzzyAsteroids.git@master#egg=fuzzy_asteroids

## Selecting an IDE

* [Pycharm Community](https://www.jetbrains.com/pycharm/download/)
* [Visual Studio Code](https://code.visualstudio.com/)
