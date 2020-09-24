import unittest
from unittest.mock import patch
import sys
import builtins
import os
sys.path.append(f'{os.path.dirname(os.path.abspath(__file__))}\..')
from retry import Retry

class TestRetry(unittest.TestCase):
    @patch('builtins.input', lambda *args: 'y')
    def test_retry_y(self):
        test = Retry.retry()
        self.assertTrue(test)
    
    @patch('builtins.input', lambda *args: 'n')
    def test_retry_n(self):
        test = Retry.retry()
        self.assertFalse(test)
    
class TestCheckIfExit(unittest.TestCase):
    def test_check_true(self):
        test = Retry.check_if_exit(True)
        self.assertFalse(test)
    
    def test_check_exit(self):
        with self.assertRaises(SystemExit) as test:
            Retry.check_if_exit(False)
        self.assertEqual(test.exception.code, 0)

class TestRetryOrExit(unittest.TestCase):
    @patch('builtins.input', lambda *args: 'y')
    def test_retry_or_exit_true(self):
        test = Retry.retry_or_exit()
        self.assertFalse(test)
    
    @patch('builtins.input', lambda *args: 'n')
    def test_retry_or_exit_false(self):
        with self.assertRaises(SystemExit) as test:
            Retry.retry_or_exit()
        self.assertEqual(test.exception.code, 0)