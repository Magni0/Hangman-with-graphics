import requests
import random
import os
import json


class GetWord:

    def from_api():
        url = 'https://random-word-api.herokuapp.com/word?number=1&swear=0'
        r = requests.get(url)  # gets a list of 1 string
        word = json.loads(r.text)
        return word[0]  # returns that 1 element in string

    def from_wordlist():
        # gets the absolute path of get_word.py
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        # defines the path of file 'wordlist.txt' the same as get_word.py
        my_file = os.path.join(THIS_FOLDER, 'wordlist.txt')
        with open(my_file, 'r') as f:
            # reads the file 'wordlist.txt' and gets a word from it
            word = random.choice(f.readlines())
        return word

    def try_api():
        try:
            return GetWord.from_api()
        except Exception:
            return GetWord.from_wordlist()
