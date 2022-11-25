import random
from random import Random  # Please stick to the random module instead of the class
import sys  # Some random is located here, but do not use
import math

numbers = [str(num) for num in range(20)]

# pick a single item from a list
element = random.choice(numbers)

# pick multiple (3) items from a list
elements = random.choices(numbers, k=3)

# get a random INT from a (1) to b (10)
rand_int = random.randint(1, 10)

rand_int_conv = math.ceil(int(random.random() * 10))

# get a random FLOAT from a (1) to b (10)
rand_float = random.random() * 10

# get a random int from a range (1, 20, 3)
rand_from_range = random.randrange(1, 20, 3)

# Make your random numbers predictable by setting a seed
random.seed("InsertSomeSeedHere")
random.seed(54894898898948)
