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
