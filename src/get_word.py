import requests
import random
import os
import json

class GetWord:
    def from_api():
        r = requests.get('https://random-word-api.herokuapp.com/word?number=1&swear=0') # gets a list of 1 string
        word = json.loads(r.text)
        return word[0] # returns that 1 element in string
    
    def from_wordlist():
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # defines the current working dir as get_word.py 
        my_file = os.path.join(THIS_FOLDER, 'wordlist.txt') # defines the path of file 'wordlist.txt' the same as get_word.py
        word = random.choice(open(my_file).readlines()) # reads the file 'wordlist.txt' and gets a word from it
        return word