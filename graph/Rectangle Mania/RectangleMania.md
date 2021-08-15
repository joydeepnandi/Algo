Rectangle Mania
Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates) and returns the number of rectangles formed by these coordinates.

A rectangle must have its four corners amongst the coordinates in order to be counted, and we only care about rectangles with sides parallel to the x and y axes (i.e., with horizontal and vertical sides--no diagonal sides).

You can also assume that no coordinate will be farther than 100 units from the origin.

Sample Input
coords = [
  [0, 0], [0, 1], [1, 1], [1, 0],
  [2, 1], [2, 0], [3, 1], [3, 0],
]
Sample Output
6

Hints
Hint 1
Try treating every coordinate as the potential lower left corner of a rectangle. What conditions would need to be met in order to actually have a rectangle with any given coordinate as its lower left corner?

Hint 2
Following Hint #1, if you treat every coordinate as the potential lower left corner of a rectangle, you can move in a clockwise pattern (i.e., directly up, then directly right, then directly down, and finally directly left) to try to find a rectangle. There are a few ways to do this, one of which involves storing, for every coordinate, all other coordinates that are directly above it, directly to the right of it, directly below it, and directly to the left of it. With this information, you can iterate through all of the coordinates and then traverse through potential rectangles in an up-right-down-left pattern.

Hint 3
Following Hint #2, do you actually need to store all of the coordinates above, to the right, below, and to the left of every coordinate?

Hint 4
Another, perhaps more clever way of solving this problem is to realize that, for any coordinate to be a valid lower left corner of a rectangle, there must be a corresponding upper right corner of the same rectangle, which is just another coordinate located to the upper right of the first coordinate. If you have two such coordinates, you should be able to easily find whether corresponding upper left and lower right corners exist.

Optimal Space & Time Complexity
O(n^2) time | O(n) space - where n is the number of coordinates

Tests

Test Case 1
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0]
  ]
}
Test Case 2
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0]
  ]
}
Test Case 3
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0]
  ]
}
Test Case 4
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0],
    [1, 3],
    [3, 3]
  ]
}
Test Case 5
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0],
    [1, 3],
    [3, 3],
    [0, -4],
    [3, -4]
  ]
}
Test Case 6
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0],
    [1, 3],
    [3, 3],
    [0, -4],
    [3, -4],
    [1, -3],
    [3, -3]
  ]
}
Test Case 7
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0],
    [1, 3],
    [3, 3],
    [0, -4],
    [3, -4],
    [1, -3],
    [3, -3],
    [-1, 0],
    [-10, 0],
    [-1, -1],
    [2, -2]
  ]
}
Test Case 8
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0],
    [1, 3],
    [3, 3],
    [0, -4],
    [3, -4],
    [1, -3],
    [3, -3],
    [-1, 0],
    [-10, 0],
    [-1, -1],
    [2, -2],
    [0, -1],
    [1, -4],
    [-10, -4]
  ]
}
Test Case 9
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 0],
    [2, 1],
    [1, 3],
    [3, 3],
    [0, -4],
    [3, -5],
    [1, -3],
    [3, -2],
    [-1, 0],
    [-10, 0],
    [-1, -1],
    [2, -2]
  ]
}
Test Case 10
{
  "coords": [
    [0, 0],
    [0, 1],
    [1, 1]
  ]
}