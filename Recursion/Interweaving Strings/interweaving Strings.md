Interweaving Strings

Write a function that takes in three strings and returns a boolean representing whether the third string can be formed by interweaving the first two strings.

To interweave strings means to merge them by alternating their letters without any specific pattern. For instance, the strings "abc" and "123" can be interwoven as "a1b2c3", as "abc123", and as "ab1c23" (this list is nonexhaustive).

Letters within a string must maintain their relative ordering in the interwoven string.

Sample Input
one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"
Sample Output
true


Hints

Hint 1
Try traversing the three strings with three different pointers to solve this problem.

Hint 2
Declare three variables (i, j, and k, for instance) pointing to indices in the three strings, respectively, and starting at 0. At any given combination of indices, if neither the character at i in the first string nor the character at j in the second string is equal to the character at k in the third string, then the first two strings can't interweave to form the third one (at least not in whatever way led to the values of i, j, and k in question).

Hint 3
If at any given combination of the indices i, j, and k mentioned in Hint #2, the character at i in the first string or the character at j in the second string is equal to the character at k in the third string, then you can potentially interweave the first two strings to get the third one. In such a case, try incrementing the two relevant indices (i and k or j and k) and repeating this process until you confirm whether or not the first two strings can be interwoven to form the third one. Try using recursion to implement this algorithm.

Hint 4
By following Hint #3, you'll perform, in some cases, many computations multiple times. How can you use caching to improve the time complexity of this algorithm?

Optimal Space & Time Complexity
O(nm) time | O(nm) space - where n is the length of the first string and m is the length of the second string

Tests

Test Case 1
{
  "one": "algoexpert",
  "two": "your-dream-job",
  "three": "your-algodream-expertjob"
}
Test Case 2
{
  "one": "a",
  "two": "b",
  "three": "ab"
}
Test Case 3
{
  "one": "a",
  "two": "b",
  "three": "ba"
}
Test Case 4
{
  "one": "a",
  "two": "b",
  "three": "ac"
}
Test Case 5
{
  "one": "abc",
  "two": "def",
  "three": "abcdef"
}
Test Case 6
{
  "one": "abc",
  "two": "def",
  "three": "adbecf"
}
Test Case 7
{
  "one": "abc",
  "two": "def",
  "three": "deabcf"
}
Test Case 8
{
  "one": "aabcc",
  "two": "dbbca",
  "three": "aadbbcbcac"
}
Test Case 9
{
  "one": "aabcc",
  "two": "dbbca",
  "three": "aadbbbaccc"
}
Test Case 10
{
  "one": "algoexpert",
  "two": "your-dream-job",
  "three": "ayloguore-xdpreeratm-job"
}
Test Case 11
{
  "one": "aaaaaaa",
  "two": "aaaabaaa",
  "three": "aaaaaaaaaaaaaab"
}
Test Case 12
{
  "one": "aaaaaaa",
  "two": "aaaaaaa",
  "three": "aaaaaaaaaaaaaa"
}
Test Case 13
{
  "one": "aacaaaa",
  "two": "aaabaaa",
  "three": "aaaabacaaaaaaa"
}
Test Case 14
{
  "one": "aacaaaa",
  "two": "aaabaaa",
  "three": "aaaacabaaaaaaa"
}
Test Case 15
{
  "one": "aacaaaa",
  "two": "aaabaaa",
  "three": "aaaaaacbaaaaaa"
}
Test Case 16
{
  "one": "algoexpert",
  "two": "your-dream-job",
  "three": "1your-algodream-expertjob"
}
Test Case 17
{
  "one": "algoexpert",
  "two": "your-dream-job",
  "three": "your-algodream-expertjob1"
}
Test Case 18
{
  "one": "algoexpert",
  "two": "your-dream-job",
  "three": "your-algodream-expertjo"
}
Test Case 19
{
  "one": "ae",
  "two": "e",
  "three": "see"
}
Test Case 20
{
  "one": "algo",
  "two": "frog",
  "three": "fralgogo"
}