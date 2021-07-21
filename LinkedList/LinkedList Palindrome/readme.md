Linked List Palindrome
Write a function that takes in the head of a Singly Linked List and returns a boolean representing whether the linked list's nodes form a palindrome. Your function shouldn't make use of any auxiliary data structure.

A palindrome is usually defined as a string that's written the same forward and backward. For a linked list's nodes to form a palindrome, their values must be the same when read from left to right and from right to left. Note that single-character strings are palindromes, which means that single-node linked lists form palindromes.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

You can assume that the input linked list will always have at least one node; in other words, the head will never be None / null.

Sample Input
head = 0 -> 1 -> 2 -> 2 -> 1 -> 0 // the head node with value 0
Sample Output
true

Hints
Hint 1
Think about comparing two nodes at a time. To determine if the linked list's nodes form a palindrome, which two nodes should we compare?

Hint 2
Following Hint #1, to determine if the linked list's nodes form a palindrome, we'll want to compare the first and last node, the second and second-to-last node, the third and third-to-last node, etc.. How can we compare all of these nodes recursively?

Hint 3
Putting aside the recursive solution hinted at in Hint #2, we can solve this problem iteratively and with no auxiliary space if we know how to reverse a linked list. How can reversing the linked list (or part of it) help us solve this problem?

Hint 4
Try reversing the second half of the linked list and then comparing nodes in the first half and in the reversed second half by simply iterating through both halves at the same time. You'll have to figure out where the second half of the linked list begins in order to reverse it.

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
      {"id": "2", "next": "2-2", "value": 2},
      {"id": "2-2", "next": "1-2", "value": 2},
      {"id": "1-2", "next": "0-2", "value": 1},
      {"id": "0-2", "next": null, "value": 0}
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
    "head": "0",
    "nodes": [
      {"id": "0", "next": "0-2", "value": 0},
      {"id": "0-2", "next": null, "value": 0}
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
      {"id": "3", "next": null, "value": 3}
    ]
  }
}
Test Case 6
{
  "linkedList": {
    "head": "6",
    "nodes": [
      {"id": "6", "next": "5", "value": 6},
      {"id": "5", "next": "4", "value": 5},
      {"id": "4", "next": "3", "value": 4},
      {"id": "3", "next": "4-2", "value": 3},
      {"id": "4-2", "next": "5-2", "value": 4},
      {"id": "5-2", "next": "6-2", "value": 5},
      {"id": "6-2", "next": null, "value": 6}
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
      {"id": "5", "next": "5-2", "value": 5},
      {"id": "5-2", "next": "4-2", "value": 5},
      {"id": "4-2", "next": "3-2", "value": 4},
      {"id": "3-2", "next": "2-2", "value": 3},
      {"id": "2-2", "next": "1-2", "value": 2},
      {"id": "1-2", "next": "0-2", "value": 1},
      {"id": "0-2", "next": "12", "value": 0},
      {"id": "12", "next": null, "value": 12}
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
      {"id": "5", "next": "5-2", "value": 5},
      {"id": "5-2", "next": "4-2", "value": 5},
      {"id": "4-2", "next": "3-2", "value": 4},
      {"id": "3-2", "next": "2-2", "value": 3},
      {"id": "2-2", "next": "1-2", "value": 2},
      {"id": "1-2", "next": "0-2", "value": 1},
      {"id": "0-2", "next": null, "value": 0}
    ]
  }
}
Test Case 9
{
  "linkedList": {
    "head": "10000",
    "nodes": [
      {"id": "10000", "next": "10000-2", "value": 10000},
      {"id": "10000-2", "next": "10000-3", "value": 10000},
      {"id": "10000-3", "next": null, "value": 10000}
    ]
  }
}
Test Case 10
{
  "linkedList": {
    "head": "10000",
    "nodes": [
      {"id": "10000", "next": "10000-2", "value": 10000},
      {"id": "10000-2", "next": "10000-3", "value": 10000},
      {"id": "10000-3", "next": "10000-4", "value": 10000},
      {"id": "10000-4", "next": null, "value": 10000}
    ]
  }
}
Test Case 11
{
  "linkedList": {
    "head": "3",
    "nodes": [
      {"id": "3", "next": "1", "value": 3},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3-2", "value": 2},
      {"id": "3-2", "next": null, "value": 3}
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
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "10", "value": 9},
      {"id": "10", "next": "11", "value": 10},
      {"id": "11", "next": "10-2", "value": 11},
      {"id": "10-2", "next": "9-2", "value": 10},
      {"id": "9-2", "next": "8-2", "value": 9},
      {"id": "8-2", "next": "7-2", "value": 8},
      {"id": "7-2", "next": "6-2", "value": 7},
      {"id": "6-2", "next": "5-2", "value": 6},
      {"id": "5-2", "next": "4-2", "value": 5},
      {"id": "4-2", "next": "3-2", "value": 4},
      {"id": "3-2", "next": "2-2", "value": 3},
      {"id": "2-2", "next": "1-2", "value": 2},
      {"id": "1-2", "next": null, "value": 1}
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
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": "9", "value": 8},
      {"id": "9", "next": "10", "value": 9},
      {"id": "10", "next": "11", "value": 10},
      {"id": "11", "next": "10-2", "value": 11},
      {"id": "10-2", "next": "9-2", "value": 10},
      {"id": "9-2", "next": "8-2", "value": 9},
      {"id": "8-2", "next": "7-2", "value": 8},
      {"id": "7-2", "next": "6-2", "value": 7},
      {"id": "6-2", "next": "5-2", "value": 6},
      {"id": "5-2", "next": "4-2", "value": 5},
      {"id": "4-2", "next": "3-2", "value": 4},
      {"id": "3-2", "next": "2-2", "value": 3},
      {"id": "2-2", "next": "1-2", "value": 2},
      {"id": "1-2", "next": "0-2", "value": 1},
      {"id": "0-2", "next": null, "value": 0}
    ]
  }
}
Test Case 14
{
  "linkedList": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "1-2", "value": 3},
      {"id": "1-2", "next": "2-2", "value": 1},
      {"id": "2-2", "next": null, "value": 2}
    ]
  }
}