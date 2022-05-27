# [11. Container with Most Water](https://leetcode.com/problems/container-with-most-water/)

## Question
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example:

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```
## Topics
- two pointer

## Idea
- time complexity: O(n)
- space complexity: O(1)

Take two pointers: left and right. Declare a global max and take the area each iteration. Ask if the max is the global max or the local area each time. Then if the height at left is less than right, increment left, else, decrement right. This will gaurentee the max area becauase we are being greedy with which heights we are considering.
