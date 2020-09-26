import unittest
import tracemalloc
from src.get_word import GetWord


class TestGetWord(unittest.TestCase):
    def test_from_api(self):
        test = GetWord.from_api()
        self.assertEqual(type(test), str)

    def test_from_wordlist(self):
        tracemalloc.start()
        test = GetWord.from_wordlist()
        self.assertEqual(type(test), str)
