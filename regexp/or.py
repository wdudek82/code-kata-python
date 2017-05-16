import re


string = "1. Dog 2. Cat 3. Turtle"
regex = re.compile(r"\d\.\s(Dog|Cat)")
match = re.findall(regex, string)

print(match)


# Exercise
# Find all sequences of 5 numbers in a row or 5-4 number
string = "12345 12345-1234 1234 12346-333"
regex = re.compile(r"\d{5}\s|\d{5}-\d{4}")
match = re.findall(regex, string)

print(match)