import sys

# A variadic number of args, then `sep` and `end` as kwargs


def print(*a, sep=" ", end="\n"):
    # Generate a string that concatenates all arguments,
    # separates them by the separator and terminates with the end.
    result = ''

    # Take the first element
    # For every OTHER element, append separator + element
    # ex. print(1, 2, 3, 4, 5)
    # 1 - 2, 3, 4, 5
    # 1 SEP 2 SEP 3 SEP 4 SEP 5

    first, *rest = a

    result += str(first)

    for thing in rest:
        result += sep
        result += str(thing)

    result += end

    sys.stdout.write(result)


""" Short-hand maniac representation
def print(*a, sep=" ", end="\n"):
    sys.stdout.write(f'{sep}'.join([str(el) for el in a]) + end)
"""

print(...)
