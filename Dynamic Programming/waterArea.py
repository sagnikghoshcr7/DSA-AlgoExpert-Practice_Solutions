"""
Water Area

You are given an array of integers.
Each non-zero integer represents the height of a pillar of width 1.
Imagine water being poured over all of the pillars and return the surface area
of the water trapped between the pillars viewed from the front.
Note that spilled water should be ignored.

Refer to the first minute of the video explanation below for a visual example.

Sample input: [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
Sample output: 48
"""


# O(n) time | O(n) space
def waterArea(heights):
    maxes = [0 for _ in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)
    return sum(maxes)
