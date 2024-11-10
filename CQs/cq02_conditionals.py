"""This is my third challenge question!"""
from pydoc import __author__
__author__

def guess_a_number() -> None:
    secret: int
    secret = 7
    answer: str
    answer = input("Guess a number:")
    print("Your guess was " + answer)
    if int(answer) == secret:
        print("You got it!")
    elif int(answer) > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    elif int(answer) < secret:
        print("Your guess was too low! The secret number is " + str(secret))

if __name__ == "__main__":
        guess_a_number()