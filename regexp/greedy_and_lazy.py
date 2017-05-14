import re


string = "<name>Life on Mars</name><name>Freaks and Geeks</name>"
regex = re.compile(r"<name>.*</name>")
match = re.findall(regex, string)
print(match)

# regex = re.compile(r"<name>.*?</name>")
regex = re.compile(r"<name>(.*?)</name>")  # now it grabs only names inside tags
match = re.findall(regex, string)
print(match)
