## Functions, HOWTO

"""
Make a function (Traditional Way)
"""


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

>>> keyword_only(1, 2) 
TypeError: keyword_only() takes 0 positional arguments but 2 were given

>>> keyword_only(x=1, y=2)
1
"""


def keyword_only(*, x, y):
    return x ** y


"""
Combine both syntaxes

>>> some_positional_some_named(1, 2, z=3)
2

>>> some_positional_some_named(1, y=2, z=3)
2

>>> some_positional_some_named(x=1, y=2, z=3)
TypeError: some_positional_some_named() got some positional-only arguments passed as keyword arguments: 'x'

>>> some_positional_some_named(1, 2, 3)
TypeError: missing keyword-only argument: 'z'
"""


def some_positional_some_named(x, /, y, *, z):
    return x - y + z
