"""This is where I will carry out the Conditionals CQ"""

__author__ = "730796945"


def guess_a_number() -> None:
    """Will take the input of a user and determine if it matches defined variable"""
    secret: int = 7
    x: int = int(input("Guess a number:"))
    print("Your guess was " + str(x) + ".")  # "Your guess was" + input value
    if secret == x:
        print("You got it!")  # if input value matches 7 
    else:
        if secret > x:
            print("Your guess was too low! The secret number is " + str(secret))
            # if input value is less than 7
        else:
            print("Your guess was too high! The secret number is " + str(secret))
            # if input value is greater than 7
            return None


if __name__ == "__main__":
    guess_a_number()
