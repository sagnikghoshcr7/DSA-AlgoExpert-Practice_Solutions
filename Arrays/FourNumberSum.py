"""
Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets in the array that sum up to the target sum
and return a two-dimensional array of all these quadruplets in no particular order.

If no four numbers sum up to the target sum, the function should return an empty array.

Sample input: [7, 6, 4, -1, 1, 2], 16
Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]
"""


# Avg: O(n^2) time | Worst: O(n^3) time | O(n^2) space
def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)-1):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets

print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))