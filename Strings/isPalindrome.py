"""
Palindrome Check

Write a function that takes in a non-empty string and that returns a boolean representing whether the string
is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character
strings are palindromes.

Sample Input: "abcdcba"
Sample Output: true
"""


# SOLUTION 1

# O(n^2) time | O(n) space
def isPalindrome1(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString


# SOLUTION 2

# O(n) time | O(n) space
def isPalindrome2(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString


# SOLUTION 3

# O(n) time | O(n) space
def isPalindrome3(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome3(string, i + 1)


# SOLUTION 4

# O(n) time | O(1) space
def isPalindrome4(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
