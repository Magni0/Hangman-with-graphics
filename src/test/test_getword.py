import unittest
import sys
import os
import tracemalloc
sys.path.append('/home/runner/work/Hangman-with-graphics/Hangman-with-graphics/src')
from get_word import GetWord

class TestGetWord(unittest.TestCase):
    def test_from_api(self):
        test = GetWord.from_api()
        self.assertEqual(type(test), str)

    def test_from_wordlist(self):
        tracemalloc.start()
        test = GetWord.from_wordlist()
        self.assertEqual(type(test), str)