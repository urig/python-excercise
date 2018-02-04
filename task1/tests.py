import unittest
from task1 import task1

class tests(unittest.TestCase):

    def test_helloWorld(self):
        expected = 'Hello, World!'
        actual = task1.helloWorld()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()