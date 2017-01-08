"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.


# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times


# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".


# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.


# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.


# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.

###############################################################################

def hello_world():
    """Prints "Hello World" when called"""

    print "Hello World"


def say_hi(name):
    """Prints "Hi" followed by name"""

    print "Hi {}".format(name)


def print_product(num1, num2):
    """Prints product of two numbers"""

    print int(num1) * int(num2)


def repeat_string(string, num):
    """Prints string num-times"""

    print str(string) * int(num)


def print_sign(num):
    """Compares num to 0 and prints if num is greater, smaller
       or equal to 0"""

    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    else:
        print "Zero"


def is_divisible_by_three(num):
    """Returns True if number is divisible by 3, otherwise returns False"""

    if int(num) % 3 == 0:
        return True
    else:
        return False


def num_spaces(item):
    """Returns number of spaces in a string"""

    return item.count(" ")


def total_meal_price(meal, tip=0.15):
    """Calculates total meal price when passed meal price and tip percentage
       If no tip percentage is passed, tip defaults to 0.15 or 15%"""

    return meal + meal * tip


def sign_and_parity(num):
    """Return sign and parity (Odd or Even) when passed a number in
       list format."""

    if num < 0:
        sign = "Negative"
    # I am assigning 0 and above as Positive
    else:
        sign = "Positive"

    if num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    return [parity, sign]

# Calling the function with number 3 and assigning parity to variable
parity = sign_and_parity(3)[0]

# Calling the function with number 3 and assigning sign to variable
sign = sign_and_parity(3)[1]

# Printing the two variables assigned above
print parity
print sign


###############################################################################

# PART TWO

# 1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string.

# 2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


###############################################################################


def full_title(name, title="Engineer"):
    """Returns title and name in one string"""

    return title + " " + name


def write_letter(name, title, sender):
    """Passes in name, title, and sender name and returns letter"""

    print "Dear {}, I think you are amazing! Sincerely, {}".format(
        full_title(name, title), sender)


###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
