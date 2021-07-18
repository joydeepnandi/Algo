Ambiguous Measurements

This problem deals with measuring cups that are missing important measuring labels. Specifically, a measuring cup only has two measuring lines, a Low (L) line and a High (H) line. This means that these cups can't precisely measure and can only guarantee that the substance poured into them will be between the L and H line. For example, you might have a measuring cup that has a Low line at 400ml and a high line at 435ml. This means that when you use this measuring cup, you can only be sure that what you're measuring is between 400ml and 435ml.

You're given a list of measuring cups containing their low and high lines as well as one low integer and one high integer representing a range for a target measurement. Write a function that returns a boolean representing whether you can use the cups to accurately measure a volume in the specified [low, high] range (the range is inclusive).

Note that:

Each measuring cup will be represented by a pair of positive integers [L, H], where 0 <= L <= H.
You'll always be given at least one measuring cup, and the low and high input parameters will always satisfy the following constraint: 0 <= low <= high.
Once you've measured some liquid, it will immediately be transferred to a larger bowl that will eventually (possibly) contain the target measurement.
You can't pour the contents of one measuring cup into another cup.

Sample Input
measuringCups = [
  [200, 210],
  [450, 465],
  [800, 850],
] 
low = 2100
high = 2300
Sample Output
true
// We use cup [450, 465] to measure four volumes:
// First measurement: Low = 450, High = 465
// Second measurement: Low = 450 + 450 = 900, High = 465 + 465 = 930
// Third measurement: Low = 900 + 450 = 1350, High = 930 + 465 = 1395
// Fourth measurement: Low = 1350 + 450 = 1800, High = 1395 + 465 = 1860

// Then we use cup [200, 210] to measure two volumes:
// Fifth measurement: Low = 1800 + 200 = 2000, High = 1860 + 210 = 2070
// Sixth measurement: Low = 2000 + 200 = 2200, High = 2070 + 210 = 2280

// We've measured a volume in the range [2200, 2280].
// This is within our target range, so we return `true`.

// Note: there are other ways to measure a volume in the target range.

Hints
Hint 1
Start by considering the last cup that you'll use in your sequence of measurements. If it isn't possible to use any of the cups as the last cup, then you can't measure the desired volume.

Hint 2
If the cup that you're going to use last has a measuring range of [100, 110] and you want to measure in the range of [500, 550], then after you pick this cup as the last cup, you need to measure a range of [400, 440]. Now, you can simply pick the last cup you'll use to measure this new range. If you continue these steps, you'll eventually know if you're able to measure the entire range or not.

Hint 3
Hint #2 should give you an idea of how to solve this problem recursively. Try every cup as the last cup for the starting range, then recursively try to measure the new ranges created after using the selected last cups. If you ever reach a point where one cup can measure the entire range, then you're finished and you can measure the target range. Try to think of a way to optimize this recursive approach, since it might involve a lot of repeated calculations.

Optimal Space & Time Complexity
O(low * high * n) time | O(low * high) space - where n is the number of measuring cups

Tests

Test Case 1
{
  "measuringCups": [
    [200, 210],
    [450, 465],
    [800, 850]
  ],
  "low": 2100,
  "high": 2300
}
Test Case 2
{
  "measuringCups": [
    [200, 210]
  ],
  "low": 10,
  "high": 20
}
Test Case 3
{
  "measuringCups": [
    [230, 240],
    [290, 310],
    [500, 515]
  ],
  "low": 2100,
  "high": 2300
}
Test Case 4
{
  "measuringCups": [
    [1, 3],
    [2, 4],
    [5, 6]
  ],
  "low": 100,
  "high": 101
}
Test Case 5
{
  "measuringCups": [
    [1, 3],
    [2, 4],
    [5, 6]
  ],
  "low": 100,
  "high": 120
}
Test Case 6
{
  "measuringCups": [
    [1, 3],
    [2, 4],
    [5, 6],
    [10, 20]
  ],
  "low": 10,
  "high": 12
}
Test Case 7
{
  "measuringCups": [
    [1, 3],
    [2, 4],
    [5, 7],
    [10, 20]
  ],
  "low": 10,
  "high": 12
}
Test Case 8
{
  "measuringCups": [
    [50, 60],
    [100, 120],
    [20, 40],
    [10, 15],
    [400, 500]
  ],
  "low": 1000,
  "high": 1050
}
Test Case 9
{
  "measuringCups": [
    [50, 65],
    [100, 120],
    [20, 40],
    [10, 15],
    [400, 500]
  ],
  "low": 1000,
  "high": 1200
}
Test Case 10
{
  "measuringCups": [
    [50, 65],
    [100, 120],
    [20, 40],
    [10, 15],
    [400, 500],
    [300, 350],
    [10, 25]
  ],
  "low": 3000,
  "high": 3300
}
Test Case 11
{
  "measuringCups": [
    [50, 60],
    [100, 120],
    [20, 40],
    [400, 500]
  ],
  "low": 1000,
  "high": 1050
}
Test Case 12
{
  "measuringCups": [
    [50, 65]
  ],
  "low": 200,
  "high": 200
}
Test Case 13
{
  "measuringCups": [
    [50, 50]
  ],
  "low": 200,
  "high": 200
}
Test Case 14
{
  "measuringCups": [
    [50, 50],
    [50, 51]
  ],
  "low": 200,
  "high": 200
}
Test Case 15
{
  "measuringCups": [
    [100, 150],
    [1000, 2000]
  ],
  "low": 0,
  "high": 1000
}
Test Case 16
{
  "measuringCups": [
    [10, 20]
  ],
  "low": 10,
  "high": 20
}
Test Case 17
{
  "measuringCups": [
    [15, 18]
  ],
  "low": 10,
  "high": 20
}
Test Case 18
{
  "measuringCups": [
    [15, 22]
  ],
  "low": 10,
  "high": 20
}