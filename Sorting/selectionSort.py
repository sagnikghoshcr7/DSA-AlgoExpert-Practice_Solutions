"""
Selection Sort

Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Selection Sort algorithm to sort the array.

Sample Input: [8, 5, 2, 9, 5, 6, 3]
Sample Output: [2, 3, 5, 5, 6, 8, 9]
"""


# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
