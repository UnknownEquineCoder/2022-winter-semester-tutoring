"""
## Fizzbuzz

This is a typical interview question.

Consider the first N natural numbers (say, 1..100)

If the number is divisible by 3, print fizz.
If the number is divisible by 5, print buzz.
If the number is divisible by 3 and 5, print fizzbuzz.
Otherwise, print the number itself.


### Variations

#### Intermediate:
Extend the Fizzbuzz algorithm to accept a third number, chug, which will appear on multiples of 7.

#### Advanced:
You receive a list of arbitrary words-to-number combinations.
Dynamically implement a version of Fizzbuzz that works with that list (without knowing its contents).

#### Crazy:
You make a request on the web for a list of numbers and words.
You parse them in the proper format and use multiprocessing to speed up your process.
Use at least 5 subprocesses to analyze the output from 1 to 1000000.
"""

user_input = int(input("How many fizzbuzz numbers would you like? "))


def fizzbuzz(x):
    """
    Compute fizz buzz numbers until x.
    """
    results = []

    for num in range(1, x + 1):
        if num % (3 * 5) == 0:
            results.append("fizzbuzz")
        # If the number is divisible by 3, print fizz
        elif num % 3 == 0:
            results.append("fizz")
        # If the number is divisible by 5, print buzz.
        elif num % 5 == 0:
            results.append("buzz")
        else:
            results.append(num)

    return results


results = fizzbuzz(user_input)

# Extend the Fizzbuzz algorithm to accept a third number,
# 'chug', which will appear on multiples of 7.
# Ex. 7 -> chug, 21 -> fizzchug, 35 -> buzzchug, 105 -> fizzbuzzchug

print(results)

def fizzbuzz_dictionary(max):
    mapping = {
        3: 'fizz',
        5: 'buzz',
        7: 'chug',
    }

    for i in range(1, max+1):
        result = ''
        for key, val in mapping.items():
            if i % key == 0:
                result += val

        if result == '':
            print(i)
        else:
            print(result)


fizzbuzz_dictionary(105)
