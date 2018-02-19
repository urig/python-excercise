import unittest
from task5 import task5

class tests(unittest.TestCase):

    def test_reverse_file(self):
        # arrange
        expected = 'god yzal eht revo spmuj xof nworb kciuq ehT'
        # act
        task5.reverse_file('task5/input.txt', 'task5/output.txt')
        # assert
        output_file = open('task5/output.txt')
        actual = output_file.read()
        output_file.close()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()