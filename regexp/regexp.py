import re

data = "The ape was at the apex"
pattern = "ape."

result = bool(re.search(pattern, data))
print(result)

searched = re.search(pattern, data)
print(searched.span())
print(searched.start())
print(searched.group())

print('---------------')

all_apes = re.findall(pattern, data)
for i in all_apes:
    print("Found: {}, span:".format(i))

print('---------------')
for i in re.finditer(pattern, data):
    it = i.span()  # indexes tuple
    print("Found: {}, span: {}".format(data[it[0]:it[1]], i.span()))

print('---------------')
animals = "Cat rat mat pat"
all_animals = re.findall(r"[rRcC]at", animals)
print(all_animals)

print('---------------')
owl_food = "rat cat mat pat"
regex = re.compile(r"[cr]at")
for i in re.findall(regex, owl_food):
    print(i)

new_owl_food = regex.sub("owl", owl_food)
print(new_owl_food)

string = "I will go there"
result = re.sub(r"will", "won't", string)
print(result)

print('---------------')
string = "Here is \\stuff"
print(r"Find \\stuff: ", re.search(r"\\stuff", string))

print('---------------')
string = "123456789"
for item in re.findall("\d{2}", string):
    print(item)

# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters
regex = re.compile(r"[\w.%+-]{1,20}@[\w.-]{2,20}\.[a-zA-Z]{2,3}")
string = "gelu47+.%@gmail.com db@aol.com @apple.com db@.com"
print(re.findall(regex, string))