"""
Smallest Difference

Write a function that takes in two non-empty arrays of integers.
The function should find the pair of numbers (one from the first array, one from the second array)
whose absolute difference is closest to zero.

The function should return an array containing these two numbers,
with the number from the first array in the first position.
Assume that there will only be one pair of numbers with the smallest difference.

Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Sample output: [28, 26]
"""


# O(n log(n) + m log(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    a = 0
    b = 0
    smallest = float("inf")
    smallestPair = []
    while a < len(arrayOne) and b < len(arrayTwo):
        firstNum = arrayOne[a]
        secondNum = arrayTwo[b]
        current = abs(firstNum - secondNum)
        if firstNum < secondNum:
            a += 1
        elif firstNum > secondNum:
            b += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
