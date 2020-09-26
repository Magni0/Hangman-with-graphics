import unittest
import sys
import tracemalloc
path = '/home/runner/work/Hangman-with-graphics/Hangman-with-graphics/src'
sys.path.append(path)
from get_word import GetWord


class TestGetWord(unittest.TestCase):
    def test_from_api(self):
        test = GetWord.from_api()
        self.assertEqual(type(test), str)

    def test_from_wordlist(self):
        tracemalloc.start()
        test = GetWord.from_wordlist()
        self.assertEqual(type(test), str)
