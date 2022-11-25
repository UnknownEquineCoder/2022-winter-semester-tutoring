"""
Write a Python program that prints the sum the squares of numbers in any given range.

e.g., range 10 to 14 Sum : 10*10 + 11*11 + 12*12 * 13*13 = 534
"""

# Ask user for the first number in the range
start = input("Give me the first number: ")

# We want to keep asking UNTIL the input can be converted into a number
# The str.isnumeric function does exactly that
#
# NOTE: Whenever you have a problem that has the word UNTIL inside
#       You can translate it at WHILE NOT (like in this example)
while not start.isnumeric():
    start = input("Give me the first number: ")


# Convert the input into a integer
start = int(start)


# Ask user for the second number in the range
end = input("Give me the second number: ")


# Do the same input check we did for the firts number
while not end.isnumeric():
    end = input("Give me the second number: ")

# Convert the second value into a integer
end = int(end)

# EXERCISE:
# make it a while, to keep asking for input
# until end > start
# Instead of checking only once


if end > start:
    # Range will return a sequence with all the numbers from start to end-1
    # e.g. range(10, 14) = 10, 11, 12, 13
    numbers = range(start, end)

    # initialise the total to 0, then add up the results
    total = 0

    # Loop through each number in the range
    for i in numbers:
        # total = total + i ** 2
        # Add the square of each value to the total
        total += i**2

    print(f"The total is {total}")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
"""
Notes on Lists, Dictionaries and Sets
"""
# We can store people using a simple list
people_list = ["Marcel", "John", "Nick", "Kamala", "Deepak"]

# And we can access elements by their index
# NOTE: An index is a positive integer from 0 to the length of the list - 1

marcel = people_list[0]

# What would happen if we had a very large list?
huge_list = [
    "Fabian",
    "Alberto",
    "Osvaldo",
    "Branson",
    "Benjamin",
    "Demarion",
    "Dylan",
    "Kason",
    "Kellen",
    "Armando",
    "Semaj",
    "Konnor",
    "Ralph",
    "Salvador",
    "Deshawn",
    "Eduardo",
    "Jude",
    "Devon",
    "Ronnie",
    "Cristopher",
    "Arjun",
    "Jasiah",
    "Rex",
    "Blaze",
    "Ace",
    "Dominique",
    "Tobias",
    "Jorden",
    "Mohammed",
    "Aaron",
    "Robert",
    "Jace",
    "Owen",
    "Trey",
    "Luke",
    "Holden",
    "Ramiro",
    "Lawrence",
    "Miles",
    "Kareem",
    "Kyler",
    "Geovanni",
    "Andy",
    "Leonel",
    "Alijah",
    "Lewis",
    "Malaki",
    "Donavan",
    "Kolten",
    "Liam",
    "Neil",
    "Layton",
    "Stephen",
    "Davion",
    "Victor",
    "Santos",
    "Yurem",
    "Kobe",
    "Douglas",
    "Jessie",
    "Jayvon",
    "Cael",
    "Joshua",
    "Tony",
    "Lee",
    "Titus",
    "Mason",
    "Raul",
    "Jordan",
    "Dustin",
    "Brennen",
    "Jayson",
    "Kymani",
    "Dallas",
    "Charlie",
    "Rayan",
    "Boston",
    "Justin",
    "Ricky",
    "Hugh",
    "Gael",
    "Finley",
    "Jamari",
    "Conor",
    "Armani",
    "Orlando",
    "Kamden",
    "Augustus",
    "Trevon",
    "Marvin",
    "Jadon",
    "Yosef",
    "Aldo",
    "Brice",
    "Deacon",
    "Santino",
    "Aditya",
    "Rudy",
    "Noah",
    "Ulises",
]

# Is the name "Owen" in the list?
# How would you check for that?

# The usual way is this:

for name in huge_list:
    if name == "Owen":
        print("Owen is in the list!")

# But you would need to iterate through the entire list!
# That's very expensive when you have a lot of data

