import unittest
from task3 import task3

class task3tests(unittest.TestCase):

    def test_pi(self):
        expected = 3.1415926
        actual = truncate(task3.pi(), 7)
        self.assertEqual(actual, expected)

def truncate(num, digits):
    return int(num * 10**digits) / 10**digits

if __name__ == '__main__':
    unittest.main()