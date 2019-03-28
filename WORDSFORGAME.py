
from textwrap import dedent
start = dedent("""
Hi, I suggest you play a game where you
need to find a simple prime number in the range 
from 1 to 100. I myself guess this number,
and you will offer me numbers, if you guess
wrong, then I will tell you "right" if the
number is to the right of your number, and
"left" if the number is to the left of your number.
You need to guess the number in 10 moves, otherwise you lose
""")

not_in_range = " You need to input numbers from 1 to 100 only, input number again"

end = "You guessed it right, You won in {} moves"

number_guessed = "I just guessed a number, it's time for your move"

inp = '> '

next_round = "Input number"
