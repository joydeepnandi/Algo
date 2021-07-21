Zip Linked List
You're given the head of a Singly Linked List of arbitrary length k. Write a function that zips the Linked List in place (i.e., doesn't create a brand new list) and returns its head.

A Linked List is zipped if its nodes are in the following order, where k is the length of the Linked List:

1st node -> kth node -> 2nd node -> (k - 1)th node -> 3rd node -> (k - 2)th node -> ...
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be None / null.

Sample Input
linkedList = 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 1 
Sample Output
1 -> 6 -> 2 -> 5 -> 3 -> 4 // the head node with value 1


Hints
Hint 1
Try to imagine how you would solve this problem if you were given two distinct linked lists. For example, how would you zip the list 1 -> 2 -> 3 with the list 4 -> 5 to get 1 -> 5 -> 2 -> 4 -> 3?

Hint 2
One of the most straightforward ways to solve this problem is to split the original linked list into two linked lists and to reverse the second linked list before interweaving it with the first one. Ultimately, you want the first node, then the kth node, then the second node, etc., so reversing the second linked list before interweaving it with the first one makes things simple.

Hint 3
After you split the linked list into two halves and reverse the second half, you'll have something like 1 -> 2 -> 3 and 5 -> 4; at this point, you can simply add the first node of the reversed second half into the first half between 1 and 2 as in 1 -> 5 -> 2.... Simply continue this process until you've inserted all of the nodes from the reversed second half into the first.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input Linked List

Tests
Test Case 1
{
  "linkedList": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": "6", "value": 5},
      {"id": "6", "next": null, "value": 6}
    ]
  }
}
Test Case 2
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
      {"id": "7", "next": null, "value": 7}
    ]
  }
}
Test Case 3
{
  "linkedList": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": null, "value": 3}
    ]
  }
}
Test Case 4
{
  "linkedList": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": null, "value": 2}
    ]
  }
}
Test Case 5
{
  "linkedList": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": null, "value": 1}
    ]
  }
}
Test Case 6
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
      {"id": "9", "next": null, "value": 9}
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
      {"id": "10", "next": null, "value": 10}
    ]
  }
}
Test Case 8
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
      {"id": "11", "next": null, "value": 11}
    ]
  }
}
Test Case 9
{
  "linkedList": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "-6", "value": 1},
      {"id": "-6", "next": "8", "value": -6},
      {"id": "8", "next": "5", "value": 8},
      {"id": "5", "next": "10", "value": 5},
      {"id": "10", "next": "-1", "value": 10},
      {"id": "-1", "next": "0", "value": -1},
      {"id": "0", "next": "2", "value": 0},
      {"id": "2", "next": "11", "value": 2},
      {"id": "11", "next": "-100", "value": 11},
      {"id": "-100", "next": "99", "value": -100},
      {"id": "99", "next": null, "value": 99}
    ]
  }
}
Test Case 10
{
  "linkedList": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "-6", "value": 1},
      {"id": "-6", "next": "8", "value": -6},
      {"id": "8", "next": "5", "value": 8},
      {"id": "5", "next": "10", "value": 5},
      {"id": "10", "next": "-1", "value": 10},
      {"id": "-1", "next": "0", "value": -1},
      {"id": "0", "next": "2", "value": 0},
      {"id": "2", "next": "11", "value": 2},
      {"id": "11", "next": "-100", "value": 11},
      {"id": "-100", "next": "99", "value": -100},
      {"id": "99", "next": "50", "value": 99},
      {"id": "50", "next": null, "value": 50}
    ]
  }
}