import graphic as gr
import random as ran
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # defines the absolute path as main.py
my_file = os.path.join(THIS_FOLDER, 'wordlist.txt') # defines the path of file 'wordlist.txt' the same as main.py

word_check = [] # used to change the word_dis variable
tried = []

def update_try_dis(): # function that makes tried object print neatly in terminal
    try_dis = ''
    for i in tried:
        try_dis += i + ' '
    return try_dis

def update_ans_dis(): # function that makes word_check print neatly in terminal
    word_dis = ''
    for i in word_check:
        word_dis += i
    return word_dis

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
    hm = ran.choice(open(my_file).readlines()) # reads the file 'wordlist.txt' and makes the contents a list
    gr.turtle_setup()

    [word_check.append('-') for i in hm] # fillers until correct letters guessed
    
    while True:
        print(update_ans_dis()) # called to show how many letters are in word object
        print(f'you have tried: {update_try_dis()}')
        guess = str(input('guess a letter: ')) 
        
        if guess == None:
            print('you need to put an answer')
            continue
        
        elif guess in hm:
            guess_index = hm.index(guess)
            word_check[guess_index] = guess
            check = update_ans_dis()
            if check == hm:
                print('YOU WIN!!!')
                gr.refresh()
                retry = check_retry()
        
        elif guess not in hm:
            if chances == 0:
                gr.head()
            elif chances == 1:
                gr.chest()
            elif chances == 2:
                gr.l_arm()
            elif chances == 3:
                gr.r_arm()
            elif chances == 4:
                gr.l_leg()
            elif chances == 5:
                print('you lose :(')
                gr.r_leg()
                gr.refresh()
                retry = check_retry()

            tried.append(guess)
            chances += 1
        
        if retry == True:
            break