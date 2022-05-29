# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)


## Question

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

**Example 1**:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Example 2**:
```
Input: nums = [1]
Output: 1
```

**Example 3**:
```
Input: nums = [5,4,-1,7,8]
Output: 23
```

## Topics
- array
- dynamic programming

## Idea
- time complexity: O(N)
- space complexity: O(1)

Declare a global max and a local max. Scan the array sequentially and check if the local max goes below 0. If it does, reset it. Then continuously update the local max by adding each element to it. Then compare the local and global max and take the highest.
