"""
Find Closest Value In BST

You are given a BST data structure consisting of BST nodes.
Each BST node has an integer value stored in a property called "value" and
two children nodes stored in properties called "left" and "right," respectively.

A node is said to be a BST node if and only if it satisfies the BST property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and both of its children nodes are either BST nodes themselves or None (null) values.
You are also given a target integer value;
write a function that finds the closest value to that target value contained in the BST.

Assume that there will only be one closest value.

Sample input:
             10           , 12
          /      \
        5        15
      /   \    /     \
    2      5  13     22
  /             \
 1               14

Sample output: 13
"""


# SOLUTION 1

# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper1(tree, target, float("inf"))


def findClosestValueInBstHelper1(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper1(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper1(tree.right, target, closest)
    else:
        return closest


# SOLUTION 2

# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def findClosestValueInBst2(tree, target):
    return findClosestValueInBstHelper2(tree, target, float("inf"))


def findClosestValueInBstHelper2(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
