# Hangman with Graphics

## What is it?

As the name implyes this is a recreation of the populor word guessing game Hangman made for the terminal with some graphics of the well.... the hangman.

## What does it require to run?

This Hangman game is rather simple it does require python to run as it is a python application preferably python version 3.8 as that was what it was written in but any version of python 3 should run it with no issue though I have not botherd to test this.

( for you convenience if you dont allready have python here is the download link for python 3.8.5 https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe )

Additionaly main.py, graphic.py & wordlist.txt need to be in the same directory for the app to run properly.

You will also need python3 pip to install the modules that aren't part to the standed library if you do have it just run this:

    python -m pip install {path to reqirements.txt}

or

    python -m pip install requests

if you dont have pip you can install it by running this command for linux:

    sudo apt-get install python3-pip

or for windows run these commands in cmd:

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

## How to run it

( Just on the off chance you dont know )

The app will run properly just by duble clicking main.py or you can run it in the terminal by typing 'python {path to file}' as long as the conditions ubove have been met.

## Can I change the words hangman uses and not just have the default ones?

Of course you can add, remove or switchout any of the words in the wordlist.txt file with whatever you want just make sure not to change the name or the file wont be read.