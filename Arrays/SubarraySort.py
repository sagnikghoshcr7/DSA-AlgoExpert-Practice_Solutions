"""
Subarray Sort

Write a function that takes in an array of integers of length at least 2.
The function should return an array of the starting and ending indices of the
smallest subarray in the input array that needs to be sorted in place in order
for the entire input array to be sorted.

If the input array is already sorted, the function should return [-1, -1].

Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Sample output: [3, 9]

"""


# O(n) time | O(1) space
def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if OutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == float("inf"):
        return [-1, -1]
    leftIndex = 0
    while minOutOfOrder >= array[leftIndex]:
        leftIndex += 1
    rightIndex = len(array) - 1
    while maxOutOfOrder <= array[rightIndex]:
        rightIndex -= 1

    return [leftIndex, rightIndex]


def OutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]
