import re



# Look Ahead
# (?=expression)
string = "One two three four"
regex = re.compile(r"\w+(?=\b)")
match = re.findall(regex, string)
print(match)


# Look Behind
# (?<=expression)
string = "1. Bread 2. Apples 3. Lettuce"
regex = re.compile(r"(?<=\d.\s)\w+")
match = re.findall(regex, string)
print(match)


# Both
string = "<h1>I'm important</h1> <h1>So am I</h1>"
regex = re.compile(r"(?<=<h1>).+?(?=</h1>)")
match = re.findall(regex, string)
print(match)


# Negative Look Ahead & Negative Look Behind
# (?!expression): Negative Look Ahead
# (?<!expression): Negative Look Behind
string = "8 Apples $2, 1 Bread $1, 1 Cereal $4"
regex = re.compile(r"(?<!\$)\d+")
match = re.findall(regex, string)
print(match)

sum_of_food = sum([int(num) for num in match])
print("Sum of all fruits: {}".format(sum_of_food))