#!/usr/bin/env python3.6

# Write a method smash that takes an array of words and
# smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation,
# but you should add spaces between each word. Be careful,
# there shouldn't be a space at the beginning or the end of the sentence!

def smash(words):
    return " ".join(words)

assert smash(["hello"]) == "hello", "Error: result != hello"
assert smash(["hello, World"]) == "hello, World", "Error: result != 'hello, World'"
