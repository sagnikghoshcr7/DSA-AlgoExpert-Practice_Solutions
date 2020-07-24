"""
Three Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all triplets in the array that sum up to the target sum and
return a two-dimensional array of all these triplets.

The numbers in each triplet should be ordered in ascending order,
and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
If no three numbers sum up to the target sum, the function should return an empty array.

Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0
Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""


# SOLUTION 1

# O(n^3) time | O(1) space
def threeNumberSum1(array, targetSum):
    ans = []
    for i in range(len(array) - 2):
        firstNum = array[i]
        for j in range(i+1, len(array) - 1):
            secondNum = array[j]
            for k in range(j+1, len(array)):
                thirdNum = array[k]
                if firstNum + secondNum + thirdNum == targetSum:
                    ans.append([firstNum, secondNum, thirdNum])
    return ans


# SOLUTION 2

# O(n^2) time | O(n) space
def threeNumberSum2(array, targetSum):
    array.sort()
    ans = []
    for i in range(len(array) - 2):
        left = i+1
        right = len(array)-1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum > targetSum:
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                ans.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
    return ans
