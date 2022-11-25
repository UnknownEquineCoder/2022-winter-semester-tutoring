import random

# Read diceware.txt from file system
# diceware = open("diceware.txt", "rt")
#
# diceware_lines = diceware.readlines()
#
# for line in diceware_lines:
#     print(line)
#
# diceware.close()


diceware_dict = {}

with open("diceware.txt", "rt") as diceware:
    for line in diceware:
        key, val = line.split("\t")
        diceware_dict[key] = val.strip()


def roll_dice(quantity):
    dices = []
    for _ in range(quantity):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        dices.append(dice)

    return dices


def make_diceware_password(length):
    keys = []
    for _ in range(length):
        dices = roll_dice(5)

        # key = ""
        # for roll in dices:
        #     key += str(roll)

        key = "".join(str(element) for element in dices)
        keys.append(key)
    password = "-".join(diceware_dict[key].capitalize() for key in keys)
    password += "-" + str(random.randint(0, 9))
    return password


password = make_diceware_password(5)
print(password)
