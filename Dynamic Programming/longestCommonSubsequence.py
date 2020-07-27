"""
Longest Common Subsequence

Implement a function that returns the longest subsequence common to two given strings.
A subsequence is defined as a group of characters that appear sequentially,
with no importance given to their actual position in a string.

In other words, characters do not need to appear consecutively in order to form a subsequence.

Assume that there will only be one longest common subsequence.

Sample input: "ZXVVYZW", "XKYKZPW"
Sample output: ["X", "Y", "Z", "W"]
"""


# SOLUTION 1

# O(nm*min(n,m)) time | O(nm*min(n,m)) space
def longestCommonSubsequence1(str1, str2):
    lcs = [[[] for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + [str2[i-1]]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key=len)
    return "".join(lcs[-1][-1])


# SOLUTION 2

# O(nm) time | O(nm) space
def longestCommonSubsequence2(str1, str2):
    lcs = [[[None, 0, None, None] for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                lcs[i][j] = [str2[i-1], lcs[i-1][j-1][1]+1, i-1, j-1]
            else:
                if lcs[i-1][j][1] > lcs[i][j-1][1]:
                    lcs[i][j] = [None, lcs[i-1][j][1], i-1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j-1][1], i, j-1]
    return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []
    i = len(lcs)-1
    j = len(lcs[0])-1
    while i != 0 and j != 0:
        currentEntry = lcs[i][j]
        if currentEntry[0] is not None:
            sequence.append(currentEntry[0])
        i = currentEntry[2]
        j = currentEntry[3]
    return "".join(list(reversed(sequence)))
