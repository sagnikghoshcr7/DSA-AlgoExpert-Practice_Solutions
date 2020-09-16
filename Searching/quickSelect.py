"""
Quick Select

Write a function that takes in an array of distinct integers as well as an integer <span>k</span> and
that returns the kth smallest integer in that array.

The function should do this in linear time, on average.

Sample Input: [8, 5, 2, 9, 7, 6, 3], 3
Sample Output: 5
"""


# Best: O(n) time | O(1) space
# Average: O(n) time | O(1) space
# Worst: O(n^2) time | O(1) space
def quickSelect(array, k):
    position = k - 1
    return quickSelectHelper(array, 0, len(array) - 1, position)


def quickSelectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception("Your algorithm should never arrive here!")
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIdx] > array[rightIdx]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        swap(pivotIdx, rightIdx, array)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1


def swap(one, two, array):
    array[one], array[two] = array[two], array[one]
