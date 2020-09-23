from terminal_display import UpdateDisplay
from graphic import HangManGraphic as gr
from retry import Retry as re
from get_word import GetWord

man = [gr.head, gr.chest, gr.l_arm, gr.r_arm, gr.l_leg, gr.r_leg]

print("{:#^50}".format(" Welcome To HangMan "))
print("type quit at any time to exit")

while True: # done so that if user wants to play again it resets everything and gets a new word
    chances: int = 0
    word_check: list = [] # used to change the word_dis variable
    tried: list = []
    
    try:
        word = GetWord.from_api()
    except:
        word = GetWord.from_wordlist()
    
    gr.setup()

    [word_check.append("-") for i in word] # fillers until correct letters guessed
    
    while True:
        UpdateDis = UpdateDisplay(word_check, tried)
        print(UpdateDis.update_ans_dis()) # called to show how many letters are in word object
        print(f"you have tried: {UpdateDis.update_try_dis()}")
        guess = input("guess a letter: ") 
        
        if guess == '':
            print("\nyou need to put an answer\n")
            continue
        
        elif guess == "quit" or guess == "exit":
            re.check_if_exit(False)
        
        elif guess in tried:
            print(f"{guess} has allready been tried")

        elif len(guess) > 1:
            print("\nyou must imput only one letter\n")
            continue

        elif guess in word:
            letter_index = [] # holds the index of every instance that the letter is in the word
            count = 0 # used to represent the index
            
            # finds every location that letter is in the word
            for letter in word:
                if letter == guess: 
                    letter_index.append(count)
                count += 1
            
            # switches the place holder '-' to the corect letter
            for i in letter_index:
                word_check[i] = guess
            
            check = UpdateDis.update_ans_dis() # creates a string of every letter that is correct and has places holders for unknown letters
            
            if check == word:
                print("YOU WIN!!!")
                gr.refresh_screen()
                re.retry_or_exit()
                break

        elif guess not in word:
            draw = man[chances]
            draw()
            if chances == 5:
                print(f"the word was '{word}'")
                gr.refresh_screen()
                re.retry_or_exit()
                break

            tried.append(guess)
            chances += 1