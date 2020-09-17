from display import UpdateDisplay
from graphic import TurtleGraphic
import random as ran
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # defines the absolute path as main.py
my_file = os.path.join(THIS_FOLDER, 'wordlist.txt') # defines the path of file 'wordlist.txt' the same as main.py

word_check = [] # used to change the word_dis variable
tried = []
gr = TurtleGraphic

man = [gr.head, gr.chest, gr.l_arm, gr.r_arm, gr.l_leg, gr.r_leg]

def check_retry():
    while True:
        print('Do you want to try again? y/n')
        choice = input('').lower()
        if choice == 'n':
            exit()
        elif choice == 'y':
            return True
        else:
            print('invalid input')

while True:
    retry = False
    chances = 0
    word_check = [] # used to change the word_dis variable
    tried = []
    
    word = ran.choice(open(my_file).readlines()) # reads the file 'wordlist.txt' and makes the contents a list
    gr.turtle_setup()

    [word_check.append('-') for i in word] # fillers until correct letters guessed
    
    while True:
        UpdateDis = UpdateDisplay(word_check, tried)
        print(UpdateDis.update_ans_dis()) # called to show how many letters are in word object
        print(f'you have tried: {UpdateDis.update_try_dis()}')
        guess = str(input('guess a letter: ')) 
        
        if guess == None:
            print('you need to put an answer')
            continue
        
        elif guess in word:
            guess_index = word.index(guess)
            word_check[guess_index] = guess
            check = UpdateDis.update_ans_dis()
            if check == word:
                print('YOU WIN!!!')
                gr.refresh()
                retry = check_retry()

        elif guess not in word:
            draw = man[chances]
            draw()
            if chances == 5:
                retry = check_retry()

            tried.append(guess)
            chances += 1
        
        if retry == True:
            break