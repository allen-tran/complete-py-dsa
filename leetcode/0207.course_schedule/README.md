# [0207. Course Schedule](https://leetcode.com/problems/course-schedule/)


## Question
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


**Example 1**:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

**Example 2**:
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

## Topics
- topological sort

## Idea
- time complexity: O(V+E)
- space complexity: O(V+E)

There are 5 steps to every topological sort algorithm. First, initialize the graph and indegrees dictionaries. The graph will have the parent as the key and a list of child nodes. The indegrees will have the nodes as a key and an integer representing how many edges are coming in to the node. Second, build the graph and the indegrees. Third, create a queue and populate the queue with all of the sources. Fourth go through the sources queue and popleft the vertecies while also append it to a sorted_order list. For each vertex, go through the children node and decretement the indegeres. Then check if the indegrees is 0. If it is, added it to the queue. Fifth, check if the number vertices given by the problem are the same as the length of the sorted_order list.
