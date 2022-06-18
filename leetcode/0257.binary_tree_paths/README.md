# [0257. Binary Tree Paths ](https://leetcode.com/problems/binary-tree-paths/)


## Question
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

**Example 1**:
```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

**Example 2**:
```
Input: root = [1]
Output: ["1"]
```

## Topics
- depth-first search

## Idea
- time complexity: O(N)
- space complexity: O(1)

Start with a resultant list to store each path you can take. Then call DFS with the list, the root, and a temporary string. Next create a new function that first checks if the node exists. If it does, add to the temp string with the node's values. Then call dfs on the node's left value and the node's right value. Make sure to add the arrows to the current string. Then we know to get out of the dfs function when there is no node.left and no node.right. We add the string to the list if that is the case.
