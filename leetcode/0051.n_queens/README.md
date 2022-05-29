# [51. N-Queens](https://leetcode.com/problems/n-queens/)


## Question

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

**Example 1**:
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

**Example 2**:
```
Input: n = 1
Output: [["Q"]]
```

## Topics
- backtracking

## Idea
- time complexity: O(N^2)
- space complexity: O(N)

Create three sets, a column set to store distinct Queens in a each column, a positive diagonal set to store the Queens in the positive slope diagnoal spots, and a negative diagonal set. Then create a board where we can perform operations on. Create a backtracking method that has a base case of the row being equal to n. When it reaches the base case, create a copy of the board and add it to the result. Inside the backtracking method, go through each column and put each Queen in all the different spaces, then call the function recursively and increase the row we are on, and then remove all of the positions after the recursive call. Outside the backtracking function, call it initally with the first row. Return the result list that will hold all of the possible boards with the Queens in the correct positions.
