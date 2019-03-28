import unittest
from game import input_try
from game import Game


class TestInputTry(unittest.TestCase):
    def test_input(self):

        data = 1
        result = input_try(data)
        expected_output = '1'
        self.assertEqual(result, expected_output)

        data = "asdfasdfas"
        result = input_try(data)
        expected_output = data + '10'
        self.assertEqual(result, expected_output)

        data = -1
        result = input_try(data)
        expected_output = data + 10
        self.assertEqual(result, expected_output)

        data = "ASDFASDFASDGG"
        result = input_try(data)
        expected_output = data + '10'
        self.assertEqual(result, expected_output)

        data = 123
        result = input_try(data)
        expected_output = data + 10
        self.assertEqual(result, expected_output)

        data = "311231c4sdfasdfag23141dsfgag"
        result = input_try(data)
        expected_output = data + '10'
        self.assertEqual(result, expected_output)

        data = "12 adf asf 123"
        result = input_try(data)
        expected_output = data + '10'
        self.assertEqual(result, expected_output)


class GameTest(unittest.TestCase):

    def test_right_or_left(self):
        game_obj = Game()
        game_obj.rand_prime_num = 37
        result = game_obj.right_or_left(num=3)
        expected_output = "right"
        self.assertEqual(result, expected_output)

        result = game_obj.right_or_left(num=40)
        expected_output = "left"
        self.assertEqual(result, expected_output)

        result = game_obj.right_or_left(num=37)
        expected_output = "You guessed it right, You won in {} moves"
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
