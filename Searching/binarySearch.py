"""
Binary Search

Write a function that takes in a sorted array of integers as well as a target integer.
The function should use the Binary Search algorithm to find if the target number is
contained in the array and should return its index if it is, otherwise -1.

Sample input: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33
Sample output: 3
"""


# O(log(n)) time | O(log(n)) space
def binarySearchRecursive(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    if target == array[middle]:
        return middle
    elif target < array[middle]:
        return binarySearchRecursive(array, target, left, middle - 1)
    else:
        return binarySearchRecursive(array, target, middle + 1, right)


# O(log(n)) time | O(1) space
def binarySearchIterative(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1
