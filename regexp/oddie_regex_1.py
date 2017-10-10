#!/usr/bin/env python3.6
import re


with open("oddie_regex_1.txt") as f:
    data = f.read()

    # regex = re.compile(r"(\+48-)\d{3}-\d{3}-\d{3,4}")
    regex = re.compile(r"")
    match = re.findall(regex, data)

    print(match)
