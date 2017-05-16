import re


string = "December 21 1974"
regex = r"^(?P<month>\w+)\s(?P<day>\d{1,2})\s(?P<year>\d{4})"
match = re.search(regex, string)
print(match)
print(match.group('month'))
print(match.group('day'))
print(match.group('year'))
print(match.group(1))


# Exercise
# find all legitimate email addresses
string = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
regex = re.compile(r"([\w+-.]+)@([\w+-]+)([\w.]+)")
match = re.findall(regex, string)

print(match)


# Exercise
# find all telephone numbers
string = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
regex = re.compile(r"((\d{0,1})([-(]*)(\d{3})([-\s)]*)(\d{3})([-\s]*)(\d{4}))")
# regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\)-|)?(\d{3})([-\s])?(\d{4}))")

match = re.findall(regex, string)

for num in match:
    print(num)
