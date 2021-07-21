# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(n) space - where n is the number of nodes in the Linked List

def nodeSwap(head):

    if head is None or head.next is None:
        return head

    nextNode = head.next
    head.next = nodeSwap(head.next.next)
    nextNode.next = head
    return nextNode
