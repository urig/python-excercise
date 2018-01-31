import unittest
from task3 import task3

class task3tests(unittest.TestCase):

    def test_pi(self):
        expected = 3.1415926
        actual = truncate(task3.pi(), 7)
        self.assertEquals(actual, expected)
'''
    def test_truncate1(self):
        self.assertEquals(3.1415926, task3.truncate(3.141592611111, 7))

    def test_truncate2(self):
        self.assertEquals(3.1415926, task3.truncate(3.141592699999, 7))
'''

def truncate(num, digits):
    return int(num * 10**digits) / 10**digits

if __name__ == '__main__':
    unittest.main()