Nth Fibonacci

The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and F1 = 1. For the purpose of this question, the first Fibonacci number is F0; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc..

Sample Input #1
n = 2
Sample Output #1
1 // 0, 1

Sample Input #2
n = 6
Sample Output #2
5 // 0, 1, 1, 2, 3, 5


Hints
Hint 1
The formula to generate the nth Fibonacci number can be written as follows: F(n) = F(n - 1) + F(n - 2). Think of the case(s) for which this formula doesn't apply (the base case(s)) and try to implement a simple recursive algorithm to find the nth Fibonacci number with this formula.

Hint 2
What are the runtime implications of solving this problem as is described in Hint #1? Can you use memoization (caching) to improve the performance of your algorithm?

Hint 3
Realize that to calculate any single Fibonacci number you only need to have the two previous Fibonacci numbers. Knowing this, can you implement an iterative algorithm to solve this question, storing only the last two Fibonacci numbers at any given time?

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the input number

Test Case 1

  "n": 6

Test Case 2

  "n": 1

Test Case 3

  "n": 2

Test Case 4

  "n": 3
  
Test Case 5

  "n": 4

Test Case 6

  "n": 5

Test Case 7

  "n": 7

Test Case 8

  "n": 8

Test Case 9

  "n": 9

Test Case 10

  "n": 10

Test Case 11

  "n": 11

Test Case 12

  "n": 12

Test Case 13

  "n": 13

Test Case 14

  "n": 14

Test Case 15

  "n": 15

Test Case 16

  "n": 16

Test Case 17

  "n": 17

Test Case 18

  "n": 18
