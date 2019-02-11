import unittest
from task1 import task1

class tests(unittest.TestCase):

    def test_hello_world(self):
        expected = 'Hello, World!'
        actual = task1.hello_world()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
