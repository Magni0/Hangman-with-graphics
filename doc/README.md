github repo : https://github.com/Magni0/Hangman-with-graphics

The solution is split up into the folowing classes:

    - GetWord: this class has three methods
        - from_api: make a GET request to this API https://random-word-api.herokuapp.com/word?number=1&swear=0 with the parameters of only one word and swear words resticted. With a status code 200 the API will send back a random word in the format of json.
        - from_wordlist: opens and reads a file containing a list of 1000 arbitrary words (all have been check to make sure non are offensive or inapropiate) and picks a random word from the list
        - try_api: tries to run from_api method but if it throws an error will run from_wordlist instead
    - HangManGraphic: a class responsible for drawing the hangman using turtle module with a method for each part
        - setup: creates the windows and specify settings such as background color
        - platform: draws the platform
        - head: draws the head
        - torso: draws the torso
        - l_arm: draws the left arm
        - r_arm: draws the right arm
        - l_leg: draws the left leg
        - r_leg: draws the right leg
        - refresh_screen: wipes the turtle window clean
    - Retry: class responsible for asking the user if they wish to play/try again. Also responsible for closing the app
        - retry: asks the user if they wish to play/try again. Returns true if yes
        - check_if_exit: if false uses the sys module to exit the application
        - retry_or_exit: combinds the two previous methods. Exits application if response is no
    - UpdateDisplay: responsible for making the terminal screen neat
        - update_try_dis: makes a list into a string with a whitespace between the elements
        - update_ans_dis: makes a list into a string

modules used and what they were used for:

    - requests: used to make a HTTP GET request to the API
    - os: used in the GetWord.from_wordlist method to specify the directory that wordlist.txt is in as the current working dirctory that ran the file may not be the same as wordlist.txt
    - random: used for its random.choice method for the GetWord.from_wordlist method to select a random word from the output of the read file
    - json: used to make the response of the requests.get method usable in python 
    - turtle: a drawing module used to create a window and draw the hangman
    - time: used for its time.sleep method in the HangManGraphic.refresh_screen method to create a delay before the tutle window refreshes
    - sys: used for its exit method for the Retry.check_if_exit method

![flowchart](/flowchart.jpg)