# We can make things a bit better with sets
huge_set = {  # <- Note the curly braces
    "Fabian",
    "Alberto",
    "Osvaldo",
    "Branson",
    "Benjamin",
    "Demarion",
    "Dylan",
    "Kason",
    "Kellen",
    "Armando",
    "Semaj",
    "Konnor",
    "Ralph",
    "Salvador",
    "Deshawn",
    "Eduardo",
    "Jude",
    "Devon",
    "Ronnie",
    "Cristopher",
    "Arjun",
    "Jasiah",
    "Rex",
    "Blaze",
    "Ace",
    "Dominique",
    "Tobias",
    "Jorden",
    "Mohammed",
    "Aaron",
    "Robert",
    "Jace",
    "Owen",
    "Trey",
    "Luke",
    "Holden",
    "Ramiro",
    "Lawrence",
    "Miles",
    "Kareem",
    "Kyler",
    "Geovanni",
    "Andy",
    "Leonel",
    "Alijah",
    "Lewis",
    "Malaki",
    "Donavan",
    "Kolten",
    "Liam",
    "Neil",
    "Layton",
    "Stephen",
    "Davion",
    "Victor",
    "Santos",
    "Yurem",
    "Kobe",
    "Douglas",
    "Jessie",
    "Jayvon",
    "Cael",
    "Joshua",
    "Tony",
    "Lee",
    "Titus",
    "Mason",
    "Raul",
    "Jordan",
    "Dustin",
    "Brennen",
    "Jayson",
    "Kymani",
    "Dallas",
    "Charlie",
    "Rayan",
    "Boston",
    "Justin",
    "Ricky",
    "Hugh",
    "Gael",
    "Finley",
    "Jamari",
    "Conor",
    "Armani",
    "Orlando",
    "Kamden",
    "Augustus",
    "Trevon",
    "Marvin",
    "Jadon",
    "Yosef",
    "Aldo",
    "Brice",
    "Deacon",
    "Santino",
    "Aditya",
    "Rudy",
    "Noah",
    "Ulises",
}

# Using the `in` keyword, we can check whether Owen is contained in constant time
# Constant time means, no matter how many elements, it will always take X microseconds
# NOTE: the `in` keyword works on lists as well, BUT it does essentially the same
#       as I've shown above, so it will iterate through the entire list to find such a value
#       Try and think what would happen with 10 Billion names!

has_owen = "Owen" in huge_set


# Dictionaries allow a further improvement for many use cases!
# Say, for examples, you want to store names and the associated emails
# Let's try to implement something using lists and tuples

names_and_emails = [
    ("Marcel", "m-repr@uniacad.net"),
    ("John", "jlofan@spotifive.com"),
    ("Nick", "nick@lesscage.at"),
    ("Kamala", "kharris@vpotus.gov"),
    ("Deepak", "admin@responsibility.at"),
]

# `names_and_emails` is a list of tuples
# the first element of each tuple is the name, the second is the email
# In this way, we achieved `loose coupling` of the data

# How would you look for Deepak's email?

for element in names_and_emails:
    if element[0] == "Deepak":
        print(f"Deepak's email is: {element[1]}")

# So we need to iterate through ALL the elements of the list and use
# manual access `[] operator` for each element
# What if we try to build a web service with 1 million users?
# Would you want to look through each user when trying to register a new user?
# And what if some data is malformed and no email is provided?
# And lastly, how would you check for two users with the same name?

# Let's see if sets can solve the issue
names_and_emails_set = {
    ("Marcel", "m-repr@uniacad.net"),
    ("John", "jlofan@spotifive.com"),
    ("Nick", "nick@lesscage.at"),
    ("Kamala", "kharris@vpotus.gov"),
    ("Deepak", "admin@responsibility.at"),
}

# Now sets aren't much better either, because we can't just check for the name

# >> `"Deepak" in names_and_emails`
#    False

# We can use dictionaries to solve this issue
names_and_emails_dictionary = {
    "Marcel": "m-repr@uniacad.net",
    "John": "jlofan@spotifive.com",
    "Nick": "nick@lesscage.at",
    "Kamala": "kharris@vpotus.gov",
    "Deepak": "admin@responsibility.at",
}

# Find deepak's email

deepaks_email = names_and_emails_dictionary["Deepak"]

# alternative method

deepaks_email = names_and_emails_dictionary.get("Deepak")

# Like for sets, dictionary access happen at CONSTANT TIME
# Many databases are actually built in a similar way (MongoDB)

# NOTE: Iteration on dictionaries

# By default dictionaries iterate the KEYS
for (
    name
) in names_and_emails_dictionary:  # alternatively: names_and_emails_dictionary.keys()
    print(f"Name is {name}")
    print(f"Email is {names_and_emails_dictionary[name]}")

# If you want just the emails, you can do this
for email in names_and_emails_dictionary.values():
    print(f"Email is {email}")

# If you want both names and emails, do this instead
for name, email in names_and_emails_dictionary.items():
    print(f"Name is: {name}, email: {email}")
