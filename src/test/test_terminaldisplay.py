import unittest
import sys
import os
sys.path.append(f'{os.path.dirname(os.path.abspath(__file__))}\..')
from terminal_display import UpdateDisplay

class TestUpdateDisplay(unittest.TestCase):
    def test_update_try_dis(self):
        UpDis = UpdateDisplay([], ['a', 'b', 'c'])
        test = UpDis.update_try_dis()
        expected = 'a b c '
        self.assertEqual(test, expected)
    
    def test_update_ans_dis(self):
        UpDis = UpdateDisplay(['a', 'b', 'c'], [])
        test = UpDis.update_ans_dis()
        expected = 'abc'
        self.assertEqual(test, expected)