Linked List Construction
Write a DoublyLinkedList class that has a head and a tail, both of which point to either a linked list Node or None / null. The class should support:

Setting the head and tail of the linked list.
Inserting nodes before and after other nodes as well as at given positions (the position of the head node is 1).
Removing given nodes and removing nodes with given values.
Searching for nodes with given values.
Note that the setHead, setTail, insertBefore, insertAfter, insertAtPosition, and remove methods all take in actual Nodes as input parameters—not integers (except for insertAtPosition, which also takes in an integer representing the position); this means that you don't need to create any new Nodes in these methods. The input nodes can be either stand-alone nodes or nodes that are already in the linked list. If they're nodes that are already in the linked list, the methods will effectively be moving the nodes within the linked list. You won't be told if the input nodes are already in the linked list, so your code will have to defensively handle this scenario.

If you're doing this problem in an untyped language like Python or JavaScript, you may want to look at the various function signatures in a typed language like Java or TypeScript to get a better idea of what each input parameter is.

Each Node has an integer value as well as a prev node and a next node, both of which can point to either another node or None / null.

Sample Usage
// Assume the following linked list has already been created:
1 <-> 2 <-> 3 <-> 4 <-> 5
// Assume that we also have the following stand-alone nodes:
3, 3, 6
setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as the head
setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with value 6 as the tail
insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the existing node with value 6
insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 after the existing node with value 6
insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 in position 1
removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value 3
remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2
containsNodeWithValue(5): true


