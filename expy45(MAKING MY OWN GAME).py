from Eratosfenexpy45 import eratosthenes
import random
import WORDSFORGAME
prime_nums = eratosthenes()
words = WORDSFORGAME


class Game(object):

    def __init__(self):
        temp = random.randint(0, 25)
        self.rand_prime_num = prime_nums[temp]
        self.count_rounds = 0

    def cont(self):
        self.count_rounds += 1

    def right_or_left(self, num):
        if num == self.rand_prime_num:
            print(words.end.format(self.count_rounds))
            exit(0)
        elif num > self.rand_prime_num:
            print("left")
        else:
            print("right")


def input_data(a):
    if (a >= 0) and (a <= 100):
        return a
    else:
        print(words.not_in_range)
        a = int(input(words.inp))
        return input_data(a)


def main():
    print(words.start)
    game = Game()
    print(words.number_guessed)
    while game.count_rounds <= 10:
        game.cont()
        print(f"Round №{game.count_rounds}")
        print(words.next_round)
        a = int(input(words.inp))
        a = input_data(a)
        game.right_or_left(a)

    print("You lost")


main()
