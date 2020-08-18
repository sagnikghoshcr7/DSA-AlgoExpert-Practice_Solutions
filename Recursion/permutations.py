"""
Permutations

Write a function that takes in an array of unique integers and returns an array of all permutations of those
integers in no particular order.

If the input array is empty, the function should return an empty array.

Sample Input: [1, 2, 3]
Sample Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""


# SOLUTION 1

# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations1(array):
    permutations = []
    permutationsHelper1(array, [], permutations)
    return permutations


def permutationsHelper1(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper1(newArray, newPermutation, permutations)


# SOLUTION 2

# O(n*n!) time | O(n*n!) space
def getPermutations2(array):
    permutations = []
    permutationsHelper2(0, array, permutations)
    return permutations


def permutationsHelper2(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelper2(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
