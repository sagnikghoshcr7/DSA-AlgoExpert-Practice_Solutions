"""
Group Anagrams

Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter.
For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.
Your function should return a list of anagram groups in no particular order.

Sample Input: ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
Sample Output: [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]]
"""


# SOLUTION 1

# O(w * n * log(n) + n * w * log(w)) time | O(wn) space - where w is the number of words and
# n is the length of the longest word
def groupAnagrams1(words):
    if len(words) == 0:
        return []

    sortedWords = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sortedWords[x])

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue

        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)

    return result


# SOLUTION 2

# O(w * n * log(n)) time | O(wn) space - where w is the number of words and
# n is the length of the longest word
def groupAnagrams2(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())
