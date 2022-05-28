# [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)


## Question

Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

**Example 1**:
```
Input: haystack = "hello", needle = "ll"
Output: 2
```

**Example 2**:
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

## Topics
- array

## Idea
- time complexity: O(N)
- space complexity: O(1)

Scan the haystack iteratively and compare the needle to the letters in haystack. Make sure the letters is a substring of the same length of the needle.
