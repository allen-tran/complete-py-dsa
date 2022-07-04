# [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)


## Question
Given the root of a binary tree, return the inorder traversal of its nodes' values.


**Example 1**:
```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

**Example 2**:
```
Input: root = []
Output: []
```

**Example 3**:
```
Input: root = [1]
Output: [1]
```

## Topics
- recursion

## Idea
- time complexity: O(N)
- space complexity: O(N)

Start with an empty list holding the node values. Create a recursive helper function that has a node passed in. Call the helper function in an inorder manner and instead of printing the node.val, append it to the resultant list.