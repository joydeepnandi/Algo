Node Swap
Write a function that takes in the head of a Singly Linked List, swaps every pair of adjacent nodes in place (i.e., doesn't create a brand new list), and returns its new head.

If the input Linked List has an odd number of nodes, its final node should remain the same.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be None / null.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0
Sample Output
1 -> 0 -> 3 -> 2 -> 5 -> 4 // the new head node with value 1

Hints
Hint 1
Each node in the linked list points to the next node in the linked list. How would you modify the next pointers of two nodes in order to swap them?

Hint 2
Can you apply what you come up with from Hint #1 in order to solve this problem recursively?

Hint 3
To solve this problem recursively, have each recursive call swap a pair of nodes and then return the first node of the swapped pair (the node that was originally the second node in the pair). Also, have each recursive call make the second node of the swapped pair (the node that was originally the first node in the pair) point to the result of the next recursive call. The next recursive call should take in the first node of the next pair as its input parameter.

Hint 4
Implementing this problem iteratively can improve the space complexity of the solution. Intuitively, you need swap nodes while traversing the entire linked list. To do this, you'll need to reference and change the pointers of three nodes at a time. You'll also need to create a placeholder node that points to the head of the linked list, so that at the end of the traversal, you can still reference the new head that you have to return.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the number of nodes in the Linked List

Tests

Test Case 1
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": null, "value": 5}
    ]
  }
}
Test Case 2
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": null, "value": 0}
    ]
  }
}
Test Case 3
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": null, "value": 1}
    ]
  }
}
Test Case 4
{
  "linkedList": {
    "head": "5",
    "nodes": [
      {"id": "5", "next": "10", "value": 5},
      {"id": "10", "next": "15", "value": 10},
      {"id": "15", "next": "20", "value": 15},
      {"id": "20", "next": "25", "value": 20},
      {"id": "25", "next": "30", "value": 25},
      {"id": "30", "next": null, "value": 30}
    ]
  }
}
Test Case 5
{
  "linkedList": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "3", "value": 1},
      {"id": "3", "next": "9", "value": 3},
      {"id": "9", "next": "6", "value": 9},
      {"id": "6", "next": "20", "value": 6},
      {"id": "20", "next": "4", "value": 20},
      {"id": "4", "next": null, "value": 4}
    ]
  }
}
Test Case 6
{
  "linkedList": {
    "head": "5",
    "nodes": [
      {"id": "5", "next": "4", "value": 5},
      {"id": "4", "next": "3", "value": 4},
      {"id": "3", "next": "2", "value": 3},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "0", "value": 1},
      {"id": "0", "next": null, "value": 0}
    ]
  }
}
Test Case 7
{
  "linkedList": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "10", "value": 9},
      {"id": "10", "next": "11", "value": 10},
      {"id": "11", "next": "12", "value": 11},
      {"id": "12", "next": "13", "value": 12},
      {"id": "13", "next": "14", "value": 13},
      {"id": "14", "next": "15", "value": 14},
      {"id": "15", "next": null, "value": 15}
    ]
  }
}
Test Case 8
{
  "linkedList": {
    "head": "10",
    "nodes": [
      {"id": "10", "next": "20", "value": 10},
      {"id": "20", "next": "30", "value": 20},
      {"id": "30", "next": null, "value": 30}
    ]
  }
}
Test Case 9
{
  "linkedList": {
    "head": "30",
    "nodes": [
      {"id": "30", "next": "10", "value": 30},
      {"id": "10", "next": "20", "value": 10},
      {"id": "20", "next": null, "value": 20}
    ]
  }
}
Test Case 10
{
  "linkedList": {
    "head": "2",
    "nodes": [
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": "3", "value": 4},
      {"id": "3", "next": "6", "value": 3},
      {"id": "6", "next": "5", "value": 6},
      {"id": "5", "next": "8", "value": 5},
      {"id": "8", "next": "7", "value": 8},
      {"id": "7", "next": "10", "value": 7},
      {"id": "10", "next": "9", "value": 10},
      {"id": "9", "next": null, "value": 9}
    ]
  }
}