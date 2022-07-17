# [0198. House Robber](https://leetcode.com/problems/house-robber/)


## Question



**Example 1**:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 2**:
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## Topics
- dynamic programming

## Idea
- time complexity: O(N)
- space complexity: O(N)

First start by creating a dp cache which will be a 1D array that holds the max profits for all of the houses we have seen so far at each index. We start off the cache by populating the 0th index with the first house (since that is the only option with one house) and the 1th index with the max of the 0th index and the 1th index of the original given nums array. Then we loop from range 2 -> len(nums) and with each iteration we have two choices with different profits. The whole idea of this problem is to maximize these profits so we pick the bigger of the two. The first profit is if we rob the curr house so we make profit1 equal to the nums at this index + the dp at 2 indicies ago. The second profit will just be equal to the dp at the index of the current index-1. This is because we could choose to skip robbing this house and instead just take the profit from the last house. We take the max of these two and by the end we just need to return the last element in the dp cache.
