Sum of Linked Lists
You're given two Linked Lists of potentially unequal length. Each Linked List represents a non-negative integer, where each node in the Linked List is a digit of that integer, and the first node in each Linked List always represents the least significant digit of the integer. Write a function that returns the head of a new Linked List that represents the sum of the integers represented by the two input Linked Lists.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list. The value of each LinkedList node is always in the range of 0 - 9.

Note: your function must create and return a new Linked List, and you're not allowed to modify either of the input Linked Lists.

Sample Input
linkedListOne = 2 -> 4 -> 7 -> 1
linkedListTwo = 9 -> 4 -> 5
Sample Output
1 -> 9 -> 2 -> 2
// linkedListOne represents 1742
// linkedListTwo represents 549
// 1742 + 549 = 2291

Hints
Hint 1
If you can determine the integers that each individual Linked List represents, then all you need to do is add these integers and create a new Linked List that represents the summed value.

Hint 2
If you go with the approach mentioned in Hint #1, you'll need to break down the sum of the two Linked Lists' numbers into its individual digits. Once you know these digits, you can create a new Linked List using them. This approach is fine, but you can solve this problem more elegantly, with a single iteration through the Linked Lists.

Hint 3
Is it necessary to know the entire numbers represented by both Linked Lists in order to calculate their sum? Think back to your elementary-school math class; how did you add two numbers together?

Hint 4
Since each Linked List's digits are ordered from least significant digit to most significant digit, you can simply loop through both Linked Lists, consider the digits with the same significance, and add these digits together while keeping track of any carry that comes out of the addition. At each iteration, when you add the two Linked List digits, also add the carry from the previous iteration. Create a new Linked List node that stores the calculated value, and add that to your new Linked List. Keep iterating until you reach the end of both Linked Lists and have no remaining carry.

Optimal Space & Time Complexity
O(max(n, m)) time | O(max(n, m)) space - where n is the length of the first Linked List and m is the length of the second Linked List

Tests
Test Case 1
{
  "linkedListOne": {
    "head": "2",
    "nodes": [
      {"id": "2", "next": "4", "value": 2},
      {"id": "4", "next": "7", "value": 4},
      {"id": "7", "next": "1", "value": 7},
      {"id": "1", "next": null, "value": 1}
    ]
  },
  "linkedListTwo": {
    "head": "9",
    "nodes": [
      {"id": "9", "next": "4", "value": 9},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": null, "value": 5}
    ]
  }
}
Test Case 2
{
  "linkedListOne": {
    "head": "2",
    "nodes": [
      {"id": "2", "next": null, "value": 2}
    ]
  },
  "linkedListTwo": {
    "head": "9",
    "nodes": [
      {"id": "9", "next": null, "value": 9}
    ]
  }
}
Test Case 3
{
  "linkedListOne": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "0-2", "value": 0},
      {"id": "0-2", "next": "0-3", "value": 0},
      {"id": "0-3", "next": "5", "value": 0},
      {"id": "5", "next": null, "value": 5}
    ]
  },
  "linkedListTwo": {
    "head": "9",
    "nodes": [
      {"id": "9", "next": null, "value": 9}
    ]
  }
}
Test Case 4
{
  "linkedListOne": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "1-2", "value": 1},
      {"id": "1-2", "next": "1-3", "value": 1},
      {"id": "1-3", "next": null, "value": 1}
    ]
  },
  "linkedListTwo": {
    "head": "9",
    "nodes": [
      {"id": "9", "next": "9-2", "value": 9},
      {"id": "9-2", "next": "9-3", "value": 9},
      {"id": "9-3", "next": null, "value": 9}
    ]
  }
}
Test Case 5
{
  "linkedListOne": {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": null, "value": 3}
    ]
  },
  "linkedListTwo": {
    "head": "6",
    "nodes": [
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "9", "value": 7},
      {"id": "9", "next": "1", "value": 9},
      {"id": "1", "next": "8", "value": 1},
      {"id": "8", "next": null, "value": 8}
    ]
  }
}
Test Case 6
{
  "linkedListOne": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": null, "value": 0}
    ]
  },
  "linkedListTwo": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": null, "value": 0}
    ]
  }
}
Test Case 7
{
  "linkedListOne": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": null, "value": 0}
    ]
  },
  "linkedListTwo": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "0-2", "value": 0},
      {"id": "0-2", "next": "0-3", "value": 0},
      {"id": "0-3", "next": "0-4", "value": 0},
      {"id": "0-4", "next": "0-5", "value": 0},
      {"id": "0-5", "next": "8", "value": 0},
      {"id": "8", "next": null, "value": 8}
    ]
  }
}
Test Case 8
{
  "linkedListOne": {
    "head": "4",
    "nodes": [
      {"id": "4", "next": "6", "value": 4},
      {"id": "6", "next": "9", "value": 6},
      {"id": "9", "next": "3", "value": 9},
      {"id": "3", "next": "1", "value": 3},
      {"id": "1", "next": null, "value": 1}
    ]
  },
  "linkedListTwo": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "0-2", "value": 0},
      {"id": "0-2", "next": "0-3", "value": 0},
      {"id": "0-3", "next": "0-4", "value": 0},
      {"id": "0-4", "next": "2", "value": 0},
      {"id": "2", "next": "7", "value": 2},
      {"id": "7", "next": null, "value": 7}
    ]
  }
}