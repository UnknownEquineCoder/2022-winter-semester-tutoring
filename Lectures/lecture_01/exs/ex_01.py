"""
# Collatz numbers

### What are collatz numbers?

They are numbers that come from a sort of 'mathematical game'
Start with any number of your choice, then iterate the following steps:

if the number is even, divide it by 2
if the number is odd, multiply it by 3 and add 1

Stop whenever you reach 1

#### BONUS POINTS: Is there any number that you can start this game and NEVER end up to 1?
#### Find such numbers if they exist and I'll give you a cookie
"""


def collatz(x):
    if x % 2 == 0:
        return x // 2
    elif x % 2 != 0:
        return x * 3 + 1


user_input = input("Please give me a number: ")

x = collatz(int(user_input))


def collatz_numbers(x):
    """
    Calculate all collatz numbers starting from x,
    then return them as a list
    """
    results = []

    while x != 1:
        results.append(x)
        x = collatz(x)

    return results


# Make a third function that asks for input until the user says "STOP"
# Each input is to be treated as a single integer
# Calculate the collatz sequence for each such number


results = collatz_numbers(x)

print(results)
