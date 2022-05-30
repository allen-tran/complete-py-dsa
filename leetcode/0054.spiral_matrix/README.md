# [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)


## Question

Given an m x n matrix, return all elements of the matrix in spiral order.

**Example 1**:
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2**:
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Topics
- array
- matrix
- simulation

## Idea
- time complexity: O(N*M)
- space complexity: O(N*M)

Declare a top, right, left, and bottom pointer. Start a while loop that continues while the left is less than the right and top is less than the bottom. Then go through 4 loops with the respecitve traversal. With each traversal, shrink that portion of the matrix down by one so the pointers can allown the inner matrices to be traversed.
