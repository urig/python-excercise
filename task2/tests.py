import unittest
from datetime import datetime, date, time
from task2 import task2

class tests(unittest.TestCase):

    def test_list(self):
        self.assertTrue(type(task2.data_structure()) is list)

    def test_0(self):
        self.assertTrue(type(task2.data_structure()[0]) is int)

    def test_1(self):
        self.assertTrue(type(task2.data_structure()[1]) is float)

    def test_2(self):
        self.assertTrue(type(task2.data_structure()[2]) is str)
    def test_3(self):        
        self.assertTrue(type(task2.data_structure()[3]) is tuple)
        
    def test_3_0(self):        
        self.assertTrue(type(task2.data_structure()[3][0]) is datetime)

    def test_3_1(self):
        self.assertTrue(type(task2.data_structure()[3][1]) is date)

    def test_3_2(self):
        self.assertTrue(type(task2.data_structure()[3][2]) is time)

    def test_4(self):        
        self.assertTrue(type(task2.data_structure()[4]) is set)

if __name__ == '__main__':
    unittest.main()