import re
from collections import Counter

pieces = re.findall("[A-Z][a-z]?|[0-9]+", "C12H10ClN2O5S")

"""
Correct chemical formula:
    - Elements will be on the periodic table
    - Single elements will have no number after them
    - `Duplicate` elements will have a number after them
"""

last = ""

# {"C": 12}
elements_table = {}

for piece in pieces:
    if piece.isnumeric():
        elements_table[last] = int(piece)
    else:
        elements_table[piece] = 1
        last = piece

print(elements_table)

# last = ""
#
# elements_str = ""
#
# for piece in pieces:
#     if piece.isnumeric():
#         elements_str += last * (int(piece) - 1)
#     else:
#         elements_str += piece
#         last = piece
#
# # "C12H10ClN2O5S" -> CCCCCCCCCCCCCCHHHHHHHHHHClNNOOOOOS
#
# elements_table = dict(Counter(elements_str))
#
# print(elements_table)