Hints
Hint 1
When dealing with linked lists, it's very important to keep track of pointers on nodes (i.e., the "next" and "prev" properties on the nodes). For instance, if you're inserting a node in a linked list, but that node is already located somewhere else in the linked list (in other words, if you're moving a node), it's crucial to completely update the pointers of the adjacent nodes of the node being moved before updating the node's own pointers. The order in which you update nodes' pointers will make or break your algorithm.

Hint 2
Realize that the insertBefore() and insertAfter() methods can be used to implement the setHead(), setTail(), and insertAtPosition() methods; making the insertBefore() and insertAfter() methods as robust as possible will simplify your code for the other methods. Make sure to take care of edge cases involving inserting nodes before the head of the linked list or inserting nodes after the tail of the linked list.

Hint 3
Similar to Hint #2, realize that the remove() method can be used to implement the removeNodesWithValue() method as well as parts of the insertBefore() and insertAfter() methods; make sure that the remove() method handles edge cases regarding the head and the tail.

Optimal Space & Time Complexity
setHead, setTail, insertBefore, insertAfter, and remove: O(1) time | O(1) space insertAtPosition: O(p) time | O(1) space - where p is input position removeNodesWithValue, containsNodeWithValue: O(n) time | O(1) space - where n is the number of nodes in the linked list

Tests

Test Case 1
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "3-2", "next": null, "prev": null, "value": 3},
    {"id": "3-3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4},
    {"id": "5", "next": null, "prev": null, "value": 5},
    {"id": "6", "next": null, "prev": null, "value": 6}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["5"],
      "method": "setHead"
    },
    {
      "arguments": ["4"],
      "method": "setHead"
    },
    {
      "arguments": ["3"],
      "method": "setHead"
    },
    {
      "arguments": ["2"],
      "method": "setHead"
    },
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["4"],
      "method": "setHead"
    },
    {
      "arguments": ["6"],
      "method": "setTail"
    },
    {
      "arguments": ["6", "3"],
      "method": "insertBefore"
    },
    {
      "arguments": ["6", "3-2"],
      "method": "insertAfter"
    },
    {
      "arguments": [1, "3-3"],
      "method": "insertAtPosition"
    },
    {
      "arguments": [3],
      "method": "removeNodesWithValue"
    },
    {
      "arguments": ["2"],
      "method": "remove"
    },
    {
      "arguments": [5],
      "method": "containsNodeWithValue"
    }
  ]
}
Test Case 2
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    }
  ]
}
Test Case 3
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setTail"
    }
  ]
}
Test Case 4
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1}
  ],
  "classMethodsToCall": [
    {
      "arguments": [1, "1"],
      "method": "insertAtPosition"
    }
  ]
}
Test Case 5
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["2"],
      "method": "setTail"
    }
  ]
}
Test Case 6
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["2"],
      "method": "setHead"
    }
  ]
}
Test Case 7
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    }
  ]
}
Test Case 8
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertBefore"
    }
  ]
}
Test Case 9
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertAfter"
    }
  ]
}
Test Case 10
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setTail"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertBefore"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertBefore"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertBefore"
    }
  ]
}
Test Case 11
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertAfter"
    },
    {
      "arguments": ["1"],
      "method": "setTail"
    }
  ]
}
Test Case 12
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setTail"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertBefore"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertBefore"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertBefore"
    },
    {
      "arguments": ["1"],
      "method": "setHead"
    }
  ]
}
Test Case 13
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "1"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertBefore"
    }
  ]
}
Test Case 14
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4},
    {"id": "5", "next": null, "prev": null, "value": 5},
    {"id": "6", "next": null, "prev": null, "value": 6},
    {"id": "7", "next": null, "prev": null, "value": 7}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertAfter"
    },
    {
      "arguments": ["4", "5"],
      "method": "insertAfter"
    },
    {
      "arguments": ["5", "6"],
      "method": "insertAfter"
    },
    {
      "arguments": ["6", "7"],
      "method": "insertAfter"
    },
    {
      "arguments": [7, "1"],
      "method": "insertAtPosition"
    },
    {
      "arguments": [1, "1"],
      "method": "insertAtPosition"
    },
    {
      "arguments": [2, "1"],
      "method": "insertAtPosition"
    },
    {
      "arguments": [3, "1"],
      "method": "insertAtPosition"
    },
    {
      "arguments": [4, "1"],
      "method": "insertAtPosition"
    },
    {
      "arguments": [5, "1"],
      "method": "insertAtPosition"
    },
    {
      "arguments": [6, "1"],
      "method": "insertAtPosition"
    }
  ]
}
Test Case 15
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1"],
      "method": "remove"
    }
  ]
}
Test Case 16
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": [1],
      "method": "removeNodesWithValue"
    }
  ]
}
Test Case 17
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertAfter"
    },
    {
      "arguments": ["1"],
      "method": "remove"
    }
  ]
}
Test Case 18
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertAfter"
    },
    {
      "arguments": ["4"],
      "method": "remove"
    }
  ]
}
Test Case 19
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2"],
      "method": "remove"
    }
  ]
}
Test Case 20
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "1-2", "next": null, "prev": null, "value": 1},
    {"id": "1-3", "next": null, "prev": null, "value": 1},
    {"id": "1-4", "next": null, "prev": null, "value": 1}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "1-2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["1-2", "1-3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["1-3", "1-4"],
      "method": "insertAfter"
    },
    {
      "arguments": [1],
      "method": "removeNodesWithValue"
    }
  ]
}
Test Case 21
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "1-2", "next": null, "prev": null, "value": 1},
    {"id": "1-3", "next": null, "prev": null, "value": 1},
    {"id": "1-4", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "1-2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["1-2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "1-3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["1-3", "4"],
      "method": "insertAfter"
    },
    {
      "arguments": [1],
      "method": "removeNodesWithValue"
    }
  ]
}
Test Case 22
{
  "nodes": [
    {"id": "1", "next": null, "prev": null, "value": 1},
    {"id": "2", "next": null, "prev": null, "value": 2},
    {"id": "3", "next": null, "prev": null, "value": 3},
    {"id": "4", "next": null, "prev": null, "value": 4}
  ],
  "classMethodsToCall": [
    {
      "arguments": ["1"],
      "method": "setHead"
    },
    {
      "arguments": ["1", "2"],
      "method": "insertAfter"
    },
    {
      "arguments": ["2", "3"],
      "method": "insertAfter"
    },
    {
      "arguments": ["3", "4"],
      "method": "insertAfter"
    },
    {
      "arguments": [1],
      "method": "containsNodeWithValue"
    },
    {
      "arguments": [2],
      "method": "containsNodeWithValue"
    },
    {
      "arguments": [3],
      "method": "containsNodeWithValue"
    },
    {
      "arguments": [4],
      "method": "containsNodeWithValue"
    },
    {
      "arguments": [5],
      "method": "containsNodeWithValue"
    }
  ]
}