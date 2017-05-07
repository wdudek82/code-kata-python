import string
from random import choice


def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def gen_primes(max_number):
    for num1 in range(2, max_number):
        if isprime(num1):
            yield num1


# print(isprime(13))
prime = gen_primes(50)
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))


# same as above but in form of a generator expression
prime2 = (num for num in range(2, 50) if isprime(num))
print("Prime: ", next(prime2))
print("Prime: ", next(prime2))
print("Prime: ", next(prime2))

print("\nContinue...")

for num in prime2:
    print(num)


# Dictionary comprehension
sample_dict = {char: string.ascii_uppercase.index(char) for char in string.ascii_uppercase}
print(sample_dict)

sample_dict2 = {num: num**2 for num in range(2, 10)}
print(sample_dict2)