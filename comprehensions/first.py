from random import randint


even_map = map(lambda x: x*2, range(1, 10))

print(list(even_map))

even = [x*2 for x in range(1, 10)]
print(even)


print(list(filter(lambda x: x % 2 == 0, range(0, 10))))
print([x for x in range(0, 10) if x % 2 == 0])


# Generate 50 values
# Take to the power of 2
# Return multiples of 8
nums = [num**2 for num in range(50) if num % 8 == 0]
print(nums)

nums2 = [x * y for x in range(1, 4) for y in range(10, 13)]
print(nums2)


# Generate a list of 10 values
# Multiply them by 2
# Return multiples of 8
nums3 = [x for x in [y * 2 for y in range(10)] if x % 8 == 0]
print(nums3)


# Problem
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# You'll have to use a list comprehension in a list comprehension
nums4 = [x for x in [randint(1, 1001) for _ in range(50)] if x % 9 == 0]
print(nums4)


# multi-dimentional lists
multi_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print second column
row_2 = [col[1] for col in multi_list]
print(row_2)

# print diagonal
diag_1 = [multi_list[_][_] for _ in range(len(multi_list))]
print(diag_1)