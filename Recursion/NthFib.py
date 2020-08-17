"""
Nth Fibonacci

The Fibonacci sequence is defined as follows:
the first number of the sequence is 0,
the second number is 1,
and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.

Write a function that takes in an integer n and returns the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first 2 numbers as F0 = 0 and F1 = 1.
For the purpose of this question, the first Fibonacci number is F0;
therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc..

Sample input #1: 2
Sample output #1: 1 (0, 1)
Sample input #2: 6
Sample output #2: 5 (0, 1, 1, 2, 3, 5)
"""


# SOLUTION 1

# O(2^n) time | O(n) space
def getNthFib1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib1(n - 1) + getNthFib1(n - 2)


# SOLUTION 2

# O(n) time | O(n) space
def getNthFib2(n, memoize=None):
    if memoize is None:
        memoize = {1: 0, 2: 1}
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib2(n - 1, memoize) + getNthFib2(n - 2, memoize)
        return memoize[n]


# SOLUTION 3

# O(n) time | O(1) space
def getNthFib3(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
