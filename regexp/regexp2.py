import re

string = "cat cats catastrophy"

# regex = re.compile("[cat]+s?")
# regex = re.compile("[cat]+s?")
regex = re.compile(r"[cat]+s?\s")  # cats only
matches = re.findall(regex, string)

for item in matches:
    print(item)

print("-" * 10)

string = "doctor doctors doctor's"
regex = re.compile(r"[doctr]+['s]*")
matches = re.findall(regex, string)

for item in matches:
    print(item)


# Exercise:
# Find lines ended with \r\n or \n
string = """Just some words
        and some more\r
        and more
        and one more time\r
        """

regex_rn = re.compile(r".*\r\n")
regex_n = re.compile(r".*[^\r]\n")

matches_rn = re.findall(regex_rn, string)
matches_n = re.findall(regex_n, string)

print("Lines ended with \\r\\n found: {rn}\nLines ended with \\n found: {n}"
      .format(rn=len(matches_rn), n=len(matches_n)))

# better solution
regex = re.compile(r"[\w\s]+[\r]?\n")
match = re.findall(regex, string)

print(match)