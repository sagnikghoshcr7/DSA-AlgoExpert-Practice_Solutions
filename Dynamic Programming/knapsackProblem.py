"""
Knapsack Problem

You're given an array of arrays where each sub-array holds two integer values and represents an item;
the first integer is the item's value, and the second integer is the item's weight.
You're also given an integer representing the maximum capacity of a knapsack that you have.
Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsack's capacity,
all the while maximizing their combined value.

Write a function that returns the maximized combined value of the items that you should pick as well
as an array of the indices of each item picked.

You can assume that there will only be one combination of items that maximizes the total value in the knapsack.

Sample input: [[1, 2], [4, 3], [5, 6], [6, 7]], 10
Sample output: [10, [1, 3]]
"""


# O(nc) time | O(nc) space
def knapsackProblem(items, capacity):
    knapsackValues = [[0 for _ in range(0, capacity + 1)] for _ in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(
                    knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue
                )
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]


def getKnapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))
