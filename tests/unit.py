import unittest
import sys

sys.path.insert(0,'./ext/imports/')
from dependecies import *
from tkinter import *
from main import *




class TestCal(unittest.TestCase):
    def testadd(self):
        result = Controller.addTest(34,45)
        self.assertEqual(result,79)


if __name__ == '__main__':
    unittest.main()
