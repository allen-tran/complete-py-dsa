# [0240. Search in a 2D Matrix II](https://leetcode.com/problems//)


## Question
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


**Example 1**:
```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

**Example 2**:
```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

## Topics
- binary seach

## Idea
- time complexity: O(N+M)
- space complexity: O(1)

Since the matrix is sorted in a particular way, we can take advantage of this and perform a modified binary search. We can initalize two pointers: a row and column, that we point to the bottom left element in the matrix. While the row is greater than 0 and the column is less than the length of a row in the matrix, we can keep searching. If the target is greater than the number we are looking at, we can move right a column. If the number target is less than the number, we can move up a row and begin searching there. This is because the matrix is sorted from left to right and top to bottom.