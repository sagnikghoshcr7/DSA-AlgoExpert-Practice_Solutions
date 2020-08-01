"""
Numbers In Pi

Given a string representation of the first n digits of Pi and a list of your favorite numbers
(all positive integers in string format),

write a function that returns the smallest number of spaces that need to be added
to the n digits of Pi such that all resulting numbers are found in the list of favorite numbers.
If no number of spaces to be added exists such that all resulting numbers are found in the list of
favorite numbers, the function should return -1.

Sample input:
"3141592653589793238462643383279",
["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
Sample output: 2 ("314159265 | 35897932384626433832 | 79")
"""


# SOLUTION 1

# O(n^3 + m) time | O(n + m) space - where n is the number of digits in Pi and m is the number of favorite numbers
def numbersInPi1(pi, numbers):
    numbersTable = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces


# SOLUTION 2

# O(n^3 + m) time | O(n + m) space - where n is the number of digits in Pi and m is the number of favorite numbers
def numbersInPi2(pi, numbers):
    numbersTable = {number: True for number in numbers}
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, numbersTable, cache, i)
    return -1 if cache[0] == float("inf") else cache[0]


def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx: i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]
