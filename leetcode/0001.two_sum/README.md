# [1. Two Sum](https://leetcode.com/problems/two-sum/)

## Question
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
## Topic
Find two numbers that add up to the target value and return their indicies.

## Idea
- time complexity: O(n)
- space complexity: O(n)

Scan the array in one pass then for each number you consider, take the difference from the target and check if it exists in the array. If it does then return the two number's indicies. If not, store the numebr as the key and the index as the value.
