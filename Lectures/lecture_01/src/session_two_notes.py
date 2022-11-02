## Functions, HOWTO

"""
Make a function (Traditional Way)
"""


import sys


def square(x):
    return x * x


"""
Make a function (Lambda)
"""
def square(x): return x * x  # <- Notice the lack of a return statement

# NOTE: Always use `def` functions, lambdas are only useful for one-time functions

"""
Function arguments.

Functions may take different types of arguments:
- positional arguments (also `args`)
- keyword arguments (also `kwargs`)
"""

"""
`say_hi` takes 1 argument: `person`

You may call this function like so:
>>> say_hi("Marcus") # positional argument
"Hi Marcus!"

>>> say_hi(person="Marcus") # keyword argument
"Hi Marcus!"
"""


def say_hi(person):
    print(f"Hi {person}!")


"""
`say_multiple_his` takes 2 arguments: `people` and `greeting`

You may call this function like so:
>>> say_multiple_his(["Aldo", "Giovanni", "Giacomo"], "Hi")
"Hi Aldo, Hi Giovanni, Hi Giacomo!"

>>> say_multiple_his(["Aldo", "Giovanni", "Giacomo"], greeting="Hi")
"Hi Aldo, Hi Giovanni, Hi Giacomo!"

>>> say_multiple_his(people=["Aldo", "Giovanni", "Giacomo"], greeting="Hi")
"Hi Aldo, Hi Giovanni, Hi Giacomo!"

# WARNING: After a keyword argument, each following argument must be a keyword argument as well
>>> say_multiple_his(people=["Aldo", "Giovanni", "Giacomo"], "Hi")
                     ^^^^^^ <---- Cannot specify a keyword argument a follow with a positional argument
SyntaxError: positional argument follows keyword argument
"""


def say_multiple_his(people, greeting):
    print(f'{greeting} ' + f', {greeting} '.join(people) + '!')


"""
Force positional arguments

Use `/` in your function declarations to FORCE the arguments `before` it to be EXCLUSIVELY positional.
Specifying any of those arguments with their name will raise a TypeError.

>>> positional_only(1, 2)
1

>>> positional_only(x=1, y=2)
TypeError: positional_only() got some positional-only arguments passed as keyword arguments: 'x', 'y'
"""


def positional_only(x, y, /):
    return x ** y


"""
Force keyword arguments

Use `*` in your function declarations to FORCE the arguments `after` it to be EXCLUSIVELY named.
Specifying any of those arguments without their name will raise a TypeError.

"""


def keyword_only(*, x, y):
    return x ** y


sys.stdout.write()
