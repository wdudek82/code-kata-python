import re


# string = "the cat cat fell out dog dog the window"
# regex = re.compile(r"(\b\w+)\s+\1")
# match = re.findall(regex, string)
# print(match)

# string = "<a href='#'><b>The Link</b></a>"
# regex = re.compile(r"<b>(.*?)</b>")
# string = re.sub(regex, r"\1", string)
# match = re.findall(regex, string)
# print(match)
# print(string)

# string = "412-555-1212"
# regex = re.compile(r"(\d{3})-(\d{3}-\d{4})")  # Output should be (412)555-1212
# string = re.sub(regex, r"(\1)\2", string)
# match = re.findall(regex, string)
# print(match)
# print(string)

# Exercise
string = "https://www.youtube.com http://www.google.com"

# Output should look like this:
# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='http://www.google.com'>www.google.com</a>
regex = re.compile(r"(https?://([\w.]+))")
# regex = re.compile(r"https?")
match = re.findall(regex, string)
string2 = re.sub(regex, r"<a href='\1'>\2</a>\n", string)
print(match)
print(string2)
