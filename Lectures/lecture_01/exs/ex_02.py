"""
# Password Generator

The idea of this project is to make a password generator that can produce complex passwords.

The following settings will be introduced by the user, one at the time
When each setting has been filled by a correct value, a password is generated

### Settings:
- length: has to be a number (at least 8 characters for a secure password)
- alphabet: should the password include special characters? what about numbers?

#### Intermediate
- (optional) seed: start with a string and include it to your password

#### Advanced
- Diceware is an open-source algorithm to produce secure and easy to remember passwords
    It works like this:
    - Ask the user for a number (usually greater than 3)
    - Roll 5 dice that many times, and write down the results in order
    - For each group of 5 dice, look up the word in the diceware dictionary
    - Chain the words you obtained this way together
    - (optional) Add more random to your password (capital letters/numbers/symbols)

  You can download a sample dictionary at: https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
"""

import random
import string

# a-z
simple = (string.ascii_lowercase, 8)

# A-Za-z0-9
intermediate = (string.ascii_letters + string.digits, 12)

# A-Za-z0-9#$%&'()*+,-./:;<=>?@[\]^_`{|}~
advanced = (string.ascii_letters + string.digits + string.punctuation, 16)


def get_password_data():
    alphabet, length = "", 0

    print(
        """Which elements do you want in your password?
1) simple
2) intermediate
3) advanced"""
    )
    option = input("> ")

    while option not in ("1", "2", "3"):
        print("Wrong! Not a valid option.")
        option = input("> ")

    uses_seed = input(
        "Would you like to set a seed?\nInsert NO if no seed, otherwise provide seed: "
    )

    if uses_seed == "NO":
        ...
    else:
        random.seed(uses_seed)

    if option == "1":
        alphabet, length = simple
    elif option == "2":
        alphabet, length = intermediate
    else:
        alphabet, length = advanced

    return alphabet, length


alphabet, length = get_password_data()

letters = random.choices(alphabet, k=length)

# Want to get: a string with all letters from `letters` attached
password = "".join(letters)

print(f"{password =}")
