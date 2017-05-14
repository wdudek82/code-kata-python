import re


string = "ape at the apex"
regex = re.compile(r"\bape\b")  # \b is boundry
match = re.findall(regex, string)
print(match)

print("-" * 10)

string = "Match everything up to @"
regex = re.compile(r"^.*[^@]")  # match everything besides @
match = re.findall(regex, string)
print(match)

print("=" * 10)

string = "@ Get this string"
regex = re.compile(r"[^@\s].*")
match = re.findall(regex, string)
print(match)

print("=" * 10)

string = """Ape is big
Turtle is slow
Cheetah is fast
"""
regex = re.compile(r"(?m)^.*?\s")
match = re.findall(regex, string)
print(match)

print("=" * 10)

string = "My number is 412-555-1212"
regex = re.compile(r"\d{3}-\d{4}")
match = re.findall(regex, string)
print(match)

print("=" * 10)

string = "412-555-1212 412-555-1213 412-555-1214"
regex = re.compile(r"(\d{3}-\d{4})")
match = re.findall(regex, string)
print(match)

string = "My number is 412-555-1212"
regex = re.compile(r"\d{3}-(.*)-(.*)")
match = re.findall(regex, string)
print(match[0][0])
print(match[0][1])