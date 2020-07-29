"""
Min Number Of Coins For Change

Given an array of positive integers representing coin denominations
and a single non-negative integer representing a target amount of money,
implement a function that returns the smallest number of coins needed to
make change for that target amount using the given coin denominations.

Note that an unlimited amount of coins is at your disposal.

If it is impossible to make change for the target amount, return -1.

Sample input: 7, [1, 5, 10]
Sample output: 3 (2x1 + 1x5)
"""


# O(n*denoms) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    nums = [float('inf') for _ in range(n+1)]
    nums[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                nums[amount] = min(nums[amount], nums[amount-denom]+1)
    return nums[n] if nums[n] != float('inf') else -1
