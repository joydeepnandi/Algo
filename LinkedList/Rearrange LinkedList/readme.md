Rearrange Linked List
Write a function that takes in the head of a Singly Linked List and an integer k, rearranges the list in place (i.e., doesn't create a brand new list) around nodes with value k, and returns its new head.

Rearranging a Linked List around nodes with value k means moving all nodes with a value smaller than k before all nodes with value k and moving all nodes with a value greater than k after all nodes with value k.

All moved nodes should maintain their original relative ordering if possible.

Note that the linked list should be rearranged even if it doesn't have any nodes with value k.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be None / null.

Sample Input
head = 3 -> 0 -> 5 -> 2 -> 1 -> 4 // the head node with value 3
k = 3
Sample Output
0 -> 2 -> 1 -> 3 -> 5 -> 4 // the new head node with value 0
// Note that the nodes with values 0, 2, and 1 have
// maintained their original relative ordering, and
// so have the nodes with values 5 and 4.
Hints
Hint 1
The final linked list that you have to return essentially consists of three linked lists attached to one another: one with nodes whose values are smaller than k, one with nodes whose values are equal to k, and one with nodes whose values are greater than k.

Hint 2
Iterate through the linked list once, build the three linked lists mentioned in Hint #1 as you go, and finally connect these three linked lists to form the rearranged list.

Hint 3
To build the three linked lists mentioned in Hints #1 and #2, you'll have to keep track of their heads and tails and update the appropriate linked list's tail with each node that you traverse as you iterate through the main linked list. You can determine which linked list is the relevant one by simply comparing the value of the node that you're traversing to k.

Hint 4
Connecting the three linked lists mentioned in the previous Hint won't be as simple as it sounds, mainly because one or two of the linked lists might actually be empty, depending on the various nodes' values and the value of k.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the number of nodes in the Linked List

Tests
Test Case 1
{
  "linkedList": {
    "head": "3",
    "nodes": [
      {"id": "3", "next": "0", "value": 3},
      {"id": "0", "next": "5", "value": 0},
      {"id": "5", "next": "2", "value": 5},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": null, "value": 4}
    ]
  },
  "k": 3
}
Test Case 2
{
  "linkedList": {
    "head": "3",
    "nodes": [
      {"id": "3", "next": "0", "value": 3},
      {"id": "0", "next": "2", "value": 0},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": null, "value": 5}
    ]
  },
  "k": 4
}
Test Case 3
{
  "linkedList": {
    "head": "3",
    "nodes": [
      {"id": "3", "next": "0", "value": 3},
      {"id": "0", "next": "2", "value": 0},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": null, "value": 5}
    ]
  },
  "k": 5
}
Test Case 4
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "3", "value": 0},
      {"id": "3", "next": "2", "value": 3},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": null, "value": 5}
    ]
  },
  "k": 0
}
Test Case 5
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "3", "value": 0},
      {"id": "3", "next": "2", "value": 3},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "3-2", "value": 5},
      {"id": "3-2", "next": "-1", "value": 3},
      {"id": "-1", "next": "-2", "value": -1},
      {"id": "-2", "next": "3-3", "value": -2},
      {"id": "3-3", "next": "6", "value": 3},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "3-4", "value": 7},
      {"id": "3-4", "next": "2-2", "value": 3},
      {"id": "2-2", "next": "-9000", "value": 2},
      {"id": "-9000", "next": null, "value": -9000}
    ]
  },
  "k": -9000
}
Test Case 6
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "3", "value": 0},
      {"id": "3", "next": "2", "value": 3},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "3-2", "value": 5},
      {"id": "3-2", "next": "-1", "value": 3},
      {"id": "-1", "next": "-2", "value": -1},
      {"id": "-2", "next": "3-3", "value": -2},
      {"id": "3-3", "next": "6", "value": 3},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "3-4", "value": 7},
      {"id": "3-4", "next": "2-2", "value": 3},
      {"id": "2-2", "next": "-9000", "value": 2},
      {"id": "-9000", "next": null, "value": -9000}
    ]
  },
  "k": 2
}
Test Case 7
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "3", "value": 0},
      {"id": "3", "next": "2", "value": 3},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "3-2", "value": 5},
      {"id": "3-2", "next": "-1", "value": 3},
      {"id": "-1", "next": "-2", "value": -1},
      {"id": "-2", "next": "3-3", "value": -2},
      {"id": "3-3", "next": "6", "value": 3},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "3-4", "value": 7},
      {"id": "3-4", "next": "2-2", "value": 3},
      {"id": "2-2", "next": "-9000", "value": 2},
      {"id": "-9000", "next": null, "value": -9000}
    ]
  },
  "k": 3
}
Test Case 8
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "3-2", "value": 3},
      {"id": "3-2", "next": "3-3", "value": 3},
      {"id": "3-3", "next": "3-4", "value": 3},
      {"id": "3-4", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": null, "value": 9}
    ]
  },
  "k": 3
}
Test Case 9
{
  "linkedList": {
    "head": "3",
    "nodes": [
      {"id": "3", "next": "0", "value": 3},
      {"id": "0", "next": "5", "value": 0},
      {"id": "5", "next": "2", "value": 5},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": null, "value": 4}
    ]
  },
  "k": -1
}
Test Case 10
{
  "linkedList": {
    "head": "3",
    "nodes": [
      {"id": "3", "next": "0", "value": 3},
      {"id": "0", "next": "5", "value": 0},
      {"id": "5", "next": "2", "value": 5},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": null, "value": 4}
    ]
  },
  "k": 6
}
Test Case 11
{
  "linkedList": {
    "head": "6",
    "nodes": [
      {"id": "6", "next": "0", "value": 6},
      {"id": "0", "next": "5", "value": 0},
      {"id": "5", "next": "2", "value": 5},
      {"id": "2", "next": "1", "value": 2},
      {"id": "1", "next": "4", "value": 1},
      {"id": "4", "next": null, "value": 4}
    ]
  },
  "k": 3
}