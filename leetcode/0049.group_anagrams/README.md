# [49. Group Anagrams](https://leetcode.com/problems/group_anagrams/)


## Question

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1**:
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2**:
```
Input: strs = [""]
Output: [[""]]
```

**Example 3**:
```
Input: strs = ["a"]
Output: [["a"]]
```

## Topics
- sorting
- hash map

## Idea
- time complexity: O(Nlog(N))
- space complexity: O(N)

Declare a hashmap to store the words and sorted words in. The key is the sorted word and the values are lists of the words in original form. Scan through the list of strings and if the word exists in the dictionary, add it to the value, if not create a new key of it in sorted form. Then at the end return a list of lists that holds the values of the dicitonary.
