from terminal_display import UpdateDisplay
from graphic import HangManGraphic as gr
from retry import Retry as re
from get_word import GetWord
import sys

word_check = [] # used to change the word_dis variable
tried = []

man = [gr.head, gr.chest, gr.l_arm, gr.r_arm, gr.l_leg, gr.r_leg]

while True:
    retry: bool = False
    chances: int = 0
    word_check: list = [] # used to change the word_dis variable
    tried: list = []
    
    try:
        word = GetWord.from_api()
    except:
        word = GetWord.from_wordlist()
    
    gr.setup()

    [word_check.append('-') for i in word] # fillers until correct letters guessed
    
    print('{:#^50}'.format(' Welcome To HangMan '))
    print('type quit at any time to exit')
    
    while True:
        UpdateDis = UpdateDisplay(word_check, tried)
        print(UpdateDis.update_ans_dis()) # called to show how many letters are in word object
        print(f'you have tried: {UpdateDis.update_try_dis()}')
        guess = input('guess a letter: ') 
        
        if guess == '':
            print('\nyou need to put an answer\n')
            continue
        
        elif guess == 'quit' or guess == 'exit':
            sys.exit(0)
        
        elif len(guess) > 1:
            print('\nyou must imput only one letter\n')
            continue

        elif guess in word:
            guess_index = word.index(guess)
            word_check[guess_index] = guess
            check = UpdateDis.update_ans_dis()
            if check == word:
                print('YOU WIN!!!')
                gr.refresh()
                retry = re.check_retry()
                if retry == True:
                    break
                else:
                    sys.exit(0)

        elif guess not in word:
            draw = man[chances]
            draw()
            if chances == 5:
                print(f'the word was {word}')
                retry = re.check_retry()
            tried.append(guess)
            chances += 1