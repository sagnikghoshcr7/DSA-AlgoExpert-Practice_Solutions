"""
Remove Kth Node From End

Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end
of the list.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list
or to None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least 2 nodes and, more specifically, at least k nodes.

Sample Input:
head = 0 ->  1 ->  2 ->  3 ->  4 ->  5 ->  6 ->  7 ->  8 ->  9 // the head node with value 0
k = 4

Sample Output:
// No output required.
// The 4th node from the end of the list (the node with value 6) is removed.
0 ->  1 ->  2 ->  3 ->  4 ->  5 ->  7 ->  8 ->  9
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
