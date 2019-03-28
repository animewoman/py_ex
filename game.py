from Eratosfenexpy45 import eratosthenes
import random
import WORDSFORGAME
prime_nums = eratosthenes()
words = WORDSFORGAME


class Game(object):

    def __init__(self):
        temp = random.randint(0, len(prime_nums) - 1)
        self.rand_prime_num = prime_nums[temp]
        self.count_rounds = 0

    def cont(self):
        self.count_rounds += 1

    def right_or_left(self, num):
        if num == self.rand_prime_num:
            return words.end
        elif num > self.rand_prime_num:
            return "left"
        else:
            return "right"


def input_data():
    while True:
        print(words.next_round)
        a = (input(words.inp))
        if a == input_try(a):
            a = int(input_try(a))
            break
        else:
            continue
    return a


def input_try(a):
    try:
        a = int(a)
    except ValueError:
        print("That's not number")
        return a + '10'
    else:
        if (a >= 0) and (a <= 100):
            return str(a)
        else:
            print(words.not_in_range)
            return a + 10


def main():
    print(words.start)
    game = Game()
    print(words.number_guessed)
    win = False
    while game.count_rounds < 10:
        game.cont()
        print("Round № {}".format(game.count_rounds))
        a = int(input_data())
        x = game.right_or_left(a)
        if (x != "right") or (x != "left"):
            print(x.format(game.count_rounds))
            win = True
            break
        else:
            print(x)

    if win is False:
        print("You lost")


main()
