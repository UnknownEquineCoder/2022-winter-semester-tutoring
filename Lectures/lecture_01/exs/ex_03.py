"""
# Move to back

In this exercise, we implement a simplified move-to-back algorithm.

In order:
    - Start with an empty list
    - Keep asking the user for a single-letter string (character)
    - If the letter is present in the list, move it to the end
    - Otherwise, just add it to the end
    - User can stop program execution by entering a certain keyword ('END' for example)

When the user decides to quit the program, display the resulting string

### Advanced
Extend this exercise for arbitrary-length strings
"""

from string import ascii_letters

terminator = 'END'


def is_valid_char(letter, length=1, letter_list=ascii_letters):
    """
    We define a valid character to be a string of length n
    that is contained inside a letter list
    """
    return len(letter) == length and letter in letter_list


def ask_for_char(terminator=terminator):
    letter = input('>> ')

    # Verify whether the char is a single letter
    while not is_valid_char(letter):
        if letter == terminator:
            return None
        letter = input('>> ')

    return letter


def move_to_back():
    result = []

    letter = ask_for_char()

    while letter is not None:
        if letter in result:
            result.remove(letter)

        result.append(letter)

        letter = ask_for_char()

    return result


if __name__ == "__main__":
    seq = move_to_back()
    print(f'{seq=}')
