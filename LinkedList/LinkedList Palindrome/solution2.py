class LinkedList:

    def __init__(self, value):

        self.value = value

        self.next = None

# O(n) time | O(1) space - where n is the number of nodes in the Linked List

def linkedListPalindrome(head):
    slowNode = head

    fastNode = head

    while fastNode is not None and fastNode.next is not None:

        slowNode = slowNode.next

        fastNode = fastNode.next.next
    reversedSecondHalfNode = reverseLinkedList(slowNode)

    firstHalfNode = head


    while reversedSecondHalfNode is not None:

        if reversedSecondHalfNode.value != firstHalfNode.value:

            return False

        reversedSecondHalfNode = reversedSecondHalfNode.next

        firstHalfNode = firstHalfNode.next

    return True

def reverseLinkedList(head):
    previousNode, currentNode = None, head

    while currentNode is not None:

        nextNode = currentNode.next

        currentNode.next = previousNode

        previousNode = currentNode

        currentNode = nextNode

    return previousNode