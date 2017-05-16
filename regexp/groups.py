import re


# bday = input("Enter your birthday (dd-mm-yyyy): ")
bday = "11-11-2011"
bd_regex = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bday)
print(bd_regex.string)

print("Birth day: {}".format(bd_regex.group(1)))
print("Birth month: {}".format(bd_regex.group(2)))
print("Birth year: {}".format(bd_regex.group(3)))


match = re.search(r"\d{2}", "The chicken weighed 13 lbs")
print(match.group())
