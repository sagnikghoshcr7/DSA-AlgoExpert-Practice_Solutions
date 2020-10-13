"""
Shifted Binary Search

Write a function that takes in a sorted array of integers as well as a target integer. The caveat is that
the integers in the array have been shifted by some amount; in other words, they've been moved to the left or
to the right by one or more positions. For example, [1, 2, 3, 4] might have turned into [3, 4, 1, 2]

The function should use a variation of the Binary Search algorithm to determine if the target integer is
contained in the array and should return its index if it is, otherwise -1.

If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of the Binary Search
question's video explanation before starting to code.

Sample Input: [45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33
Sample Output: 8
"""


# SOLUTION 1

# O(log(n)) time | O(log(n)) space
def shiftedBinarySearch1(array, target):
    return shiftedBinarySearchHelper1(array, target, 0, len(array) - 1)


def shiftedBinarySearchHelper1(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    leftNum = array[left]
    rightNum = array[right]
    if target == potentialMatch:
        return middle
    elif leftNum <= potentialMatch:
        if potentialMatch > target >= leftNum:
            return shiftedBinarySearchHelper1(array, target, left, middle - 1)
        else:
            return shiftedBinarySearchHelper1(array, target, middle + 1, right)
    else:
        if potentialMatch < target <= rightNum:
            return shiftedBinarySearchHelper1(array, target, middle + 1, right)
        else:
            return shiftedBinarySearchHelper1(array, target, left, middle - 1)


# SOLUTION 2

# O(log(n)) time | O(1) space
def shiftedBinarySearch2(array, target):
    return shiftedBinarySearchHelper2(array, target, 0, len(array) - 1)


def shiftedBinarySearchHelper2(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        leftNum = array[left]
        rightNum = array[right]
        if target == potentialMatch:
            return middle
        elif leftNum <= potentialMatch:
            if potentialMatch > target >= leftNum:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if potentialMatch < target <= rightNum:
                left = middle + 1
            else:
                right = middle - 1
    return -1
