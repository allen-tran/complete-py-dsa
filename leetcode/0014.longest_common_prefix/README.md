# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)


## Question

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1**:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2**:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Topics
- sorting

## Idea
- time complexity: O(Nlog(N))
- space complexity: O(1)

Start by sorting the words list because the we want to take the smallest word anyways. Then scan every other word and compare the word to the result. If the word's prefix is not equal to the result, keep subtracting the result by 1 until they are equal. This will gaurentee a common prefix and the shortest one as well.