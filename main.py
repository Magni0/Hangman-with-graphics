import graphic as gr
import random as ran
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # defines the absolute path as main.py
my_file = os.path.join(THIS_FOLDER, 'wordlist.txt') # defines the path of file 'wordlist.txt' the same as main.py
word = ran.choice(open(my_file).readlines()) # reads the file 'wordlist.txt' and makes the contents a list

word_check = [] # used to change the word_dis variable
tried = []

man = (gr.head(), gr.chest(), gr.l_arm, gr.r_arm(), gr.l_leg(), gr.r_leg) # defined function calls in a tuple to be drawn in sequence order
chances = 0 

for i in word:
    word_check.append('-') # fillers until correct letters guessed

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

while True:
    print(update_ans_dis()) # called to show how many letters are in word object
    print(f'you have tried: {update_try_dis()}')
    guess = str(input('guess a letter: ')) 
    if guess == None:
        print('you need to put an answer')
        continue
    elif guess in word:
        guess_index = word.index(guess)
        word_check[guess_index] = guess
        check = update_ans_dis()
        if check == word:
            print('YOU WIN!!!')
            break
    elif guess not in word:
        man[chances]
        tried.append(guess)
        if chances == 5:
            print('you lose :(')
            break
        chances += 1
    else:
        print('logic issue')
        break