#!/usr/bin/env python3.6

# Description
# https://www.codewars.com/kata/how-much-water-do-i-need/train/python

# recursive function to count the amount of woter needed
def calculate_additional_water(water, units):
    if units < 1:
        return round(water, 2)
    else:
        return calculate_additional_water(water+(water/10), units-1)


def how_much_water(l, x, n):
    if n > 2 * x:
        return "Too much clothes"
    elif n < x:
        return "not enough clothes"
    return calculate_additional_water(l, n-x)


l, x, n = 50, 15, 29
result = how_much_water(l, x, n)

assert how_much_water(10,10,21) == 'Too much clothes', ''
assert how_much_water(10,10,2) == 'Not enough clothes',''
assert how_much_water(10,11,20) == 23.58, ''
assert how_much_water(50,15,29) == 189.87, ''
