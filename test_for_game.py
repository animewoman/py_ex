import unittest
from game import input_try


class TestInputTry(unittest.TestCase):
    def test_input(self):

        data = '1'
        result = input_try(data)
        self.assertEqual(result, data)


if __name__ == '__main__':
    unittest.main()
