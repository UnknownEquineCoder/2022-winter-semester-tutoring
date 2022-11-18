"""

f(x) = x + 1

g(x, y, z) = x + y + z

"""


def f(x):
    return x + 1


def g(x, y, z=4):
    return x + y + z


def k(x, /, y, *, z):
    return x + y + z


# positional arguments
pos = g(1, 2, 3)

print(f"{pos=}")

# key-word arguments
kwargs = g(x=1, y=2, z=3)

print(f"{kwargs=}")

# key-word arguments out of order
kwout_of_order = g(y=2, z=3, x=1)

print(f"{kwout_of_order=}")

# positional + keyword arguments
pos_kwargs = g(1, y=2, z=3)

print(f"{pos_kwargs=}")

# default arguments
default = g(1, y=2)

print(f"{default=}")

# override default arguments
override = g(z=3, x=1, y=2)

print(f"{override=}")

# Constraint calls
constraint = k(1, y=2, z=3)

print(f"{constraint=}")
