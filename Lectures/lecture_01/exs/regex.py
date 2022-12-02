# RegEx => Regular Expression

import re

pattern = "ac..ve"

"""
Special Characters
    - The `.` stands for ANY CHARACTER WILL MATCH
    - The `^` matches the BEGINNING of a string
    - The `$` matches the END of a string
    - 
    - The `[]` make a "sequence"
    - The `()` make a "group"
    - The `|` makes an "alternative"
    - The `\` escapes a character

Special Sequences:
    - all lower-case letters: [a-z]
    - all upper-case letters: [A-Z]
    - all ascii letters: [A-Za-z] \w
    - all digits (numbers 0-9): [0-9] or \d
    - all whitespace chars: \s

Quantifiers:
    - ?: match 0 or 1 of the preceding block
    - +: match one or more of the preceding block
    - *: match any number of the preceding block
    - {n}: match n number of preceding blocks
"""

email_regex = "(\w)+@(\w)+\.(\w){2,3}"  # ([A-Za-z]+)
extension = "\.(\w){2,3}"

email = "noahb@live.com "

emails = """noahb@live.com
dartlife@comcast.net
dburrows@outlook.com
hedwig@att.net
fatelk@msn.com
jaarnial@yahoo.ca
hyper@yahoo.ca
pierce@yahoo.com
aprakash@att.net
bhtower@sbcglobal.net
kildjean@outlook.com
wagnerch@verizon.net"""

compiled_regex = re.compile(email_regex)  # makes regex ~20% faster

for email in emails.split("\n"):
    m = re.match(compiled_regex, email)
    # print(m)
    # print(email[m.pos : m.endpos])

for email in emails.split("\n"):
    m = re.sub(extension, ".at", email)
    print(m)

# Match parentheses encapsulating 3 digits, then a space, then 3 digits, then a dash and finally 4 digits
regex_pn = "^\([0-9]{3}\)[ ]?[0-9]{3}-[0-9]{4,5}$"

phone_numbers = """
(747) 734-62500
(526)645-7703
(721) 756-92495
(233) 473-0266
(588)869-6623
(889) 426-1476
(525) 221-1744
(492)964-0447
(719) 882-13893
(673) 684-5398
"""


"""
Find websites in Austria and Tuvalu

websites country -> extension
Austria             .at
Germany             .de
Tuvalu              .tv
...

Find whether a URL ends in `.at` or `.tv`
.at or .tv
[\.at]|[\.tv]  // MATCH AT LEAST ONE

(\.at)|(\.tv)  // MATCH ALL
"""

website = """
https://www.google.at
https://www.facebook.at
https://www.amazon.at
https://www.imc-fh-krems.at
https://www.somesite.de
https://www.atsomesite.de
https://www.amazon.tv
"""


test_string_2 = """
active states"""

test_string = "my activestate platform account is now active"

result = re.findall(pattern, test_string)

# print(result)
