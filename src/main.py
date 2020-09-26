from terminal_display import UpdateDisplay
from graphic import HangManGraphic as gr
from retry import Retry
from get_word import GetWord

# called in order of how the man is drawn
man = [gr.head, gr.chest, gr.l_arm, gr.r_arm, gr.l_leg, gr.r_leg]

print("{:#^50}".format(" Welcome To HangMan "))
print("type quit at any time to exit")

# done so that if user wants to play again it resets everything
while True:
    chances: int = 0
    word_check: list = []  # used to change the word_dis variable
    tried: list = []

    word = GetWord.try_api()
    # fillers until correct letters guessed
    [word_check.append("-") for i in word]

    gr.setup()

    while True:
        UpdateDis = UpdateDisplay(word_check, tried)
        # called to show how many letters are in word object
        print(UpdateDis.update_ans_dis())
        print(f"you have tried: {UpdateDis.update_try_dis()}")
        guess = input("guess a letter: ")

        if guess == '':
            print("you need to put an answer\n")
            continue

        elif guess == "quit" or guess == "exit":
            Retry.check_if_exit(False)

        elif guess in tried:
            print(f"{guess} has allready been tried")

        elif len(guess) > 1:
            print("you must imput only one letter\n")
            continue  # jumps to begining of loop for user input

        elif guess in word:
            # holds the index of every instance that the letter is in the word
            letter_index = []
            count = 0  # used to represent the index

            # finds every location that letter is in the word
            for letter in word:
                if letter == guess:
                    letter_index.append(count)
                count += 1

            # switches the place holder '-' to the corect letter
            for i in letter_index:
                word_check[i] = guess

            # creates a string of every letter that is correct
            # and places holders for unknown letters
            check = UpdateDis.update_ans_dis()
            if check == word:
                print("YOU WIN!!!")
                gr.refresh_screen()
                Retry.retry_or_exit()
                break

            tried.append(guess)

        elif guess not in word:
            draw = man[chances]
            draw()
            if chances == 5:
                print(f"the word was {word}")
                gr.refresh_screen()
                Retry.retry_or_exit()
                break

            tried.append(guess)
            chances += 1
