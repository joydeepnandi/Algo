Find Loop
Write a function that takes in the head of a Singly Linked List that contains a loop (in other words, the list's tail node points to some node in the list instead of None / null). The function should return the node (the actual node--not just its value) from which the loop originates in constant space.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 0
                           ^         v
                           9 <- 8 <- 7
Sample Output
4 -> 5 -> 6 // the node with value 4
^         v
9 <- 8 <- 7

Hints
Hint 1
Try traversing the linked list with two pointers, one iterating through every single node in the list and another iterating through every other node in the list (skipping a node every time). Eventually, both pointers will point to the same node since there is a loop in the list and since one pointer is moving faster than the other. Stop once the pointers overlap each other. How can you find the origin of the loop from here?

Hint 2
Can you come up with a mathematical relation between the respective distances traveled by each pointer? How far will the first pointer have traveled when the pointers overlap? What about the second pointer? How can this relation then help you find the actual origin of the loop in the list?

Hint 3
Let D be the distance between the start of the linked list and the origin of the loop in the list. Let P be distance between the origin of the loop and the node N where the first and second pointers overlap (going in the primary direction of the list). By the time the pointers reach N, the first pointer will have traveled a distance of length D + P, and the second pointer will have traveled a distance of length 2D + 2P, since it will have traveled twice as much as the first pointer. Thus, the distance between N and the origin of the loop (going in the primary direction of the list) can be arithmetically deduced to be 2D + 2P - D - 2P = D. With both pointers D length away from the origin of the loop, how can you find the origin?

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
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "4", "value": 9}
    ]
  }
}
Test Case 2
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "0", "value": 9}
    ]
  }
}
Test Case 3
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "1", "value": 9}
    ]
  }
}
Test Case 4
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "2", "value": 9}
    ]
  }
}
Test Case 5
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "3", "value": 9}
    ]
  }
}
Test Case 6
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "5", "value": 9}
    ]
  }
}
Test Case 7
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "6", "value": 9}
    ]
  }
}
Test Case 8
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "7", "value": 9}
    ]
  }
}
Test Case 9
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "8", "value": 9}
    ]
  }
}
Test Case 10
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "9", "value": 9}
    ]
  }
}
Test Case 11
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 5},
      {"id": "1", "next": "2", "value": 4},
      {"id": "2", "next": "3", "value": 3},
      {"id": "3", "next": "2", "value": 2}
    ]
  }
}
Test Case 12
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "2-2", "value": 6},
      {"id": "2-2", "next": "7", "value": 2},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "4", "value": 9}
    ]
  }
}
Test Case 13
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": "2-2", "value": 6},
      {"id": "2-2", "next": "7", "value": 2},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "2-2", "value": 9}
    ]
  }
}
Test Case 14
{
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "0-2", "value": 0},
      {"id": "0-2", "next": "0-3", "value": 0},
      {"id": "0-3", "next": "0-4", "value": 0},
      {"id": "0-4", "next": "0-5", "value": 0},
      {"id": "0-5", "next": "0-6", "value": 0},
      {"id": "0-6", "next": "0-7", "value": 0},
      {"id": "0-7", "next": "0-8", "value": 0},
      {"id": "0-8", "next": "0-9", "value": 0},
      {"id": "0-9", "next": "0-7", "value": 0}
    ]
  }
}